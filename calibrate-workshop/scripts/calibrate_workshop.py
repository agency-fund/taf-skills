"""Set up and run the Calibrate side of a labeling workshop with the workspace API key.

Subcommands (all read workshop.json; the API key comes from CALIBRATE_API_KEY in .env):

    check              confirm the key works against the configured server
    create             evaluators -> annotation task -> question order + optional questions -> items
    annotators         make sure every name in "annotators" exists in the workspace
    jobs               one labeling job per annotator (all items), then write the links file
    links              read the jobs back and write the links file (no writes to Calibrate)
    run-judge          run the AI judge (live evaluator versions) on every item
    update-evaluators  push changed judge prompts / answer options as new live versions
    status             item count, questions, and each annotator's progress

Safety switches:
    --dry-run   read from Calibrate but write nothing; print each write it would make
    --offline   no network at all; print every request that would be sent (for practice runs)

Self-hosted Calibrate: set calibrate.api_url / calibrate.web_url in workshop.json. A key from
one deployment returns 401 on another, and `check` says so.
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import sys
import time
from pathlib import Path
from typing import Any, Dict, List, Optional

from workshop_config import (
    Config,
    add_config_arg,
    load_config,
    load_env,
    load_evaluators,
    require_env,
    utf8_console,
)

SCALE_KEYS = ("value", "name", "description", "color")
DEFAULT_SCALE = [{"value": True, "name": "Yes"}, {"value": False, "name": "No"}]

BINARY_TEMPLATE = """You are a highly accurate evaluator assessing {subject}.{context}

You will be given a full conversation.{message_format} {focus}

Question: {description}

Answer Yes when: {rubric}

Answer No when that standard is not met. If the conversation gives no occasion for this to apply, answer Yes \
rather than penalising {judged} for something the exchange never called for.

Respond with Yes or No, and a one-sentence reason grounded in the conversation."""

SCALE_TEMPLATE = """You are a highly accurate evaluator assessing {subject}.{context}

You will be given a full conversation.{message_format} {focus}

Question: {description}

Choose exactly one of these answers. The text after each answer's name defines what that answer means for this \
question.{yes_clause}
{options}

Respond with the chosen answer's name exactly as written above, and a one-sentence reason grounded in the conversation."""


# --------------------------------------------------------------------------------------------
# HTTP
# --------------------------------------------------------------------------------------------


class CalibrateError(RuntimeError):
    def __init__(self, message: str, status: Optional[int] = None) -> None:
        super().__init__(message)
        self.status = status


class Client:
    """Thin wrapper over the public REST API (X-API-Key auth)."""

    def __init__(self, api_url: str, api_key: str, mode: str) -> None:
        self.api_url = api_url.rstrip("/")
        self.mode = mode  # "live" | "dry-run" | "offline"
        self.session = None
        if mode != "offline":
            import requests

            self.session = requests.Session()
            self.session.headers.update({"X-API-Key": api_key, "Content-Type": "application/json"})

    def _show(self, method: str, path: str, body: Any) -> None:
        print(f"    would send {method} {path} {preview(body)}")

    def request(self, method: str, path: str, body: Any = None) -> Any:
        if self.mode == "offline" or (self.mode == "dry-run" and method != "GET"):
            self._show(method, path, body)
            return None
        data = json.dumps(body, ensure_ascii=False).encode("utf-8") if body is not None else None
        response = self.session.request(method, f"{self.api_url}{path}", data=data, timeout=120)
        if response.status_code >= 400:
            raise CalibrateError(f"{method} {path} -> HTTP {response.status_code}: {response.text[:400]}", response.status_code)
        return response.json() if response.content else {}

    def get(self, path: str) -> Any:
        return self.request("GET", path)


