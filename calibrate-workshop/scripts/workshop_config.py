"""Shared helpers for the calibrate-workshop scripts.

Every script takes ``--config path/to/workshop.json``. This module loads that file, fills in
defaults, resolves relative paths against the folder the config lives in, and loads the
``.env`` that holds the API keys (searched from the workshop folder upwards). Nothing here
prints a secret.
"""

from __future__ import annotations

import copy
import json
import os
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional

DEFAULTS: Dict[str, Any] = {
    "workshop": {
        # Shown on the dashboard and its password page when dashboard.title / eyebrow are empty.
        "name": "",
        # Short id for browser storage keys of the dashboard (letters, digits, dashes).
        "slug": "workshop",
        # Prepended to every evaluator name ("NH W5" -> "NH W5 - Empathetic"). Must be new per
        # workshop: evaluators are matched by name, so a reused prefix reuses old evaluators.
        "prefix": "",
    },
    "calibrate": {
        "api_url": "https://api.calibrate.artpark.ai",
        "web_url": "https://calibrate.artpark.ai",
        "judge_model": "openai/gpt-5.4-mini",
    },
    "data": {
        "raw_export": "data/export.csv",
        "sample_file": "data/sample.csv",
        "translated_file": "data/sample_translated.csv",
        "columns": {
            "conversation_id": "conversation_id",
            "speaker": "speaker",
            "text": "text",
            "translation": None,
            "timestamp": "timestamp",
            "order_by": None,
            "message_id": None,
            "language": None,
        },
        # Per-message tags shown on one line above the text: [{"column": ..., "label": ...}].
        "message_meta": [],
        # Raw speaker value -> header annotators see ("OWNER" -> "Patient").
        "speaker_labels": {},
        # Raw speaker values that are the side being judged (nurse, agent, bot).
        "assistant_speakers": [],
        # Raw speaker values removed before sampling (system messages, templates).
        "drop_speakers": [],
        # Keep only these languages (matched against columns.language, case-insensitive).
        "language_filter": [],
        # IANA zone for time tags, e.g. "Asia/Kolkata". Timestamps are read as UTC.
        "display_timezone": None,
        "id_label": "Conversation ID",
        # Conversation-level facts for the description panel:
        # [{"column": ..., "label": ..., "mode": "first" | "distinct" | "count"}]
        "description_fields": [],
    },
    "sample": {
        "n_conversations": 25,
        "min_messages": 0,
        "seed": 42,
        "drop_duplicates": False,
        "require_text": True,
        # Optional sheet of hand-picked conversations (exported to CSV). Item order follows it.
        "ids_file": None,
        "ids_column": "conversation_id",
        "note_column": None,
        "note_label": "Note",
    },
    "translation": {
        "model": "gpt-4.1-mini",
        "context": "chat messages",
        "language_hint": "",
        "batch_size": 25,
        "concurrency": 5,
        "skip_speakers": [],
    },
    "task": {
        "name": "",
        "description": "",
        "evaluators_file": "evaluators.json",
        "items_file": "out/items.json",
        "ids_file": "out/task_ids.json",
    },
    "judge": {
        "subject": "a conversation",
        "context": "",
        "message_format": "",
        "focus": "Judge the responses across the whole conversation.",
        # Who is being judged, used in the prompt wording ("the nurse", "the agent").
        "judged": "the agent",
    },
    "annotators": [],
    "jobs": {"reasoning_mode": "optional", "comments_enabled": True},
    "dashboard": {
        "export_csv": "out/annotations_export.csv",
        "out_html": "out/dashboard.html",
        "title": "",
        "eyebrow": "",
        "rater_names": {},
        "rater_order": [],
        "speaker_acronyms": [],
        "hint_fields": [],
        "fallback_speakers": {"user": "User", "assistant": "Agent"},
        "deploy_dir": "out/site",
        "salt_file": "out/.salt",
    },
}


def utf8_console() -> None:
    """Windows consoles default to a legacy code page; non-ASCII output would crash there."""
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8", errors="replace")
        except Exception:
            pass


