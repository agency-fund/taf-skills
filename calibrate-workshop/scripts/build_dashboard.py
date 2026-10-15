"""Build the rater-agreement dashboard from the annotation export you downloaded from Calibrate.

Input: the items CSV from the task page (one row per conversation) plus the workshop's evaluator
spec. Output: one self-contained HTML file that works offline. The agreement maths (majority,
who disagrees, pairwise agreement, Krippendorff's alpha) runs in the page, so the toggles used in
the discussion recompute instantly.

The export's columns:
    name, description, conversation_history          the item as uploaded
    <rater>_<Evaluator_Name>/value, /reasoning        one pair per human rater and question
    <rater>/comment                                   the rater's note on the whole conversation
    evaluator_<Evaluator_Name>_v<N>/value, /reasoning the AI judge (only if it was run)
Spaces in evaluator names become underscores. Humans are stored as the option's value (1, 2,
true); the AI as the option's name ("Yes"); both are mapped back to names via the spec.

Prints counts only. The HTML embeds the conversations, so treat it like the raw data.

    python build_dashboard.py --config workshop.json
    python build_dashboard.py --config workshop.json --csv ~/Downloads/My_Task-items.csv
"""

from __future__ import annotations

import argparse
import html
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

import polars as pl

from workshop_config import Config, add_config_arg, load_config, load_evaluators, utf8_console

HERE = Path(__file__).resolve().parent
FALLBACK_COLORS = ["#16a34a", "#dc2626", "#ca8a04", "#6b7280", "#2563eb", "#9333ea", "#0891b2"]

# Mirrors the message body build_items.py writes. The tag line and the translation block are optional.
MESSAGE_RE = re.compile(
    r"^\*\*\* (?P<speaker>[^*]+?) \*\*\*\n"
    r"(?:(?P<meta>[^\n]+)\n)?\n"
    r"\[(?P<orig_label>[^\]]+)\]\n(?P<original>.*?)"
    r"(?:\n\n\[(?P<en_label>[^\]]+)\]\n(?P<translation>.*))?$",
    re.DOTALL,
)


def short_question_name(name: str) -> str:
    """'NH W4 - Easy to understand' -> 'Easy to understand'."""
    return name.split(" - ", 1)[1] if " - " in name else name


def column_key(name: str) -> str:
    return name.replace(" ", "_")


def parse_pairs(text: str, sep: str) -> list[dict]:
    out = []
    for entry in (text or "").split(sep):
        entry = entry.strip().rstrip(";")
        label, _, value = entry.partition(":")
        if label.strip():
            out.append({"label": label.strip(), "value": value.strip()})
    return out


class Builder:
    def __init__(self, cfg: Config) -> None:
        self.cfg = cfg
        self.acronyms = set(cfg.get("dashboard.speaker_acronyms", []))
        self.fallback = cfg.get("dashboard.fallback_speakers", {})

    def speaker(self, raw: str) -> str:
        text = raw.strip()
        return text if text in self.acronyms else text.title()

    def transcript(self, raw: str) -> list[dict]:
        out = []
        for m in json.loads(raw):
            content = m.get("content") or ""
            match = MESSAGE_RE.match(content)
            if match:
                translated = match.group("en_label") is not None
                out.append(
                    {
                        "role": m.get("role"),
                        "speaker": self.speaker(match.group("speaker")),
                        "meta": parse_pairs(match.group("meta") or "", "|"),
                        "original_label": match.group("orig_label") if translated else None,
                        "original": match.group("original").strip() if translated else None,
                        "translation_label": match.group("en_label") if translated else match.group("orig_label"),
                        "translation": (match.group("translation") if translated else match.group("original")).strip(),
                        "time": m.get("created_at"),
                    }
                )
            else:
                out.append(
                    {
                        "role": m.get("role"),
                        "speaker": self.fallback.get(m.get("role"), str(m.get("role")).title()),
                        "meta": [],
                        "original_label": None,
                        "original": None,
                        "translation_label": "Message",
                        "translation": content,
                        "time": m.get("created_at"),
                    }
                )
        return out