def preview(body: Any) -> str:
    """A one-line summary of a request body that never includes conversation text."""
    if body is None:
        return ""
    if isinstance(body, dict) and ("items" in body or "updates" in body):
        entries = body.get("items") or body.get("updates") or []
        names = [str((e.get("payload") or {}).get("name")) for e in entries]
        shown = ", ".join(names[:5]) + (", ..." if len(names) > 5 else "")
        verb = "new" if "items" in body else "updated"
        return f"({len(entries)} {verb} conversation(s): {shown}; message text not shown)"
    if isinstance(body, dict) and ("version" in body or "system_prompt" in body):
        version = body.get("version") or body
        scale = (version.get("output_config") or {}).get("scale") or []
        summary = {k: body[k] for k in ("name", "output_type") if k in body}
        summary["options"] = [o.get("name") for o in scale]
        summary["judge_model"] = version.get("judge_model")
        summary["judge_prompt"] = f"{len(version.get('system_prompt', ''))} chars (see --show-prompts)"
        if "make_live" in body:
            summary["make_live"] = body["make_live"]
        return json.dumps(summary, ensure_ascii=False)
    return json.dumps(body, ensure_ascii=False)


def show_prompts(cfg: Config, specs: List[Dict]) -> None:
    """Print each judge prompt in full. Built from workshop.json and evaluators.json only."""
    for spec in specs:
        print(f"\n===== {spec['name']} =====\n{evaluator_prompt(spec, cfg)}")
    print()


def as_list(response: Any) -> List[Dict]:
    if isinstance(response, list):
        return response
    if isinstance(response, dict):
        for key in ("items", "data", "results"):
            if isinstance(response.get(key), list):
                return response[key]
    return []


def auth_hint(cfg: Config, exc: CalibrateError) -> str:
    if exc.status == 401:
        return (
            f"\nThe server at {cfg.get('calibrate.api_url')} rejected the key (401). Keys only work on the "
            "deployment that issued them: check calibrate.api_url in workshop.json (it must be the API host, "
            "not the web address) and that CALIBRATE_API_KEY in .env is current."
        )
    if exc.status == 403:
        return "\nThe key is valid but not allowed to do this (403)."
    return ""


# --------------------------------------------------------------------------------------------
# Evaluators
# --------------------------------------------------------------------------------------------


def evaluator_prompt(spec: Dict, cfg: Config) -> str:
    context = cfg.get("judge.context", "")
    message_format = cfg.get("judge.message_format", "")
    judged = cfg.get("judge.judged", "the agent")
    common = {
        "subject": cfg.get("judge.subject", "a conversation"),
        "context": f" {context}" if context else "",
        "message_format": f" {message_format}" if message_format else "",
        "focus": spec.get("focus") or cfg.get("judge.focus"),
        "description": spec["description"],
        "judged": judged,
    }
    if spec.get("scale"):
        options = "\n".join(
            f"- {o['name']}: {o['description']}" if o.get("description") else f"- {o['name']}" for o in spec["scale"]
        )
        has_yes = any(o["name"].strip().lower() == "yes" for o in spec["scale"])
        yes_clause = f' The "Yes" answer states the standard {judged}\'s response must meet.' if has_yes else ""
        return SCALE_TEMPLATE.format(options=options, yes_clause=yes_clause, **common)
    return BINARY_TEMPLATE.format(rubric=spec.get("rubric", ""), **common)


def scale_of(spec: Dict) -> List[Dict]:
    return [{k: o[k] for k in SCALE_KEYS if k in o} for o in (spec.get("scale") or DEFAULT_SCALE)]


def evaluator_payload(spec: Dict, cfg: Config) -> Dict:
    scale = scale_of(spec)
    output_type = spec.get("output_type") or "binary"
    value_types = {type(o["value"]) for o in scale}
    if output_type == "binary" and value_types != {bool}:
        raise SystemExit(f"{spec['name']}: a binary question's values must be true/false")
    if output_type == "rating" and not value_types <= {int}:
        raise SystemExit(f"{spec['name']}: a rating question's values must be whole numbers (1, 2, 3, ...)")
    return {
        "name": spec["name"],
        "description": spec["description"],
        "evaluator_type": "conversation",
        "data_type": "text",
        "output_type": output_type,
        "version": {
            "judge_model": cfg.get("calibrate.judge_model"),
            "system_prompt": evaluator_prompt(spec, cfg),
            "output_config": {"scale": scale},
        },
    }


