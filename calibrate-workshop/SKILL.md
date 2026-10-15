---
name: calibrate-workshop
description: >-
  Set up and run a rater calibration (human labeling) workshop on Calibrate with Claude Code. Turns a
  chat or WhatsApp conversation export into a Calibrate annotation task with rubric questions, an AI
  judge and one labeling link per rater, then turns the downloaded annotations into an inter-rater
  agreement dashboard for the group discussion, and rolls the revised rubric into the next round.
  Use when someone asks to set up a Calibrate project, task or annotation task, run a labeling or
  rubric workshop, write evaluator questions, create annotator links, run the AI judge, compare
  raters, build an agreement dashboard from a Calibrate CSV export, or prepare the next workshop.
  Ships Noora Health presets (India and Bangladesh RES data, self-hosted Calibrate).
metadata:
  author: The Agency Fund
  version: 1.0.0
---

# Calibrate workshop

A **rater calibration workshop** puts a small group of experts in front of the same 20 to 30 real
conversations. Each person answers the same rubric questions on their own in
[Calibrate](https://docs.calibrate.artpark.ai/getting-started/introduction), an AI judge answers
them too, and then the group meets to look at where they disagreed and why. The output is a
sharper rubric and a measured sense of how far the AI judge can be trusted. Noora Health ran four
of these in 2026 (Bangladesh, then three India rounds); this skill packages how they were set up
so anyone with Claude Code can repeat it on their own data.

What the person ends up with:

- a Calibrate annotation task holding the conversations and the rubric questions
- one private labeling link per rater (no login needed), collected in a sheet
- the AI judge's answers on the same conversations
- a dashboard that shows, per conversation and per question, who disagreed with the majority and
  their reasoning, plus agreement statistics
- a revised rubric, ready for the next round

---

## How to work with the person

**Coach, one step at a time.** Most people using this are program or research staff, not
engineers. Ask one question at a time and always offer a recommended answer they can accept. Say
what you are about to run and why in one plain sentence, run it, and report the result in plain
words. Keep commands and file paths in code blocks they can copy.

| Don't say | Say instead |
|---|---|
| "evaluator" (first time) | "question (Calibrate calls it an evaluator)" |
| "payload", "item" | "conversation" |
| "job" | "labeling link" |
| "POST failed with 403" | "Calibrate didn't let the API key do this, so we'll do it in the web app" |
| "Krippendorff's alpha" (unexplained) | "agreement corrected for chance (1 = perfect, 0 = no better than chance)" |

**Resume, don't restart.** Every workshop folder has a `progress.md`. Read it first; after each
phase, add one line (date, phase, result). A new session picks up from the last line.

**Data rules. These are not optional.** The conversations are usually patient or user messages.

1. Never open, print, `cat`, `head` or `Read` the export, the sample, `items.json`, the annotation
   export, `dashboard.html` or `.env`. Use `inspect_export.py` for structure and the scripts'
   printed counts for everything else. To check how conversations look, upload three with
   `calibrate_workshop.py create --limit 3` and ask the person to open them in Calibrate (in a
   practice run, ask them to open `out/dashboard.html`). The helper's `--offline` and `--dry-run`
   previews show conversation ids and counts, never message text; `--show-prompts` prints the AI
   judge's instructions, which contain no conversation text.
2. Keys live only in `.env`, typed in by the person. You may create `.env` with empty
   placeholders; never ask them to paste a key into the chat.
3. Never commit data. Phase 0 writes a `.gitignore`; keep the workshop folder out of shared repos.
4. Ask before anything leaves the machine: translation (OpenAI), the upload to Calibrate, the links
   sheet on Google Drive, and any hosting of the dashboard.
5. Labeling links work without a login. Each goes only to its owner.
6. If a permission prompt or safety check blocks a step that touches the data (for example pulling
   annotations through the API), don't look for a way around it. That step becomes a manual step
   for the person, and the skill already has one for each case.

---

## Setup check (once per machine)

Read `references/setup.md` and walk the person through anything missing.

| Need | Check |
|---|---|
| Claude Code, with this skill installed | `/calibrate-workshop` is listed when they type `/` |
| Python 3.10+ with the packages in `scripts/requirements.txt` | `python -c "import polars, requests"` |
| A Calibrate login in the right workspace and an API key in `.env` | `calibrate_workshop.py check` prints "Key works" (not needed for a practice run) |
| The right Calibrate server | Noora uses a self-hosted one; see `references/noora-profile.md` |
| (optional) OpenAI API key, for translation | only if messages need translating |
| (optional) Google Drive connector in Claude | for the links sheet; otherwise they upload a CSV |
| (optional) Node.js + a Vercel account | only to host the dashboard online |

Scripts live in this skill's `scripts/` folder. Below, `<skill>` means the folder this file is in
(usually `~/.claude/skills/calibrate-workshop`) and `python` means the Python from
`references/setup.md` (often `python3` on a Mac without a virtual environment). Run every script
from the workshop folder: `python <skill>/scripts/<script>.py --config workshop.json`.

---

## The workflow

Each phase lists what to ask, what to run, and what "done" looks like. Details, options and
failure modes are in the reference file named in each heading.

### Phase 0. Workshop folder (`references/setup.md`)

Ask where the folder should live (outside any shared git repo; a synced drive is fine if only the
team can see it). Create:

```
<workshop>/
  workshop.json      settings (start from a preset in assets/ or scripts/workshop.example.json)
  evaluators.json    the rubric (start from assets/ or the previous workshop)
  .env               CALIBRATE_API_KEY=, OPENAI_API_KEY=  (the person fills these in)
  .gitignore         .env  data/  out/  *.csv
  progress.md        one line per finished phase
  data/              the export goes here
  out/               everything the scripts produce
```

Noora staff: start from `assets/workshop.noora-india.json` or `assets/workshop.noora-bangladesh.json`.
In `workshop.json`, `workshop.name` is the display name (dashboard title and password page),
`workshop.slug` a short id for the dashboard's browser storage (`nh-w5`), and `workshop.prefix`
goes in front of every question name (see phase 4). `task.name` is what Calibrate shows.

### Phase 1. Look at the export (`references/data-prep.md`)

Ask the person to save their export as CSV in `data/`. Run `inspect_export.py data/<file>.csv`.
It prints column names, empty counts and the values of short categorical columns, never message
text. Together, fill `data.columns` in `workshop.json` (conversation id, speaker, text,
translation, timestamp, order) and the speaker settings (`speaker_labels`, `assistant_speakers`,
`drop_speakers`).

### Phase 2. Choose the conversations (`references/data-prep.md`)

Decide: how many (recommend 25), random or hand-picked by experts, minimum length (recommend 10+
messages so there is something to judge), language filter, and whether to drop conversations with
images or voice notes (recommend yes: annotators would see gaps). Run `make_sample.py`. It prints
how many conversations each filter removed; read that back to the person.

### Phase 3. Translate, if needed (`references/data-prep.md`)

Only if raters need English. **Ask first**: this sends message text to OpenAI, and the data owner
must agree. Then `translate.py --limit 20 --confirm-send`, then `--resume --confirm-send`, then
`--verify` (must print PASS). If the export already has an English column (Noora Bangladesh, or
the practice data's `export_with_translation.csv`), set `data.columns.translation` to it and run
only `translate.py --verify`: it sends nothing and checks the column is complete.

### Phase 4. The rubric (`references/rubric-and-items.md`)

Start from the previous workshop's `evaluators.json`, the Noora rubric
(`assets/evaluators.noora-rubric.json`) or the two-question starter. Work through each question
with the person: the question as annotators will read it, the answer options and what each means,
whether it may be skipped. Pick a **new prefix** for this workshop (`workshop.prefix`, e.g.
`NH W5`). Calibrate matches questions by name, so an old prefix silently reuses old questions.

### Phase 5. Build the conversations for Calibrate (`references/rubric-and-items.md`)

Run `build_items.py --config workshop.json`. Expect `Validation: PASS`. Fill in `judge.*` in
`workshop.json` (who is judged, the setting, what each message shows); it becomes the AI judge's
instructions.

### Phase 6. Create the task on Calibrate (`references/calibrate-task.md`)

```
python <skill>/scripts/calibrate_workshop.py check  --config workshop.json
python <skill>/scripts/calibrate_workshop.py create --config workshop.json --dry-run --show-prompts
python <skill>/scripts/calibrate_workshop.py create --config workshop.json
```

Confirm with the person before the real `create`. Then ask them to open the task page it prints
and look at two conversations: speaker names, both languages, time tags, the panel on the right,
and every question with its options. Fix and re-run `create --update` if anything is off.

### Phase 7. Raters and their links (`references/calibrate-task.md`)

Collect rater names (first names, lowercase, unique). Run `annotators`, then `jobs`. It writes
`out/annotator_links.csv`. If Calibrate refuses job creation with the API key, the script prints
the web-app steps; after the person does them, run `links`. Offer to put the links in a Google
Sheet with restricted sharing (Drive connector, or they import the CSV).

### Phase 8. The AI judge (`references/calibrate-task.md`)

When raters have finished, run `run-judge --wait` (or the person clicks run in the task page if
the API key can't). Running it after the humans keeps it on the same final question wording.

### Phase 9. The dashboard (`references/dashboard.md`)

The person downloads the items export from the task page and saves it as
`out/annotations_export.csv`. Run `build_dashboard.py`, then ask the person to open
`out/dashboard.html` in their browser and check it. Share it the way they choose: as a file in a restricted Drive folder (default), or password-encrypted on their
own free Vercel project (`encrypt_dashboard.py`, then `deploy_vercel.py`).

### Phase 10. The session and the next round (`references/workshop-playbook.md`)

Help plan the session: agenda, which conversations to discuss (sort by most disagreement), how to
record rubric decisions. Afterwards, edit `evaluators.json` with the agreed changes. For the next
workshop, copy the folder settings (see below). To fix the judge's wording on the current task,
run `update-evaluators`.

---

## Practice run (invented data, no API key)

Offer this to anyone new, before their first real workshop. Everything runs on the laptop.

1. Phase 0 as usual, with `assets/workshop.noora-india.json` as `workshop.json` and
   `assets/evaluators.noora-rubric.json` as `evaluators.json`. No `.env` keys needed.
2. `python <skill>/scripts/make_synthetic_data.py export --out data/export.csv --conversations 100`.
   It also writes `data/export_with_translation.csv`. Point `data.raw_export` at that file so
   phase 3 is only `translate.py --verify`.
3. Phases 1, 2, 4 and 5 as usual.
4. Phases 6 to 8 with `--offline` on every `calibrate_workshop.py` command (add `--show-prompts`
   to `create` to read the judge instructions). Nothing is sent; no links file is written.
5. `python <skill>/scripts/make_synthetic_data.py annotations --config workshop.json --raters asha,ravi,meena`
   stands in for the raters, then phase 9: `build_dashboard.py`, and the person opens
   `out/dashboard.html`. Optionally `encrypt_dashboard.py` to see the password page.

To also see Calibrate's screens, run phases 6 to 8 for real with a prefix and task name starting
`PRACTICE`, in a workspace the person may clutter. Questions created this way can only be deleted
in the web app.

---

## Next workshop from the last one

1. New folder. Copy `workshop.json`, `evaluators.json` and `.gitignore` from the last one.
2. Change `workshop.name`, `workshop.slug`, **`workshop.prefix`**, `task.name`, `dashboard.title`,
   and the data paths.
3. Apply the rubric decisions from the last session to `evaluators.json`.
4. New conversations: a new export, a new `sample.seed`, or a new hand-picked list.
5. Same raters: keep `annotators`; they already exist in Calibrate.
6. Phases 2 to 9 as before. Keep the old folder: its export and dashboard are the record.

---

## What has and hasn't been tested

The scripts were rebuilt from the ones used for Noora's workshops and checked against them: on
the Workshop 4 data they reproduce the uploaded conversations, the judge instructions and the
dashboard numbers exactly. These steps were **not** re-run against a live server for this
version: creating annotators, creating labeling links and running the AI judge with the API key.
Calibrate's public documentation says the API key can do all three. On Noora's self-hosted server
in August and September 2026 it could not create labeling links. If the server refuses, the
scripts stop and print the web-app steps instead. Tell the person this up front.

---

## Reference files

| File | Read when |
|---|---|
| `references/setup.md` | first run on a machine; installing; keys; the workshop folder |
| `references/data-prep.md` | phases 1 to 3: columns, sampling, translation |
| `references/rubric-and-items.md` | phases 4 and 5: writing questions, answer options, the item format |
| `references/calibrate-task.md` | phases 6 to 8: every `calibrate_workshop.py` command, fallbacks, CLI and MCP equivalents |
| `references/dashboard.md` | phase 9: export, dashboard, sharing, encrypted hosting |
| `references/workshop-playbook.md` | phase 10: running the session, reading agreement, the next round |
| `references/pitfalls.md` | something behaves oddly |
| `references/noora-profile.md` | the person is at Noora Health |
| `references/links.md` | original documentation for every tool used |

Scripts (all print counts, never message text): `inspect_export.py <csv>`, and with
`--config workshop.json`: `make_sample.py`, `translate.py`, `build_items.py`,
`calibrate_workshop.py <command>`, `build_dashboard.py`, `encrypt_dashboard.py`,
`deploy_vercel.py`. `make_synthetic_data.py export --out <csv>` and
`make_synthetic_data.py annotations --config workshop.json` make invented data for practice.
