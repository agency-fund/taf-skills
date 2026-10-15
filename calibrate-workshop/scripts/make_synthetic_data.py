"""Make fake data for a practice run (no real conversations involved).

Run from the workshop folder:

    # 1. a fake export shaped like Noora's India RES data. Also writes
    #    data/export_with_translation.csv, the same rows with an English column.
    python <skill>/scripts/make_synthetic_data.py export --out data/export.csv --conversations 100

    # 2. after build_items.py: a fake Calibrate annotation export for the dashboard
    #    (written to dashboard.export_csv)
    python <skill>/scripts/make_synthetic_data.py annotations --config workshop.json --raters asha,ravi,meena

Use these to rehearse the whole pipeline, test a changed rubric, or show the dashboard to someone
without exposing anyone's messages. Every message is invented and repetitive by design.
"""

from __future__ import annotations

import argparse
import json
import random
import sys
import uuid
from datetime import datetime, timedelta
from pathlib import Path

import polars as pl

from workshop_config import add_config_arg, load_config, load_evaluators, utf8_console

USER_LINES = [
    ("नमस्ते, मुझे एक सवाल पूछना है।", "Hello, I want to ask a question."),
    ("मेरी अगली जांच कब है?", "When is my next check-up?"),
    ("क्या यह सामान्य है?", "Is this normal?"),
    ("धन्यवाद, समझ गई।", "Thank you, I understood."),
    ("कृपया बताएं क्या खाना चाहिए।", "Please tell me what I should eat."),
    ("ठीक है।", "Okay."),
]
AGENT_LINES = [
    ("नमस्ते! बताइए, मैं आपकी कैसे मदद कर सकती हूँ?", "Hello! Tell me, how can I help you?"),
    ("कृपया अपने नजदीकी स्वास्थ्य केंद्र पर जांच करवाएं।", "Please get a check-up at your nearest health centre."),
    ("यह आम बात है, पर ध्यान रखें।", "This is common, but please take care."),
    ("दिन में तीन बार पौष्टिक भोजन लें।", "Eat nutritious food three times a day."),
    ("और कोई सवाल हो तो पूछिए।", "Ask if you have any other questions."),
]
STATES = ["Uttar Pradesh", "Madhya Pradesh", "Punjab", "Karnataka"]
AREAS = ["ANC", "PNC", "Newborn care"]