def ensure_evaluators(client: Client, cfg: Config, specs: List[Dict]) -> List[str]:
    """Reuse evaluators that already exist by name; create the rest. Returns ids in spec order."""
    existing = {} if client.mode == "offline" else {e.get("name"): e.get("uuid") for e in as_list(client.get("/evaluators"))}
    ids = []
    for spec in specs:
        payload = evaluator_payload(spec, cfg)  # validates even when reusing
        if spec["name"] in existing:
            print(f"  reuse   {spec['name']}")
            ids.append(existing[spec["name"]])
            continue
        print(f"  create  {spec['name']}")
        created = client.request("POST", "/evaluators", payload)
        if created is None:
            ids.append(f"<new:{spec['name']}>")
            continue
        uuid = created.get("uuid") or (created.get("evaluator") or {}).get("uuid")
        if not uuid:
            raise CalibrateError(f"no uuid returned for evaluator {spec['name']}: {created}")
        ids.append(uuid)
    return ids


# --------------------------------------------------------------------------------------------
# Subcommands
# --------------------------------------------------------------------------------------------


def task_ids_path(cfg: Config) -> Path:
    return cfg.path("task.ids_file")


def read_task_uuid(cfg: Config, override: Optional[str], offline: bool = False) -> str:
    if override:
        return override
    path = task_ids_path(cfg)
    if not path.exists() and offline:
        return "<task-uuid>"
    if not path.exists():
        raise SystemExit(f"No task yet: {path} not found. Run `create` first, or pass --task-uuid.")
    return json.loads(path.read_text(encoding="utf-8"))["task_uuid"]


def cmd_check(client: Client, cfg: Config, args) -> int:
    print(f"API:        {client.api_url}")
    print(f"Web:        {cfg.get('calibrate.web_url')}")
    if client.mode == "offline":
        print("Offline: skipped.")
        return 0
    annotators = as_list(client.get("/annotators"))
    tasks = as_list(client.get("/annotation-tasks"))
    evaluators = as_list(client.get("/evaluators"))
    print(f"Key works.  annotators: {len(annotators)}   annotation tasks: {len(tasks)}   evaluators: {len(evaluators)}")
    prefix = cfg.get("workshop.prefix", "")
    if prefix:
        clash = [e.get("name") for e in evaluators if str(e.get("name", "")).startswith(prefix)]
        if clash:
            print(f"Note: {len(clash)} evaluator(s) already use the prefix {prefix!r}; `create` will REUSE them, "
                  "not make new ones. Pick a new prefix for a new workshop.")
    name = cfg.get("task.name")
    if name and any(t.get("name") == name for t in tasks):
        print(f"Note: a task named {name!r} already exists.")
    return 0