def label_lookup(spec: dict) -> dict:
    lookup = {}
    for option in spec["scale"]:
        for key in (option["value"], str(option["value"]), option["name"], option["name"].lower()):
            lookup[key] = option["name"]
    return lookup


def clean(value) -> str | None:
    if value is None:
        return None
    text = str(value).strip()
    return text or None


def build(cfg: Config, csv_path: Path, specs: list[dict], task: dict) -> dict:
    df = pl.read_csv(csv_path, infer_schema_length=10000)
    for col in ("name", "conversation_history"):
        if col not in df.columns:
            raise SystemExit(f"{csv_path.name} has no {col!r} column. Is this the items export from the task page?")
    for spec in specs:
        spec.setdefault("scale", [{"value": True, "name": "Yes"}, {"value": False, "name": "No"}])
        for i, option in enumerate(spec["scale"]):
            option.setdefault("color", FALLBACK_COLORS[i % len(FALLBACK_COLORS)])

    # Human columns are <rater>_<evaluator key>/value: strip a known key to find the rater.
    value_cols = [c for c in df.columns if c.endswith("/value")]
    suffixes = sorted(("_" + column_key(s["name"]) for s in specs), key=len, reverse=True)
    human_keys = []
    unmatched = []
    for col in value_cols:
        prefix = col[: -len("/value")]
        if prefix.startswith("evaluator_"):
            continue
        suffix = next((s for s in suffixes if prefix.endswith(s)), None)
        if suffix is None:
            unmatched.append(col)
            continue
        rater = prefix[: -len(suffix)]
        if rater not in human_keys:
            human_keys.append(rater)
    if unmatched:
        print(f"WARNING: {len(unmatched)} rating column(s) match no question in the spec (ignored), e.g. {unmatched[:2]}."
              " Is the spec the one this task used (same names, same prefix)?")
    if not human_keys:
        raise SystemExit("No human rating columns found. Check that the evaluator names in the spec match the task.")
    order = [k.lower() for k in cfg.get("dashboard.rater_order", [])]
    human_keys.sort(key=lambda k: (order.index(k.lower()) if k.lower() in order else len(order), k.lower()))

    # AI judge columns: evaluator_<key>_v<N>; keep the newest version when it was run more than once.
    ai_cols: dict[str, str | None] = {}
    versions = set()
    for spec in specs:
        key = column_key(spec["name"])
        found = []
        for col in value_cols:
            m = re.match(rf"^evaluator_{re.escape(key)}_v(\d+)/value$", col)
            if m:
                found.append((int(m.group(1)), col[: -len("/value")]))
        if found:
            version, base = max(found)
            ai_cols[spec["name"]] = base
            versions.add(f"v{version}")
        else:
            ai_cols[spec["name"]] = None
    ai_name = "AI evaluator" + (f" ({', '.join(sorted(versions))})" if versions else " (not run)")

    names = {str(k).lower(): v for k, v in cfg.get("dashboard.rater_names", {}).items()}
    raters = [{"key": k, "name": names.get(k.lower(), k[:1].upper() + k[1:]), "kind": "human"} for k in human_keys]
    raters.append({"key": "ai", "name": ai_name, "short": "AI", "kind": "ai"})
    for r in raters:
        r.setdefault("short", r["name"])

    questions = [
        {
            "key": column_key(s["name"]),
            "name": s["name"],
            "short": short_question_name(s["name"]),
            "description": s.get("description", ""),
            "rubric": s.get("rubric", ""),
            "focus": s.get("focus", ""),
            "binary": s.get("output_type") == "binary",
            "optional": bool(s.get("optional", False)),
            "scale": [{"name": o["name"], "color": o["color"], "description": o.get("description", "")} for o in s["scale"]],
        }
        for s in specs
    ]

    builder = Builder(cfg)
    unknown = []
    conversations = []
    for idx, row in enumerate(df.iter_rows(named=True), start=1):
        ratings = {}
        for spec, q in zip(specs, questions):
            lookup = label_lookup(spec)
            per = {}
            for rk in human_keys:
                base = f"{rk}_{q['key']}"
                value = row.get(f"{base}/value")
                label = None
                if value is not None:
                    label = lookup.get(value)
                    if label is None:
                        unknown.append((idx, q["short"], rk, value))
                        label = str(value)
                per[rk] = {"label": label, "reasoning": clean(row.get(f"{base}/reasoning"))}
            ai_base = ai_cols[spec["name"]]
            value = row.get(f"{ai_base}/value") if ai_base else None
            label = None
            if value is not None:
                label = lookup.get(value) or lookup.get(str(value).strip().lower())
                if label is None:
                    unknown.append((idx, q["short"], "ai", value))
                    label = str(value)
            per["ai"] = {"label": label, "reasoning": clean(row.get(f"{ai_base}/reasoning")) if ai_base else None}
            ratings[q["key"]] = per
        comments = {rk: clean(row.get(f"{rk}/comment")) for rk in human_keys}
        conversations.append(
            {
                "idx": idx,
                "id": str(row["name"]),
                "description": parse_pairs(row.get("description") or "", ";\n"),
                "transcript": builder.transcript(row["conversation_history"]),
                "ratings": ratings,
                "comments": {k: v for k, v in comments.items() if v},
            }
        )
    if unknown:
        print(f"WARNING: {len(unknown)} answers did not match any option in the spec (shown as-is), e.g.:")
        for item in unknown[:5]:
            print("   conversation", item[0], "|", item[1], "|", item[2], "|", repr(item[3]))

    title = cfg.get("dashboard.title") or f"{cfg.get('workshop.name') or 'Workshop'} Agreement Review"
    return {
        "meta": {
            "title": title,
            "task_name": task.get("task_name") or cfg.get("task.name") or title,
            "task_url": task.get("task_url"),
            "source_file": csv_path.name,
            "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC"),
            "n_conversations": len(conversations),
            "storage_key": f"{cfg.slug}-review",
            "hint_fields": cfg.get("dashboard.hint_fields", []),
            "id_label": cfg.get("data.id_label", "Conversation ID"),
        },
        "raters": raters,
        "questions": questions,
        "conversations": conversations,
    }