def cmd_export(args) -> int:
    rng = random.Random(args.seed)
    start = datetime(2026, 3, 1, 4, 30)
    rows = []
    for c in range(args.conversations):
        chat_id = str(910000 + c)
        lang = "hindi" if rng.random() < 0.85 else "bengali"
        state, area = rng.choice(STATES), rng.choice(AREAS)
        t = start + timedelta(days=rng.randint(0, 60), minutes=rng.randint(0, 600))
        n = rng.randint(6, 20)
        tickets = [str(uuid.UUID(int=rng.getrandbits(128))) for _ in range(rng.randint(1, 3))]
        if rng.random() < 0.1:
            rows.append(dict(chat_id=chat_id, author_type="SYSTEM", message_type="template", text="स्वागत है", en="Welcome",
                             t=t, lang=lang, state=state, area=area, medical="FALSE", emergency="FALSE", ticket=tickets[0]))
        for k in range(n):
            owner = k % 2 == 0
            original, english = rng.choice(USER_LINES if owner else AGENT_LINES)
            image = owner and rng.random() < 0.04
            t = t + timedelta(minutes=rng.randint(1, 90))
            rows.append(dict(chat_id=chat_id, author_type="OWNER" if owner else "OPERATOR",
                             message_type="image" if image else "text", text="" if image else original,
                             en="" if image else english, t=t, lang=lang, state=state, area=area,
                             medical="TRUE" if rng.random() < 0.3 else "FALSE",
                             emergency="TRUE" if rng.random() < 0.05 else "FALSE",
                             ticket=tickets[min(k * len(tickets) // n, len(tickets) - 1)]))
    records = []
    for i, r in enumerate(rows):
        stamp = r["t"].strftime("%Y-%m-%d %H:%M:%S") + f".{i % 1000000:06d} UTC"
        records.append(
            {
                "chat_id": r["chat_id"],
                "message_id": str(5_000_000 + i),
                "ticket_uuid": r["ticket"],
                "author_type": r["author_type"],
                "message_type": r["message_type"],
                "message_content": r["text"],
                "message_content_en": r["en"],
                "inserted_at": stamp,
                "updated_at": stamp,
                "user_language": r["lang"],
                "user_state": r["state"],
                "res_program": "RES",
                "res_condition_area": r["area"],
                "has_medical_tag": r["medical"],
                "has_emergency_tag": r["emergency"],
            }
        )
    df = pl.DataFrame(records)
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    df.drop("message_content_en").write_csv(out)
    translated = out.with_name(out.stem + "_with_translation.csv")
    df.write_csv(translated)
    print(f"Wrote {out} ({df.height} messages, {args.conversations} conversations, no translation column)")
    print(f"Wrote {translated} (same rows with message_content_en, for skipping the paid translation step)")
    return 0


def cmd_annotations(args) -> int:
    cfg = load_config(args.config)
    rng = random.Random(args.seed)
    items = json.loads(cfg.path("task.items_file").read_text(encoding="utf-8"))
    specs = load_evaluators(cfg)
    raters = [r.strip().lower() for r in args.raters.split(",") if r.strip()]
    rows = []
    for item in items:
        p = item["payload"]
        row = {
            "name": p["name"],
            "description": p["description"],
            "conversation_history": json.dumps(p["transcript"], ensure_ascii=False),
        }
        for spec in specs:
            key = spec["name"].replace(" ", "_")
            scale = spec.get("scale") or [{"value": True, "name": "Yes"}, {"value": False, "name": "No"}]
            truth = rng.choices(scale, weights=[6] + [2] * (len(scale) - 1))[0]
            for rater in raters:
                if spec.get("optional") and rng.random() < 0.3:
                    choice = None
                else:
                    choice = truth if rng.random() < args.agreement else rng.choice(scale)
                row[f"{rater}_{key}/value"] = None if choice is None else choice["value"]
                row[f"{rater}_{key}/reasoning"] = None if choice is None or rng.random() < 0.5 else f"(practice) picked {choice['name']}"
            ai = truth if rng.random() < args.agreement else rng.choice(scale)
            row[f"evaluator_{key}_v1/value"] = ai["name"]
            row[f"evaluator_{key}_v1/reasoning"] = f"(practice) judged {ai['name']}"
        for rater in raters:
            row[f"{rater}/comment"] = "(practice comment)" if rng.random() < 0.1 else None
        rows.append(row)
    out = Path(args.out) if args.out else cfg.path("dashboard.export_csv")
    out.parent.mkdir(parents=True, exist_ok=True)
    pl.DataFrame(rows, infer_schema_length=None).write_csv(out)
    print(f"Wrote {out}: {len(rows)} conversations x {len(specs)} questions x {len(raters)} raters + AI")
    return 0


def main() -> int:
    utf8_console()
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="command", required=True)
    e = sub.add_parser("export", help="fake conversation export")
    e.add_argument("--out", required=True)
    e.add_argument("--conversations", type=int, default=100)
    e.add_argument("--seed", type=int, default=1)
    a = sub.add_parser("annotations", help="fake Calibrate annotation export built from items.json")
    add_config_arg(a)
    a.add_argument("--raters", default="asha,ravi,meena,john")
    a.add_argument("--agreement", type=float, default=0.75, help="Chance a rater picks the 'true' answer.")
    a.add_argument("--out", default=None, help="Default: dashboard.export_csv.")
    a.add_argument("--seed", type=int, default=1)
    args = ap.parse_args()
    return cmd_export(args) if args.command == "export" else cmd_annotations(args)


if __name__ == "__main__":
    sys.exit(main())