def cmd_create(client: Client, cfg: Config, args) -> int:
    items_path = cfg.path("task.items_file")
    if not items_path.exists():
        raise SystemExit(f"Items not found: {items_path}. Run build_items.py first.")
    items = json.loads(items_path.read_text(encoding="utf-8"))
    if args.limit:
        items = items[: args.limit]
    specs = load_evaluators(cfg)
    if args.show_prompts:
        show_prompts(cfg, specs)
    name = cfg.get("task.name")
    if not name:
        raise SystemExit("Set task.name in workshop.json.")
    print(f"Task:        {name}")
    print(f"Items:       {len(items)}   questions: {len(specs)}   judge model: {cfg.get('calibrate.judge_model')}")

    existing_task = None
    if client.mode != "offline":
        existing_task = next((t for t in as_list(client.get("/annotation-tasks")) if t.get("name") == name), None)
    task_uuid = args.task_uuid or (existing_task or {}).get("uuid")
    if existing_task and not (args.task_uuid or args.update):
        raise SystemExit(
            f"A task named {name!r} already exists. Re-run with --update to sync its questions and items, "
            "or change task.name."
        )

    print("\nQuestions (evaluators):")
    evaluator_ids = ensure_evaluators(client, cfg, specs)
    optional_ids = [uid for uid, spec in zip(evaluator_ids, specs) if spec.get("optional")]
    if optional_ids:
        print(f"  optional: {', '.join(s['name'] for s in specs if s.get('optional'))}")

    if not task_uuid:
        created = client.request(
            "POST",
            "/annotation-tasks",
            {"name": name, "type": "conversation", "description": cfg.get("task.description", ""), "evaluator_ids": evaluator_ids},
        )
        task_uuid = (created or {}).get("uuid") or "<new-task>"
        print(f"\nTask created: {task_uuid}" if created else "\nTask: would be created")
    else:
        print(f"\nTask (existing): {task_uuid}")

    # Order + optional flags are applied as one whole set: an id left out of optional_evaluator_ids
    # becomes required again.
    client.request(
        "PUT",
        f"/annotation-tasks/{task_uuid}/evaluators",
        {"evaluator_ids": evaluator_ids, "optional_evaluator_ids": optional_ids},
    )

    print(f"\nItems ({len(items)}):")
    sync_items(client, task_uuid, items, args.batch_size)

    if client.mode != "live":
        print(f"\nNothing was written ({client.mode}).")
        return 0
    task = client.get(f"/annotation-tasks/{task_uuid}")
    web = cfg.get("calibrate.web_url").rstrip("/")
    link = f"{web}/annotation-tasks/{task_uuid}"
    print(f"\nitem_count:  {task.get('item_count')}")
    for ev in sorted(task.get("evaluators", []), key=lambda e: e.get("position", 0)):
        names = " / ".join(o["name"] for o in (ev.get("output_config") or {}).get("scale", []))
        print(f"  {ev.get('position')}. {ev.get('name')}  [{names}]{'  (optional)' if ev.get('is_optional') else ''}")
    print(f"Task page:   {link}")
    path = task_ids_path(cfg)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(
            {"task_name": name, "task_uuid": task_uuid, "task_url": link, "api_url": client.api_url, "evaluator_ids": evaluator_ids},
            indent=2,
        ),
        encoding="utf-8",
    )
    print(f"Saved ids:   {path}")
    return 0


def sync_items(client: Client, task_uuid: str, items: List[Dict], batch_size: int) -> None:
    """Update items already on the task in place (matched by name) and add the rest, so a rebuilt
    items.json can be re-sent without duplicates."""
    existing: Dict[str, str] = {}
    if client.mode != "offline" and not task_uuid.startswith("<"):
        task = client.get(f"/annotation-tasks/{task_uuid}")
        existing = {
            it["payload"]["name"]: it["uuid"]
            for it in task.get("items", [])
            if (it.get("payload") or {}).get("name") and not it.get("deleted_at")
        }
    updates = [{"uuid": existing[it["payload"]["name"]], "payload": it["payload"]} for it in items if it["payload"]["name"] in existing]
    additions = [it for it in items if it["payload"]["name"] not in existing]
    for start in range(0, len(updates), batch_size):
        client.request("PUT", f"/annotation-tasks/{task_uuid}/items", {"updates": updates[start : start + batch_size]})
        time.sleep(0.2)
    for start in range(0, len(additions), batch_size):
        client.request("POST", f"/annotation-tasks/{task_uuid}/items", {"items": additions[start : start + batch_size]})
        time.sleep(0.2)
    print(f"  updated in place: {len(updates)}   added: {len(additions)}")


def annotator_names(cfg: Config, override: Optional[str]) -> List[str]:
    names = [n.strip() for n in (override.split(",") if override else cfg.get("annotators", [])) if str(n).strip()]
    if not names:
        raise SystemExit('No annotators. List them in workshop.json as "annotators": ["asha", "ravi", ...].')
    return names


