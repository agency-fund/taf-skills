"""Pick the conversations for the workshop from the full export.

Works at the conversation level: a conversation is kept whole or dropped, never cut. Two modes:

- random (default): filter, then draw `sample.n_conversations` at random with `sample.seed`.
- hand-picked: if `sample.ids_file` is set, keep exactly the conversations listed there.

Filters, in order (each prints how many rows/conversations it removed):
  1. language       keep rows whose data.columns.language is in data.language_filter
  2. speakers       drop rows whose speaker is in data.drop_speakers (system messages, templates)
  3. duplicates     sample.drop_duplicates removes rows identical in every column
  4. text present   sample.require_text drops conversations with any empty message
                    (images, audio and stickers carry no text, so annotators would see holes)
  5. length         sample.min_messages keeps conversations with at least N messages

Prints counts only, never message text.

    python make_sample.py --config workshop.json
    python make_sample.py --config workshop.json --n 30 --seed 7
"""

from __future__ import annotations

import argparse
import random
import sys
from pathlib import Path

import polars as pl

from workshop_config import add_config_arg, load_config, utf8_console


def lower_list(values) -> list[str]:
    return [str(v).strip().lower() for v in (values or []) if str(v).strip()]


def main() -> int:
    utf8_console()
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    add_config_arg(ap)
    ap.add_argument("--input", default=None, help="Export CSV (default: data.raw_export).")
    ap.add_argument("--out", default=None, help="Output CSV (default: data.sample_file).")
    ap.add_argument("--n", type=int, default=None, help="Override sample.n_conversations (0 = keep all eligible).")
    ap.add_argument("--seed", type=int, default=None, help="Override sample.seed.")
    args = ap.parse_args()
    cfg = load_config(args.config)

    input_path = Path(args.input) if args.input else cfg.path("data.raw_export")
    out_path = Path(args.out) if args.out else cfg.path("data.sample_file")
    if input_path is None or not input_path.exists():
        raise SystemExit(f"Export not found: {input_path}")
    n_target = cfg.get("sample.n_conversations", 25) if args.n is None else args.n
    seed = cfg.get("sample.seed", 42) if args.seed is None else args.seed

    conv, speaker, text, lang = (cfg.column(r) for r in ("conversation_id", "speaker", "text", "language"))
    # Every column as text: long numeric ids survive the round trip unchanged.
    df = pl.read_csv(input_path, infer_schema_length=0)
    for role, col in (("conversation_id", conv), ("text", text)):
        if not col or col not in df.columns:
            raise SystemExit(f"data.columns.{role} = {col!r} is not a column of {input_path.name}. Run inspect_export.py.")

    def report(step: str) -> None:
        print(f"{step:<18} rows {df.height:>8,}   conversations {df[conv].n_unique():>6,}")

    print(f"Input:             {input_path}")
    report("Start")

    languages = lower_list(cfg.get("data.language_filter"))
    if languages:
        if not lang or lang not in df.columns:
            raise SystemExit("data.language_filter is set but data.columns.language is not a column.")
        df = df.filter(pl.col(lang).fill_null("").str.strip_chars().str.to_lowercase().is_in(languages))
        report(f"Language {','.join(languages)}")

    drop = lower_list(cfg.get("data.drop_speakers"))
    if drop and speaker in df.columns:
        df = df.filter(~pl.col(speaker).fill_null("").str.strip_chars().str.to_lowercase().is_in(drop))
        report(f"Drop {','.join(d.upper() for d in drop)}")

    n_dup = df.height - df.unique().height
    if cfg.get("sample.drop_duplicates"):
        df = df.unique(maintain_order=True)
        report(f"Duplicates (-{n_dup})")
    elif n_dup:
        print(f"Note: {n_dup:,} rows are exact duplicates (kept; set sample.drop_duplicates to remove them)")

    blank = pl.col(text).fill_null("").str.strip_chars() == ""
    if cfg.get("sample.require_text", True):
        complete = df.group_by(conv).agg(blank.sum().alias("n_blank")).filter(pl.col("n_blank") == 0)[conv]
        df = df.filter(pl.col(conv).is_in(complete.to_list()))
        report("Text in every msg")

    min_messages = cfg.get("sample.min_messages", 0) or 0
    if min_messages > 0:
        long_enough = df.group_by(conv).agg(pl.len().alias("n")).filter(pl.col("n") >= min_messages)[conv]
        df = df.filter(pl.col(conv).is_in(long_enough.to_list()))
        report(f">= {min_messages} messages")

    if df.height == 0:
        raise SystemExit("No conversations left after filtering. Loosen a filter in workshop.json.")

    ids_path = cfg.path("sample.ids_file")
    if ids_path is not None:
        sel = pl.read_csv(ids_path, infer_schema_length=0)
        sel = sel.rename({c: c.strip() for c in sel.columns})
        id_col = cfg.get("sample.ids_column")
        if id_col not in sel.columns:
            raise SystemExit(f"{ids_path.name} has no column {id_col!r}; its columns are {sel.columns}")
        wanted = [str(v).strip() for v in sel[id_col].to_list() if v is not None and str(v).strip()]
        available = set(df[conv].cast(pl.Utf8).str.strip_chars().to_list())
        missing = [w for w in wanted if w not in available]
        if missing:
            print(f"WARNING: {len(missing)} hand-picked conversation(s) were removed by the filters or are not in "
                  f"the export, e.g. {missing[:3]}")
        df = df.filter(pl.col(conv).str.strip_chars().is_in(wanted))
        report(f"Hand-picked ({ids_path.name})")
    else:
        ids = sorted(df[conv].unique().to_list())  # sorted first so the seed is reproducible
        print(f"Eligible:          {len(ids):,} conversations")
        if n_target and n_target > 0:
            if n_target > len(ids):
                raise SystemExit(f"Asked for {n_target} conversations but only {len(ids)} are eligible.")
            picked = random.Random(seed).sample(ids, n_target)
            df = df.filter(pl.col(conv).is_in(picked))
            report(f"Random {n_target} (seed {seed})")

    sort_cols = [c for c in (conv, cfg.column("order_by") or cfg.column("timestamp")) if c and c in df.columns]
    if sort_cols:
        df = df.sort(sort_cols)
    sizes = df.group_by(conv).agg(pl.len().alias("n"))["n"]
    print(f"Messages per conversation: min {sizes.min()}, median {int(sizes.median())}, max {sizes.max()}")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    df.write_csv(out_path)
    print(f"Output:            {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
