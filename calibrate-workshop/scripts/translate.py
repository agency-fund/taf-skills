"""Add an English translation column to the sampled conversations with the OpenAI API.

This SENDS MESSAGE TEXT TO OPENAI. Run it only after the data owner has agreed that is allowed
for this data; the script refuses to call the API without --confirm-send.

Routine (each step is cheap to repeat):
    python translate.py --config workshop.json --limit 20 --confirm-send   # small paid trial
    python translate.py --config workshop.json --resume --confirm-send     # the rest
    python translate.py --config workshop.json --verify                    # no API call; must print PASS

Messages are sent in batches of `translation.batch_size`, grouped by the language column when
there is one, `translation.concurrency` at a time. Progress is saved to a checkpoint after every
batch, so --resume picks up where a failed or interrupted run stopped. The translation column
(data.columns.translation) is placed right after the original text column.
"""

from __future__ import annotations

import argparse
import asyncio
import json

import random
import sys
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import polars as pl

from workshop_config import add_config_arg, load_config, load_env, require_env, utf8_console


class CountMismatch(ValueError):
    pass


def blank(value) -> bool:
    return value is None or str(value).strip() == ""


def is_quota_error(exc: Exception) -> bool:
    text = str(exc)
    return "insufficient_quota" in text or "exceeded your current quota" in text


def extract_json_array(text: str) -> List:
    try:
        parsed = json.loads(text)
        if isinstance(parsed, list):
            return parsed
    except json.JSONDecodeError:
        pass
    start, end = text.find("["), text.rfind("]")
    if start == -1 or end <= start:
        raise ValueError("no JSON array in the response")
    return json.loads(text[start : end + 1])


def build_prompt(texts: List[str], language: Optional[str], context: str, hint: str) -> str:
    source = language.strip().title() if language else "the source language"
    if hint:
        source = f"{source} ({hint})"
    return (
        f"You are translating {context}. The messages below are written in {source}. "
        "They may appear in the native script, in romanized Latin script, or as a mix of both, and "
        "some may already be partly in English - translate all of them into natural English.\n"
        "Rules:\n"
        "- Keep emoji, numerals, dates and measurements exactly as they appear.\n"
        "- Do not add explanations, notes, transliterations or commentary.\n"
        "- If an item cannot be translated, return an empty string for it.\n"
        "- Return ONLY a JSON array of strings, same length and same order as the input, with no extra text.\n\n"
        + json.dumps(texts, ensure_ascii=False)
    )


async def translate_batch(client, texts: List[str], language: Optional[str], opts: Dict) -> List[str]:
    prompt = build_prompt(texts, language, opts["context"], opts["hint"])
    for attempt in range(opts["retries"]):
        try:
            response = await client.responses.create(model=opts["model"], input=prompt)
            content = getattr(response, "output_text", None) or response.output[0].content[0].text
            out = extract_json_array(content)
            if len(out) != len(texts):
                if len(texts) == 1 and out:
                    return [" ".join(str(x) for x in out if x)]
                raise CountMismatch(f"expected {len(texts)} translations, got {len(out)}")
            return ["" if x is None else str(x) for x in out]
        except CountMismatch:
            if len(texts) > 1:  # split the batch and try each half
                mid = len(texts) // 2
                return await translate_batch(client, texts[:mid], language, opts) + await translate_batch(
                    client, texts[mid:], language, opts
                )
            if attempt == opts["retries"] - 1:
                raise
        except Exception as exc:
            if is_quota_error(exc) or attempt == opts["retries"] - 1:
                raise
            print(f"  retrying after error: {str(exc)[:120]}", file=sys.stderr)
        await asyncio.sleep(2**attempt + random.random())
    return [""] * len(texts)


def with_translation(df: pl.DataFrame, values: List[Optional[str]], text_col: str, out_col: str) -> pl.DataFrame:
    out = df.with_columns(pl.Series(out_col, values, dtype=pl.Utf8))
    order = []
    for col in out.columns:
        if col == out_col:
            continue
        order.append(col)
        if col == text_col:
            order.append(out_col)
    return out.select(order if out_col in order else order + [out_col])


def verify(df: pl.DataFrame, out_path: Path, text_col: str, out_col: str, skip: List[bool], id_cols: List[str],
           adjacent: bool = True) -> int:
    if not out_path.exists():
        print(f"FAIL  output not found: {out_path}")
        return 1
    out = pl.read_csv(out_path, infer_schema_length=0)
    problems = []
    if out.height != df.height:
        problems.append(f"row count {out.height} != input {df.height}")
    if out_col not in out.columns:
        problems.append(f"missing column {out_col!r}")
    elif adjacent and text_col in out.columns and out.columns.index(out_col) != out.columns.index(text_col) + 1:
        problems.append(f"{out_col!r} is not right after {text_col!r}")
    for col in id_cols:
        if col in df.columns and col in out.columns and out.height == df.height and df[col].to_list() != out[col].to_list():
            problems.append(f"column {col!r} changed between input and output")
    if out_col in out.columns and out.height == df.height:
        texts, outs = df[text_col].to_list(), out[out_col].to_list()
        missing = sum(1 for i, t in enumerate(texts) if not blank(t) and not skip[i] and blank(outs[i]))
        if missing:
            problems.append(f"{missing} rows should be translated but are empty (re-run with --resume)")
    for p in problems:
        print(f"FAIL  {p}")
    if not problems:
        print(f"PASS  {out.height:,} rows in {out_path.name} are complete and match the input.")
    return 1 if problems else 0