def cmd_annotators(client: Client, cfg: Config, args) -> int:
    names = annotator_names(cfg, args.annotators)
    existing = {} if client.mode == "offline" else {a["name"].strip().lower(): a["uuid"] for a in as_list(client.get("/annotators"))}
    missing = [n for n in names if n.lower() not in existing]
    print(f"Annotators: {len(names)} listed, {len(names) - len(missing)} already exist, {len(missing)} to create")
    failed = []
    for name in missing:
        try:
            client.request("POST", "/annotators", {"name": name})
            print(f"  create  {name}")
        except CalibrateError as exc:
            failed.append(name)
            print(f"  FAILED  {name}: {exc}")
    if failed:
        print(
            "\nCreate these annotators in the Calibrate web app instead (Annotators page, Add annotator), "
            f"then re-run: {', '.join(failed)}"
        )
        return 1
    return 0


def write_links(cfg: Config, task: Dict, names: List[str]) -> int:
    web = cfg.get("calibrate.web_url").rstrip("/")
    jobs = {str(j.get("annotator_name", "")).strip().lower(): j for j in task.get("jobs", [])}
    rows = []
    for name in names:
        job = jobs.get(name.lower()) or {}
        token = job.get("public_token")
        rows.append(
            {
                "Name": name[:1].upper() + name[1:],
                "Annotation link": f"{web}/annotate-job/{token}" if token else "NOT CREATED",
                "Conversations": job.get("item_count", 0),
                "Completed": job.get("completed_item_count", 0),
                "Status": job.get("status", "no job"),
            }
        )
    out = cfg.dir / "out" / "annotator_links.csv"
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)
    ready = sum(1 for r in rows if r["Annotation link"] != "NOT CREATED")
    print(f"Links ready: {ready}/{len(rows)}   written to {out}")
    print("Each link opens that person's labeling page without a login: share each one only with its owner.")
    return 0 if ready == len(rows) else 1


def cmd_jobs(client: Client, cfg: Config, args) -> int:
    task_uuid = read_task_uuid(cfg, args.task_uuid, client.mode == "offline")
    names = annotator_names(cfg, args.annotators)
    if client.mode == "offline":
        print("Offline: no links file is written (links come from the live task).")
        for name in names:
            client.request(
                "POST",
                f"/annotation-tasks/{task_uuid}/jobs",
                {"annotator_ids": [f"<uuid of {name}>"], "select_all": True,
                 "reasoning_mode": cfg.get("jobs.reasoning_mode"), "comments_enabled": cfg.get("jobs.comments_enabled")},
            )
        return 0
    annotators = {a["name"].strip().lower(): a["uuid"] for a in as_list(client.get("/annotators"))}
    missing = [n for n in names if n.lower() not in annotators]
    if missing:
        raise SystemExit(f"These annotators do not exist yet: {missing}. Run the `annotators` step first.")
    task = client.get(f"/annotation-tasks/{task_uuid}")
    have = {str(j.get("annotator_name", "")).strip().lower() for j in task.get("jobs", [])}
    todo = [n for n in names if n.lower() not in have]
    print(f"Task: {task.get('name')}   items: {task.get('item_count')}   jobs already: {len(have)}   to create: {len(todo)}")
    blocked = False
    for name in todo:
        body = {
            "annotator_ids": [annotators[name.lower()]],
            "select_all": True,
            "reasoning_mode": cfg.get("jobs.reasoning_mode"),
            "comments_enabled": cfg.get("jobs.comments_enabled"),
        }
        try:
            client.request("POST", f"/annotation-tasks/{task_uuid}/jobs", body)
            print(f"  created  {name}")
        except CalibrateError as exc:
            print(f"  FAILED   {name}: {exc}")
            if exc.status in (401, 403):
                blocked = True
                break
    if blocked:
        print(
            "\nThis Calibrate server does not let the API key create labeling jobs. Do it in the web app:\n"
            f"  1. Open {cfg.get('calibrate.web_url').rstrip('/')}/annotation-tasks/{task_uuid}\n"
            "  2. Create a labeling job for each annotator, assigning all items.\n"
            "  3. Run:  python calibrate_workshop.py links --config workshop.json\n"
            "     That reads the links back with the API key and writes out/annotator_links.csv."
        )
        return 3
    if client.mode != "live":
        return 0
    return write_links(cfg, client.get(f"/annotation-tasks/{task_uuid}"), names)


