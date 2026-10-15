"""Describe a conversation export without showing any message text.

Claude uses this instead of opening the CSV, so the conversations never enter the chat. For each
column it prints the type, how many values are empty, and how many distinct values there are.
Short categorical columns (speaker, language, program; at most 15 distinct values, all short)
also list their values, because those are needed to fill in workshop.json. Free-text columns
never do. It then guesses which column plays which role.

    python inspect_export.py data/export.csv
    python inspect_export.py data/export.csv --conversation-col chat_id
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

import polars as pl

from workshop_config import utf8_console

GUESSES = {
    "conversation_id": [r"^chat_?id$", r"^convo_?id$", r"^conversation_?id$", r"thread", r"session", r"ticket"],
    "speaker": [r"^author_?type$", r"^role$", r"^speaker$", r"^sender", r"^author$", r"^from$"],
    "text": [r"^message_?content$", r"^text$", r"^message$", r"^body$", r"^content$"],
    "translation": [r"_en$", r"english", r"translat"],
    "timestamp": [r"^updated_at$", r"^timestamp", r"^created_at$", r"^inserted_at$", r"_at$", r"time", r"date"],
    "order_by": [r"^inserted_at$", r"turn_?index", r"^seq", r"order"],
    "message_id": [r"^message_?id$", r"^msg_?id$"],
    "language": [r"language", r"^lang"],
}
MAX_CATEGORIES = 15
MAX_CATEGORY_LENGTH = 40


def guess(columns: list[str]) -> dict[str, str]:
    out: dict[str, str] = {}
    taken: set[str] = set()
    for role, patterns in GUESSES.items():
        for pattern in patterns:
            hit = next((c for c in columns if c not in taken and re.search(pattern, c, re.IGNORECASE)), None)
            if hit:
                out[role] = hit
                if role not in ("order_by",):
                    taken.add(hit)
                break
    return out


def main() -> int:
    utf8_console()
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("csv", type=Path)
    ap.add_argument("--conversation-col", default=None, help="Column that identifies a conversation.")
    args = ap.parse_args()
    if not args.csv.exists():
        raise SystemExit(f"Not found: {args.csv}")
    if args.csv.suffix.lower() in (".xlsx", ".xls"):
        raise SystemExit("This is an Excel file. Save it as CSV (File > Save as > CSV UTF-8) and point at the CSV.")

    df = pl.read_csv(args.csv, infer_schema_length=0)
    roles = guess(df.columns)
    hidden = {roles.get("text"), roles.get("translation")}
    print(f"File:     {args.csv}  ({args.csv.stat().st_size / 1e6:.1f} MB)")
    print(f"Rows:     {df.height:,}   columns: {df.width}\n")
    print(f"{'column':<34} {'empty':>8} {'distinct':>9}  values (categorical columns only)")
    for col in df.columns:
        series = df[col]
        empty = int((series.fill_null("").str.strip_chars() == "").sum())
        distinct = series.n_unique()
        values = ""
        lengths = series.drop_nulls().str.len_chars()
        if col in hidden:
            values = "(message text; not shown)"
        elif distinct <= MAX_CATEGORIES and (lengths.max() or 0) <= MAX_CATEGORY_LENGTH:
            counts = series.value_counts(sort=True)
            values = ", ".join(f"{v}={n:,}" for v, n in counts.iter_rows())
        elif lengths.len() and (lengths.mean() or 0) > MAX_CATEGORY_LENGTH:
            values = f"(free text, mean {lengths.mean():.0f} chars; not shown)"
        print(f"{col[:34]:<34} {empty:>8,} {distinct:>9,}  {values}")

    conv = args.conversation_col or roles.get("conversation_id")
    print("\nLikely roles (check these before writing workshop.json):")
    for role in GUESSES:
        print(f"  {role:<16} {roles.get(role, '?')}")
    if conv and conv in df.columns:
        sizes = df.group_by(conv).agg(pl.len().alias("n"))["n"]
        print(f"\nConversations ({conv}): {sizes.len():,}   messages each: min {sizes.min()}, "
              f"median {int(sizes.median())}, max {sizes.max()}")
        for threshold in (5, 10, 20):
            print(f"  with {threshold}+ messages: {int((sizes >= threshold).sum()):,}")
    ts = roles.get("timestamp")
    if ts:
        stamps = df[ts].drop_nulls().str.slice(0, 19).sort()
        if stamps.len():
            print(f"\nTime range ({ts}): {stamps[0]}  to  {stamps[-1]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
