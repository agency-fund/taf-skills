"""Turn the sampled (and translated) conversations into Calibrate annotation items.

Offline: reads a CSV, writes a JSON list of items, one per conversation. Safe to re-run and diff.
Prints counts only, never message text.

Each item looks like this (the shape Calibrate's conversation tasks accept):

    {"payload": {"name": <conversation id>,
                 "description": "Conversation ID: 123;\\nMessages: 14;\\n...",
                 "transcript": [{"role": "user" | "assistant",
                                 "content": "*** PATIENT ***\\nType: text\\n\\n[Hindi — original]\\n...",
                                 "created_at": "YYYY-MM-DD HH:MM:SS"}]}}

Why it looks like this (each one cost time to find out):

- Calibrate's transcript view only understands the roles ``user`` and ``assistant``. Any other
  role is stored but the whole conversation renders as a single dash, so the speaker's name goes
  in the message body as ``*** LABEL ***`` instead.
- ``created_at`` must be bare ``YYYY-MM-DD HH:MM:SS``; a time zone suffix or microseconds stop it
  rendering as a time tag. Time zone conversion therefore happens here, and the zone is written
  into the description panel.
- The dashboard builder parses this exact body layout back out of the export, so keep it.

    python build_items.py --config workshop.json
    python build_items.py --config workshop.json --input data/other.csv --limit 3
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Dict, List, Optional
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError

import polars as pl

from workshop_config import Config, add_config_arg, load_config, utf8_console

NA = "NA"
TIME_RE = re.compile(r"^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}$")
# A leaked Python None shows up as a whole field ("Type: None"), a whole line or the whole
# string, never as the English word inside a sentence ("None of the medicines helped").
LEAKED_NONE_RE = re.compile(r"(?:^|: |\n)None(?:$|;|\n| \|)")


def na(value) -> str:
    """Every empty or missing value is shown as NA."""
    if value is None:
        return NA
    text = str(value).strip()
    return text if text else NA


def parse_timestamp(value) -> Optional[datetime]:
    """Accept the common export forms: '2025-09-01 10:22:03.123456 UTC', '2025-09-01T10:22:03Z',
    '2025-09-01 10:22:03+05:30', '2025-09-01 10:22:03'. Naive values are taken as UTC."""
    text = na(value)
    if text == NA:
        return None
    text = text.replace(" UTC", "").replace("T", " ").strip()
    if text.endswith("Z"):
        text = text[:-1] + "+00:00"
    offset = ""
    match = re.search(r"([+-]\d{2}:?\d{2})$", text)
    if match:
        offset = match.group(1)
        text = text[: match.start()].strip()
    if "." in text:
        text = text.split(".", 1)[0]
    try:
        stamp = datetime.strptime(text, "%Y-%m-%d %H:%M:%S")
    except ValueError:
        try:
            stamp = datetime.strptime(text, "%Y-%m-%d %H:%M")
        except ValueError:
            return None
    if offset:
        sign = 1 if offset[0] == "+" else -1
        digits = offset[1:].replace(":", "")
        delta = timedelta(hours=int(digits[:2]), minutes=int(digits[2:]))
        return stamp.replace(tzinfo=timezone(sign * delta))
    return stamp.replace(tzinfo=timezone.utc)


def clean_timestamp(value, tz: Optional[ZoneInfo] = None) -> str:
    """The bare 'YYYY-MM-DD HH:MM:SS' form Calibrate renders as a time tag, in `tz` if given."""
    stamp = parse_timestamp(value)
    if stamp is None:
        return na(value)
    if tz is not None:
        stamp = stamp.astimezone(tz)
    elif stamp.utcoffset() != timedelta(0):
        stamp = stamp.astimezone(timezone.utc)
    return stamp.strftime("%Y-%m-%d %H:%M:%S")


def tz_note(tz: ZoneInfo) -> str:
    """'IST (UTC+05:30)' for the description panel."""
    local = datetime(2026, 1, 1, tzinfo=timezone.utc).astimezone(tz)
    total = int((local.utcoffset() or timedelta(0)).total_seconds())
    sign, total = ("+" if total >= 0 else "-"), abs(total)
    return f"{local.tzname()} (UTC{sign}{total // 3600:02d}:{(total % 3600) // 60:02d})"


def first_non_null(values) -> str:
    for value in values:
        if value is not None and str(value).strip():
            return str(value).strip()
    return NA


def distinct_in_order(values) -> str:
    seen, out = set(), []
    for value in values:
        text = str(value).strip() if value is not None else ""
        if text and text not in seen:
            seen.add(text)
            out.append(text)
    return ", ".join(out) if out else NA


def sort_key(value):
    """Numbers sort as numbers (turn 2 before turn 10), everything else as text."""
    text = "" if value is None else str(value).strip()
    for parse in (int, float):  # int first: long message ids lose precision as floats
        try:
            return (0, parse(text), "")
        except ValueError:
            pass
    return (1, 0, text)


class ItemBuilder:
    def __init__(self, cfg: Config, columns: List[str]) -> None:
        self.cfg = cfg
        self.present = set(columns)
        self.col_id = cfg.column("conversation_id")
        self.col_speaker = cfg.column("speaker")
        self.col_text = cfg.column("text")
        self.col_translation = cfg.column("translation")
        self.col_time = cfg.column("timestamp")
        self.col_order = cfg.column("order_by") or self.col_time
        self.col_msg_id = cfg.column("message_id")
        self.col_language = cfg.column("language")
        self.labels = {str(k).strip().upper(): str(v) for k, v in cfg.get("data.speaker_labels", {}).items()}
        self.assistant = {str(s).strip().upper() for s in cfg.get("data.assistant_speakers", [])}
        self.meta = [m for m in cfg.get("data.message_meta", []) if m.get("column")]
        self.fields = cfg.get("data.description_fields", [])
        self.id_label = cfg.get("data.id_label", "Conversation ID")
        tz_name = cfg.get("data.display_timezone")
        self.tz: Optional[ZoneInfo] = None
        if tz_name:
            try:
                self.tz = ZoneInfo(tz_name)
            except ZoneInfoNotFoundError:
                raise SystemExit(
                    f"Unknown time zone {tz_name!r}. Use an IANA name such as Asia/Kolkata "
                    "(on Windows also run: pip install tzdata)."
                )

    def check_columns(self) -> None:
        required = {
            "conversation_id": self.col_id,
            "speaker": self.col_speaker,
            "text": self.col_text,
            "timestamp": self.col_time,
        }
        missing = [f"{role} -> {col!r}" for role, col in required.items() if not col or col not in self.present]
        if self.col_translation and self.col_translation not in self.present:
            missing.append(f"translation -> {self.col_translation!r} (set it to null if there is no translation)")
        if missing:
            raise SystemExit(
                "These data.columns entries in workshop.json do not match the CSV:\n  "
                + "\n  ".join(missing)
                + "\nRun inspect_export.py on the file to see its column names."
            )

    def speaker(self, row: Dict) -> str:
        raw = (row.get(self.col_speaker) or "").strip()
        return self.labels.get(raw.upper(), raw or NA)

    def role(self, row: Dict) -> str:
        raw = (row.get(self.col_speaker) or "").strip().upper()
        return "assistant" if raw in self.assistant else "user"

    def content(self, row: Dict) -> str:
        """Speaker header, optional tag line, then the original text and its English translation."""
        original = na(row.get(self.col_text))
        parts = [f"*** {self.speaker(row).upper()} ***"]
        if self.meta:
            parts.append(" | ".join(f"{m.get('label') or m['column']}: {na(row.get(m['column']))}" for m in self.meta))
        parts.append("")
        if not self.col_translation:
            parts += ["[Message]", original]
            return "\n".join(parts)
        translated = row.get(self.col_translation)
        if translated is None or not str(translated).strip():
            # Nothing came back from the translator; show the original rather than a blank block.
            translated = f"{original}  ({NA} — no translation available)"
        language = na(row.get(self.col_language)) if self.col_language else NA
        original_label = f"{language.title()} — original" if language != NA else "Original"
        parts += [f"[{original_label}]", original, "", "[English — translation]", str(translated).strip()]
        return "\n".join(parts)

    def description(self, conv_id: str, rows: List[Dict], note: Optional[str], note_label: str) -> str:
        """Top-right panel in Calibrate: conversation-level facts, ';' + newline between entries."""
        entries = [f"{self.id_label}: {na(conv_id)}", f"Messages: {len(rows)}"]
        for field in self.fields:
            column = field.get("column")
            if not column or column not in self.present:
                continue
            label = field.get("label") or column
            values = [r.get(column) for r in rows]
            mode = field.get("mode", "first")
            if mode == "count":
                rendered = str(len({na(v) for v in values} - {NA}))
            elif mode == "distinct":
                rendered = distinct_in_order(values)
            else:
                rendered = first_non_null(values)
            entries.append(f"{label}: {rendered}")
        if self.tz is not None:
            entries.append(f"Time zone: {tz_note(self.tz)}")
        if note is not None and na(note) != NA:
            entries.append(f"{note_label}: {na(note)}")
        return ";\n".join(entries)

    def build(self, df: pl.DataFrame, order: Optional[List[str]], notes: Dict[str, str], note_label: str) -> List[Dict]:
        grouped: Dict[str, List[Dict]] = {}
        for row in df.iter_rows(named=True):
            grouped.setdefault(str(row[self.col_id]).strip(), []).append(row)
        conv_ids = order if order is not None else sorted(grouped)
        missing = [c for c in conv_ids if c not in grouped]
        if missing:
            raise SystemExit(f"{len(missing)} listed conversation id(s) are not in the CSV, e.g. {missing[:3]}")

        items = []
        for conv_id in conv_ids:
            rows = sorted(
                grouped[conv_id],
                key=lambda r: (sort_key(r.get(self.col_order)), sort_key(r.get(self.col_msg_id) if self.col_msg_id else None)),
            )
            transcript = [
                {
                    "role": self.role(r),
                    "content": self.content(r),
                    "created_at": clean_timestamp(r.get(self.col_time), self.tz),
                }
                for r in rows
            ]
            items.append(
                {
                    "payload": {
                        "name": conv_id,
                        "description": self.description(conv_id, rows, notes.get(conv_id), note_label),
                        "transcript": transcript,
                    }
                }
            )
        return items


def validate(items: List[Dict]) -> List[str]:
    problems: List[str] = []
    names = [it["payload"]["name"] for it in items]
    if len(names) != len(set(names)):
        problems.append("duplicate item names")
    for it in items:
        p = it["payload"]
        if not p.get("transcript"):
            problems.append(f"{p['name']}: empty transcript")
        roles = {t.get("role") for t in p.get("transcript", [])}
        if not roles <= {"user", "assistant"}:
            problems.append(f"{p['name']}: roles other than user/assistant: {sorted(roles)}")
        for turn in p.get("transcript", []):
            for key in ("role", "content", "created_at"):
                if not turn.get(key):
                    problems.append(f"{p['name']}: turn missing {key}")
            stamp = turn.get("created_at")
            if stamp and stamp != NA and not TIME_RE.match(stamp):
                problems.append(f"{p['name']}: created_at not 'YYYY-MM-DD HH:MM:SS': {stamp!r}")
            if LEAKED_NONE_RE.search(turn.get("content") or ""):
                problems.append(f"{p['name']}: literal 'None' leaked into a message")
        if LEAKED_NONE_RE.search(p["description"]):
            problems.append(f"{p['name']}: literal 'None' leaked into the description")
    return problems


def read_selection(cfg: Config) -> tuple[Optional[List[str]], Dict[str, str], str]:
    ids_path = cfg.path("sample.ids_file")
    if ids_path is None:
        return None, {}, ""
    if not ids_path.exists():
        raise SystemExit(f"IDs file not found: {ids_path}")
    sel = pl.read_csv(ids_path, infer_schema_length=0)
    sel = sel.rename({c: c.strip() for c in sel.columns})
    id_col = cfg.get("sample.ids_column")
    if id_col not in sel.columns:
        raise SystemExit(f"IDs file has no column {id_col!r}; its columns are {sel.columns}")
    order = [str(v).strip() for v in sel[id_col].to_list() if v is not None and str(v).strip()]
    if len(order) != len(set(order)):
        raise SystemExit("The IDs file lists the same conversation more than once.")
    notes: Dict[str, str] = {}
    note_col = cfg.get("sample.note_column")
    if note_col and note_col in sel.columns:
        notes = {str(c).strip(): (n or "") for c, n in zip(sel[id_col].to_list(), sel[note_col].to_list()) if c is not None}
    return order, notes, cfg.get("sample.note_label", "Note")


def main() -> int:
    utf8_console()
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    add_config_arg(ap)
    ap.add_argument("--input", default=None, help="CSV to read (default: data.translated_file, else data.sample_file).")
    ap.add_argument("--out", default=None, help="Output JSON (default: task.items_file).")
    ap.add_argument("--limit", type=int, default=0, help="Keep only the first N items, for a visual check.")
    args = ap.parse_args()
    cfg = load_config(args.config)

    if args.input:
        input_path = Path(args.input)
    elif cfg.column("translation") and cfg.path("data.translated_file") and cfg.path("data.translated_file").exists():
        input_path = cfg.path("data.translated_file")
    else:
        input_path = cfg.path("data.sample_file")
    if input_path is None or not input_path.exists():
        raise SystemExit(f"Input CSV not found: {input_path}")
    out_path = Path(args.out) if args.out else cfg.path("task.items_file")

    df = pl.read_csv(input_path, infer_schema_length=0)
    builder = ItemBuilder(cfg, df.columns)
    builder.check_columns()

    order, notes, note_label = read_selection(cfg)
    if order is not None:
        df = df.filter(pl.col(builder.col_id).str.strip_chars().is_in(order))
    items = builder.build(df, order, notes, note_label)
    if args.limit and args.limit > 0:
        items = items[: args.limit]

    problems = validate(items)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(items, ensure_ascii=False, indent=2), encoding="utf-8")

    turns = sum(len(it["payload"]["transcript"]) for it in items)
    roles = sorted({t["role"] for it in items for t in it["payload"]["transcript"]})
    labels = sorted({t["content"].split("\n", 1)[0] for it in items for t in it["payload"]["transcript"]})
    print(f"Input:       {input_path}")
    print(f"Items:       {len(items)}   messages: {turns}   roles: {roles}")
    print(f"Speakers:    {', '.join(labels)}")
    print(f"Time zone:   {tz_note(builder.tz) if builder.tz else 'UTC (unchanged)'}")
    print(f"Translation: {'shown under the original' if builder.col_translation else 'none (single language)'}")
    skipped = [f.get("column") for f in builder.fields if f.get("column") and f.get("column") not in builder.present]
    if skipped:
        print(f"Panel:       skipped {len(skipped)} description field(s) not in this CSV: {', '.join(skipped)}")
    if order is not None:
        print(f"Selection:   {len(order)} conversations from {cfg.path('sample.ids_file').name}, in that order")
    print(f"Output:      {out_path}")
    if problems:
        print(f"\n{len(problems)} validation problem(s):")
        for p in problems[:20]:
            print(f"  FAIL {p}")
        return 1
    print("Validation:  PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