def cmd_links(client: Client, cfg: Config, args) -> int:
    if client.mode == "offline":
        print("Offline: skipped (links are read from the live task).")
        return 0
    task = client.get(f"/annotation-tasks/{read_task_uuid(cfg, args.task_uuid)}")
    names = annotator_names(cfg, args.annotators) if (args.annotators or cfg.get("annotators")) else [
        str(j.get("annotator_name")) for j in task.get("jobs", [])
    ]
    return write_links(cfg, task, names)


def cmd_run_judge(client: Client, cfg: Config, args) -> int:
    task_uuid = read_task_uuid(cfg, args.task_uuid, client.mode == "offline")
    if client.mode == "offline":
        evaluator_ids = ["<evaluator ids from the task>"]
    else:
        task = client.get(f"/annotation-tasks/{task_uuid}")
        evaluator_ids = [e.get("uuid") or e.get("evaluator_id") for e in task.get("evaluators", [])]
    body = {"evaluators": [{"evaluator_id": e} for e in evaluator_ids], "select_all": True}
    try:
        launched = client.request("POST", f"/annotation-tasks/{task_uuid}/evaluator-runs", body)
    except CalibrateError as exc:
        print(f"Could not start the AI judge: {exc}{auth_hint(cfg, exc)}")
        print(
            "Run it from the web app instead: open the task, choose the run-evaluators action, select all "
            "questions and all items."
        )
        return 3
    if not launched:
        return 0
    job = launched.get("job_uuid")
    print(f"AI judge started: {launched.get('evaluator_count')} questions x {launched.get('item_count')} items (run {job})")
    if not args.wait:
        print("Re-run with --wait to follow it, or watch the task page.")
        return 0
    while True:
        time.sleep(10)
        run = client.get(f"/annotation-tasks/{task_uuid}/evaluator-runs/{job}")
        status = run.get("status")
        print(f"  {status}")
        if status in ("completed", "failed"):
            if run.get("error"):
                print(f"  error: {run['error']}")
            return 0 if status == "completed" else 1


def cmd_update_evaluators(client: Client, cfg: Config, args) -> int:
    specs = load_evaluators(cfg)
    if args.show_prompts:
        show_prompts(cfg, specs)
    if client.mode == "offline":
        for spec in specs:
            client.request("POST", f"/evaluators/<uuid of {spec['name']}>/versions",
                           {"judge_model": cfg.get("calibrate.judge_model"), "system_prompt": evaluator_prompt(spec, cfg),
                            "output_config": {"scale": scale_of(spec)}, "make_live": True})
        return 0
    by_name = {e.get("name"): e.get("uuid") for e in as_list(client.get("/evaluators"))}
    published, needs_ui, missing = 0, [], []
    for spec in specs:
        uuid = by_name.get(spec["name"])
        if not uuid:
            missing.append(spec["name"])
            continue
        detail = client.get(f"/evaluators/{uuid}")
        live = next((v for v in detail.get("versions", []) if v.get("uuid") == detail.get("live_version_id")), {}) or {}
        prompt, scale = evaluator_prompt(spec, cfg), scale_of(spec)
        live_scale = [{k: o[k] for k in SCALE_KEYS if o.get(k) is not None} for o in ((live.get("output_config") or {}).get("scale") or [])]
        if detail.get("description") != spec["description"]:
            needs_ui.append(spec["name"])
        if live.get("system_prompt") == prompt and live_scale == scale:
            print(f"  unchanged  {spec['name']}")
            continue
        print(f"  new live version  {spec['name']}")
        created = client.request(
            "POST",
            f"/evaluators/{uuid}/versions",
            {"judge_model": live.get("judge_model") or cfg.get("calibrate.judge_model"), "system_prompt": prompt,
             "output_config": {"scale": scale}, "make_live": True},
        )
        if created:
            print(f"    now v{created.get('version_number', '?')}")
        published += 1
    if missing:
        print(f"\nNot on the server (run `create` first): {', '.join(missing)}")
    if needs_ui:
        print(
            "\nThe question text shown to annotators changed for these. The API key cannot edit it; change it "
            f"in the web app (Evaluators page -> open the evaluator -> edit description): {', '.join(needs_ui)}"
        )
    print(f"\nnew live versions: {published}{f' ({client.mode}: nothing written)' if client.mode != 'live' else ''}")
    return 1 if missing else 0