def _merge(base: Dict[str, Any], override: Dict[str, Any]) -> Dict[str, Any]:
    out = copy.deepcopy(base)
    for key, value in (override or {}).items():
        if isinstance(value, dict) and isinstance(out.get(key), dict):
            out[key] = _merge(out[key], value)
        else:
            out[key] = value
    return out


class Config:
    def __init__(self, path: Path) -> None:
        self.file = path.resolve()
        self.dir = self.file.parent
        raw = json.loads(self.file.read_text(encoding="utf-8"))
        raw.pop("_comment", None)
        self.data = _merge(DEFAULTS, raw)

    def get(self, dotted: str, default: Any = None) -> Any:
        node: Any = self.data
        for part in dotted.split("."):
            if not isinstance(node, dict) or part not in node:
                return default
            node = node[part]
        return default if node is None else node

    def path(self, dotted: str) -> Optional[Path]:
        """A path setting resolved against the workshop folder (absolute paths kept)."""
        value = self.get(dotted)
        if not value:
            return None
        p = Path(os.path.expanduser(str(value)))
        return p if p.is_absolute() else (self.dir / p)

    def column(self, role: str) -> Optional[str]:
        return self.get(f"data.columns.{role}")

    @property
    def slug(self) -> str:
        return str(self.get("workshop.slug", "workshop"))


def load_config(path: Optional[str]) -> Config:
    candidate = Path(path) if path else Path.cwd() / "workshop.json"
    if not candidate.exists():
        raise SystemExit(
            f"Config not found: {candidate}\n"
            "Copy scripts/workshop.example.json into the workshop folder as workshop.json and fill it in."
        )
    return Config(candidate)


def add_config_arg(parser) -> None:
    parser.add_argument(
        "--config",
        default=None,
        help="Path to workshop.json (default: ./workshop.json).",
    )


def load_env(start: Path) -> Optional[Path]:
    """Load the nearest .env at or above `start`. Values override the shell so a stale exported
    key never silently wins. Returns the file used (never its contents)."""
    for folder in [start, *start.parents]:
        env_path = folder / ".env"
        if env_path.is_file():
            try:
                from dotenv import load_dotenv

                load_dotenv(env_path, override=True)
            except ImportError:
                for line in env_path.read_text(encoding="utf-8").splitlines():
                    line = line.strip()
                    if not line or line.startswith("#") or "=" not in line:
                        continue
                    key, value = line.split("=", 1)
                    os.environ[key.strip()] = value.strip().strip('"').strip("'")
            return env_path
    return None


def require_env(name: str, hint: str) -> str:
    value = os.environ.get(name, "").strip()
    if not value:
        raise SystemExit(f"{name} is not set. {hint}")
    return value


def evaluator_name(spec_name: str, prefix: str) -> str:
    """'Empathetic' + 'NH W5' -> 'NH W5 - Empathetic'; names that already carry the prefix stay."""
    prefix = (prefix or "").strip()
    if not prefix or spec_name.startswith(prefix):
        return spec_name
    return f"{prefix} - {spec_name}"


def load_evaluators(cfg: Config, path: Optional[Path] = None) -> List[Dict[str, Any]]:
    """Evaluator specs with the workshop prefix applied to every name."""
    spec_path = path or cfg.path("task.evaluators_file")
    if spec_path is None or not spec_path.exists():
        raise SystemExit(f"Evaluator spec not found: {spec_path}")
    specs = json.loads(spec_path.read_text(encoding="utf-8"))
    if isinstance(specs, dict):
        specs = specs.get("evaluators", [])
    prefix = cfg.get("workshop.prefix", "")
    out = []
    for spec in specs:
        spec = dict(spec)
        spec["name"] = evaluator_name(spec["name"], prefix)
        out.append(spec)
    names = [s["name"] for s in out]
    if len(names) != len(set(names)):
        raise SystemExit("Two evaluators share a name; names must be unique.")
    return out