def main() -> int:
    utf8_console()
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    add_config_arg(ap)
    ap.add_argument("--csv", type=Path, default=None, help="Default: dashboard.export_csv.")
    ap.add_argument("--out", type=Path, default=None, help="Default: dashboard.out_html.")
    ap.add_argument("--template", type=Path, default=HERE / "dashboard_template.html")
    args = ap.parse_args()
    cfg = load_config(args.config)

    csv_path = args.csv or cfg.path("dashboard.export_csv")
    if csv_path is None or not csv_path.exists():
        raise SystemExit(
            f"Export not found: {csv_path}\nDownload it from the task page in Calibrate and save it there "
            "(or pass --csv)."
        )
    out = args.out or cfg.path("dashboard.out_html")
    ids_path = cfg.path("task.ids_file")
    task = json.loads(ids_path.read_text(encoding="utf-8")) if ids_path and ids_path.exists() else {}

    data = build(cfg, csv_path, load_evaluators(cfg), task)
    payload = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
    template = args.template.read_text(encoding="utf-8")
    if "/*__DATA__*/" not in template:
        raise SystemExit("template is missing the /*__DATA__*/ placeholder")
    page = template.replace("__TITLE__", html.escape(data["meta"]["title"])).replace("/*__DATA__*/", payload)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(page, encoding="utf-8")

    humans = [r for r in data["raters"] if r["kind"] == "human"]
    n_msgs = sum(len(c["transcript"]) for c in data["conversations"])
    print(f"Conversations: {data['meta']['n_conversations']}   messages: {n_msgs}   questions: {len(data['questions'])}")
    print(f"Human raters:  {len(humans)} ({', '.join(r['name'] for r in humans)})   AI: {data['raters'][-1]['name']}")
    print(f"Wrote {out} ({len(page) / 1024:.0f} KB). It contains the conversations: keep it out of git and public places.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