def cmd_status(client: Client, cfg: Config, args) -> int:
    if client.mode == "offline":
        print("Offline: skipped.")
        return 0
    task = client.get(f"/annotation-tasks/{read_task_uuid(cfg, args.task_uuid)}")
    print(f"Task: {task.get('name')}   items: {task.get('item_count')}   questions: {len(task.get('evaluators', []))}")
    for job in sorted(task.get("jobs", []), key=lambda j: str(j.get("annotator_name", "")).lower()):
        print(f"  {str(job.get('annotator_name')):<16} {job.get('completed_item_count', 0):>3}/{job.get('item_count', 0):<3} {job.get('status')}")
    return 0


COMMANDS = {
    "check": cmd_check,
    "create": cmd_create,
    "annotators": cmd_annotators,
    "jobs": cmd_jobs,
    "links": cmd_links,
    "run-judge": cmd_run_judge,
    "update-evaluators": cmd_update_evaluators,
    "status": cmd_status,
}


def main() -> int:
    utf8_console()
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("command", choices=sorted(COMMANDS))
    add_config_arg(ap)
    ap.add_argument("--dry-run", action="store_true", help="Read from Calibrate but write nothing.")
    ap.add_argument("--offline", action="store_true", help="No network at all; print the requests.")
    ap.add_argument("--task-uuid", default=None, help="Use this task instead of the one in task.ids_file.")
    ap.add_argument("--update", action="store_true", help="create: sync an existing task with the same name.")
    ap.add_argument("--limit", type=int, default=0, help="create: send only the first N items.")
    ap.add_argument("--batch-size", type=int, default=50, help="create: items per request.")
    ap.add_argument("--annotators", default=None, help="Comma-separated names, overriding workshop.json.")
    ap.add_argument("--wait", action="store_true", help="run-judge: poll until the run finishes.")
    ap.add_argument("--show-prompts", action="store_true", help="create/update-evaluators: print each AI judge prompt in full.")
    args = ap.parse_args()

    cfg = load_config(args.config)
    mode = "offline" if args.offline else ("dry-run" if args.dry_run else "live")
    api_key = ""
    if mode != "offline":
        env_file = load_env(cfg.dir)
        api_key = require_env(
            "CALIBRATE_API_KEY",
            "Add CALIBRATE_API_KEY=<key> to the .env file in the workshop folder "
            "(Calibrate web app -> Workspace settings -> API keys).",
        )
        print(f"Key:        ...{api_key[-4:]} (from {env_file.name if env_file else 'environment'})")
    api_url = os.environ.get("CALIBRATE_API_URL") or cfg.get("calibrate.api_url")
    client = Client(api_url, api_key, mode)
    try:
        return COMMANDS[args.command](client, cfg, args)
    except CalibrateError as exc:
        print(f"\nERROR {exc}{auth_hint(cfg, exc)}")
        return 2


if __name__ == "__main__":
    sys.exit(main())