def main() -> int:
    utf8_console()
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    add_config_arg(ap)
    ap.add_argument("--input", default=None, help="Default: data.sample_file.")
    ap.add_argument("--out", default=None, help="Default: data.translated_file.")
    ap.add_argument("--limit", type=int, default=0, help="Translate at most N pending messages (a cheap trial).")
    ap.add_argument("--resume", action="store_true", help="Continue from the checkpoint or existing output.")
    ap.add_argument("--verify", action="store_true", help="Check the output for completeness; no API call.")
    ap.add_argument("--confirm-send", action="store_true", help="Required to send text to OpenAI.")
    args = ap.parse_args()
    cfg = load_config(args.config)

    in_path = Path(args.input) if args.input else cfg.path("data.sample_file")
    out_path = Path(args.out) if args.out else cfg.path("data.translated_file")
    text_col, out_col = cfg.column("text"), cfg.column("translation")
    lang_col, speaker_col = cfg.column("language"), cfg.column("speaker")
    if not out_col:
        raise SystemExit("Set data.columns.translation (for example \"text_en\") to name the new column.")
    if in_path is None or not in_path.exists():
        raise SystemExit(f"Input not found: {in_path}")
    df = pl.read_csv(in_path, infer_schema_length=0)
    if text_col not in df.columns:
        raise SystemExit(f"Text column {text_col!r} not in {in_path.name}")
    already = out_col in df.columns

    skip_speakers = {s.strip().lower() for s in cfg.get("translation.skip_speakers", [])}
    speakers = df[speaker_col].to_list() if speaker_col in df.columns else [None] * df.height
    skip = [bool(s) and str(s).strip().lower() in skip_speakers for s in speakers]
    id_cols = [c for c in (cfg.column("conversation_id"), cfg.column("message_id")) if c]
    if already:
        # The export came with its translation (e.g. Noora Bangladesh): nothing to send, only check it.
        print(f"{in_path.name} already has a {out_col!r} column, so there is nothing to translate.")
        return verify(df, in_path, text_col, out_col, skip, id_cols, adjacent=False)
    if args.verify:
        return verify(df, out_path, text_col, out_col, skip, id_cols)

    texts = df[text_col].to_list()
    languages = df[lang_col].to_list() if lang_col and lang_col in df.columns else [None] * df.height
    checkpoint = out_path.with_suffix(".checkpoint.csv")
    done: List[Optional[str]] = [None] * df.height
    if args.resume:
        for source in (checkpoint, out_path):
            if source.exists():
                prev = pl.read_csv(source, infer_schema_length=0)
                if prev.height == df.height and out_col in prev.columns:
                    done = prev[out_col].to_list()
                    print(f"Resuming from {source.name}")
                    break
    pending = [(i, texts[i], languages[i]) for i in range(df.height) if not skip[i] and not blank(texts[i]) and blank(done[i])]
    if args.limit:
        pending = pending[: args.limit]
    model = cfg.get("translation.model")
    print(f"Input:        {in_path}   rows {df.height:,}")
    print(f"To translate: {len(pending):,} messages with {model}")
    if not pending:
        with_translation(df, done, text_col, out_col).write_csv(out_path)
        print(f"Nothing pending. Output: {out_path}")
        return 0
    if not args.confirm_send:
        print(
            "\nStopped before sending anything. This step sends message text to OpenAI. Once the data owner "
            "has agreed, re-run with --confirm-send."
        )
        return 4

    load_env(cfg.dir)
    require_env("OPENAI_API_KEY", "Add OPENAI_API_KEY=<key> to the .env file in the workshop folder.")
    from openai import AsyncOpenAI

    groups: Dict[str, List[Tuple[int, str]]] = {}
    for i, text, language in pending:
        groups.setdefault((language or "").strip().lower(), []).append((i, text))
    size = int(cfg.get("translation.batch_size", 25))
    batches = [(lang or None, items[k : k + size]) for lang, items in sorted(groups.items()) for k in range(0, len(items), size)]
    opts = {"model": model, "context": cfg.get("translation.context"), "hint": cfg.get("translation.language_hint", ""), "retries": 5}

    async def run() -> None:
        client = AsyncOpenAI(timeout=120, max_retries=0)
        gate = asyncio.Semaphore(int(cfg.get("translation.concurrency", 5)))
        lock = asyncio.Lock()
        finished = 0

        async def work(language, items):
            nonlocal finished
            async with gate:
                result = await translate_batch(client, [t for _, t in items], language, opts)
            async with lock:
                for (i, _), translation in zip(items, result):
                    done[i] = translation
                tmp = checkpoint.with_suffix(".tmp")
                with_translation(df, done, text_col, out_col).write_csv(tmp)
                tmp.replace(checkpoint)
                finished += 1
                print(f"  batch {finished}/{len(batches)} done", file=sys.stderr)

        await asyncio.gather(*(work(lang, items) for lang, items in batches))

    try:
        asyncio.run(run())
    except Exception as exc:
        if is_quota_error(exc):
            print("\nThe OpenAI account is out of credit. Add credit, then re-run with --resume --confirm-send.")
            return 2
        print(f"\nStopped: {exc}\nProgress is saved; re-run with --resume --confirm-send.")
        return 1
    with_translation(df, done, text_col, out_col).write_csv(out_path)
    left = sum(1 for i in range(df.height) if not skip[i] and not blank(texts[i]) and blank(done[i]))
    print(f"Output:       {out_path}   still untranslated: {left}")
    print("Next: --verify" if not left else "Next: re-run with --resume --confirm-send for the rest")
    return 0


if __name__ == "__main__":
    sys.exit(main())
