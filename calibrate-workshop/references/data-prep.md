# Data preparation (phases 1 to 3)

From a raw export to the exact conversations raters will see. All three scripts read
`workshop.json`, print counts only, and never show message text.

## The export Claude can work with

One row per message, as CSV (Excel: File, Save as, CSV UTF-8). Required columns, under any names:

| Role in `data.columns` | What it is | Noora India | Noora Bangladesh |
|---|---|---|---|
| `conversation_id` | groups messages into one conversation | `chat_id` | `convo_id` |
| `speaker` | who sent it | `author_type` (OWNER, OPERATOR, SYSTEM) | `role` |
| `text` | the message as sent | `message_content` | `text` |
| `timestamp` | when; shown as the time tag | `updated_at` | `timestamp_utc` |

Optional:

| Role | What it is | Noora India | Noora Bangladesh |
|---|---|---|---|
| `translation` | English version. `null` if there is none and none is needed | `message_content_en` (added by `translate.py`) | `text_en` |
| `order_by` | sort order inside a conversation, if not the timestamp | `inserted_at` | `turn_index` |
| `message_id` | tie-breaker for messages with the same time | `message_id` | `msg_id` |
| `language` | per-message language; filters the sample and labels the original text ("Hindi — original") | `user_language` | `user_language` |

A conversation is whatever the export groups under one id. Noora India's `chat_id` is a whole
WhatsApp thread with one user; Noora Bangladesh's `convo_id` is a 48-hour window that starts with
a medical message. Check which one the person's export uses; it changes what "one conversation"
means to a rater.

## Phase 1: inspect, then fill in `workshop.json`

```
python <skill>/scripts/inspect_export.py data/export.csv
```

It prints each column's empty and distinct counts, the values of short categorical columns (for
example `author_type: OWNER=332, OPERATOR=298, SYSTEM=7`), a guess at which column plays which
role, conversation lengths (how many have 5+, 10+, 20+ messages) and the time range. Message
text columns are never listed.

Then, with the person:

- **`data.columns`**: confirm or correct each guess.
- **`data.speaker_labels`**: raw speaker value to the name raters see. Short and neutral works best
  (`{"OWNER": "USER", "OPERATOR": "AGENT"}` in Workshop 4; `Patient` / `MSE` in Workshops 2 and 3).
  Match the wording the rubric uses: if questions say "the nurse's response", label that speaker
  NURSE, not AGENT.
- **`data.assistant_speakers`**: the raw value(s) of the side being judged. Their messages go to
  Calibrate with the `assistant` role, everyone else's with `user` (the only two roles it shows).
- **`data.drop_speakers`**: automated senders to remove entirely (`SYSTEM`, template bots).
- **`data.message_meta`**: per-message tags worth showing above each message, as
  `[{"column": "message_type", "label": "Type"}, ...]`. Leave empty if none.
- **`data.description_fields`**: conversation-level facts for the panel on the right of each
  conversation in Calibrate (program, region, condition area, due date). Each is
  `{"column": ..., "label": ..., "mode": "first" | "distinct" | "count"}`: `first` shows the first
  non-empty value, `distinct` lists every distinct value in order (for things that change within a
  conversation), `count` counts distinct values (for example tickets). Columns the export lacks are
  skipped, so one preset works across exports.
- **`data.display_timezone`**: an IANA zone name (`Asia/Kolkata`, `Asia/Dhaka`, `Africa/Nairobi`)
  so raters see local times. Timestamps are read as UTC unless they carry their own offset.
  The zone is written into the panel ("Time zone: IST (UTC+05:30)").

## Phase 2: choose the conversations

```
python <skill>/scripts/make_sample.py --config workshop.json
```

Decisions, with the recommended answer first:

- **How many?** 25. Workshops 3 and 4 each used 25 conversations with 7 questions. Fewer than 15 gives agreement numbers that swing on one conversation; more than
  40 tires people out.
- **Random or hand-picked?** Random for a first look at the data. Hand-picked when experts want
  specific situations discussed (Workshop 3 used 25 conversations chosen by experts, each with the
  question it was picked for). For hand-picked, export the experts' sheet as CSV and set
  `sample.ids_file`, `sample.ids_column`, and optionally `sample.note_column` / `sample.note_label`
  to show their note in the panel. Item order then follows the sheet.
- **Minimum length?** 10 messages (`sample.min_messages`). Very short exchanges leave most
  questions "Not Applicable".
- **Drop conversations with images, audio or stickers?** Yes (`sample.require_text: true`). Those
  messages carry no text, so raters would see gaps.
- **Exact duplicate rows?** Drop them (`sample.drop_duplicates: true`); some exports repeat rows.
- **Language?** Filter to one language per workshop (`data.language_filter`) unless raters read all
  of them.
- **Seed**: keep 42 unless redrawing; the same seed and filters give the same sample.

The script prints rows and conversations left after each filter, then the length spread. If the
eligible pool is smaller than the sample size it stops; loosen a filter rather than lowering the
sample silently, and tell the person which filter bit hardest.

## Phase 3: translate (optional)

Needed when raters do not all read the original language.

**Already translated?** When the export already has an English column (Noora Bangladesh does, and
so does the practice data's `export_with_translation.csv`), set `data.columns.translation` to that
column and run only `translate.py --config workshop.json --verify`. It sees the column, sends
nothing, and checks that every message with text has a translation (PASS). `build_items.py` reads
`data.translated_file` if that file exists, otherwise the sample, so either setting works.

**Ask first, every time.** This sends every message in the sample to OpenAI. The person must
confirm the data owner allows that. The script refuses to call the API without `--confirm-send`.

```
python <skill>/scripts/translate.py --config workshop.json --limit 20 --confirm-send   # small paid trial
python <skill>/scripts/translate.py --config workshop.json --resume --confirm-send     # everything else
python <skill>/scripts/translate.py --config workshop.json --verify                    # no API call; must print PASS
```

- Set `data.columns.translation` to the name of the new column (`message_content_en`), and
  `translation.context` to one phrase describing the messages ("WhatsApp messages between patients
  and nurses on a maternal health support service in India"). `translation.language_hint` is added
  after the language name ("an Indic language").
- Model: `gpt-4.1-mini` by default, batches of 25, 5 at a time. 25 conversations (about 450
  messages) is a few minutes and well under a dollar.
- Progress is saved after every batch to `<output>.checkpoint.csv`. After a network error or an
  interrupted run, `--resume` continues; rows that came back empty are retried.
- `--verify` checks row count, column position, that ids did not change, and that every message
  with text has a translation. Run it before building items.
- Out of credit: the script says so and keeps the checkpoint; add credit and `--resume`.
- Messages without text (blank rows) are never sent.

The translation is shown under the original in Calibrate, labelled "[English — translation]". If
a translation is missing, the original is shown with a note, so raters never see an empty block.
