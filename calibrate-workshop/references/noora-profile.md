# Noora Health profile

Defaults and history for Noora Health staff. Everything here is safe to publish: no ids, people,
links or conversation text. Ask your TAF contact for anything workshop-specific (folders, previous
task pages, rater list).

## Calibrate server and workspace

Noora's workshops run on a **self-hosted Calibrate**, not the public service the Calibrate docs
describe:

- Web app: `https://calibrate.learning.org.ai`
- API (for `calibrate.api_url`): `https://calibrate-backend.learning.org.ai`
- Workspace: **TAF | Noora Health** (the same server also hosts other TAF workspaces; check the
  workspace switcher before creating anything)

A key made here returns 401 on `api.calibrate.artpark.ai` and the other way round. With the CLI:
`calibrate configure --no-interactive --server-url https://calibrate-backend.learning.org.ai`
before logging in.

Known behaviour of this server (Aug to Oct 2026): creating labeling jobs and editing evaluator text
needed a browser session, not the API key; `get-agreement` and `get-summary` returned 404. The
skill's fallbacks (web app, then `links`) cover this. Labeling links look like
`https://calibrate.learning.org.ai/annotate-job/<token>` and open without a login.

## Presets

- `assets/workshop.noora-india.json`: the India RES ticket-message export (Workshop 4 settings).
  Columns `chat_id`, `author_type` (OWNER / OPERATOR / SYSTEM), `message_content`,
  `message_content_en` (added by translation), `updated_at` (time tag), `inserted_at` (order),
  `message_id`, `user_language`; per-message tags `message_type`, `has_medical_tag`,
  `has_emergency_tag`; panel fields for tickets, due date, baby's birth date, language, state,
  RES program, condition area, mother's age, high-risk details, operator type. Hindi only, 25
  conversations of 10+ messages, SYSTEM rows dropped, duplicates dropped, IST time tags, speakers
  shown as USER / AGENT.
- `assets/workshop.noora-bangladesh.json`: the translated Bangladesh RES dataset (one row per
  message: `user_phone_hash`, `convo_id`, `msg_id`, `turn_index`, `role`, `timestamp_utc`, `text`,
  `text_en`, `user_language`, `user_condition_area`, `country`). Already translated, so skip
  phase 3. A `convo_id` is a 48-hour window that starts with a message the platform classed as
  medical. **Before building items, run `inspect_export.py` and replace the placeholder speaker
  values** (`USER`, `NURSE`) with the real values of `role`. Time tags in Asia/Dhaka.

## The rubric so far

`assets/evaluators.noora-rubric.json` holds the 7 questions used in Workshops 3 and 4 (prefix
removed; add a new one in `workshop.prefix`):

| Question | Options |
|---|---|
| Easy to understand: Is the MSE's response easy to understand? | Yes / No / Not enough Information / Not Applicable |
| Empathetic | same |
| Contextually appropriate | same |
| Clear next steps | same |
| Accurate | same |
| Safe | same |
| Classification: How would you classify this query? (optional) | Routine / Emergency |

"Yes" carries each question's standard; the other three options are shared. Two open items from
those rounds:
- The classification question refers to CoPilot's definition of Routine vs Emergency, which was
  never written into the options, so the AI judge used a generic definition. Paste the real
  definition into the two option descriptions.
- Questions say "MSE" while Workshop 4 transcripts label the speaker AGENT. Align them, or keep
  the difference on purpose.

The judge settings that reproduce the Workshop 3 and 4 prompts exactly are in the India preset's
`judge` block.

## History (for context)

| Round | Data | Conversations | Questions | Notes |
|---|---|---|---|---|
| Workshop 1 | Bangladesh, English | 100 before and 100 after AI assistance was introduced | five-option questions, set up in the web app | Time tags in Asia/Dhaka |
| Workshop 2 | India, Hindi + English | 200 random | 12 Yes/No | Speakers Patient / MSE; UTC time tags |
| Workshop 3 | India, Hindi + English | 25 hand-picked by experts, in their order, each with the question it was picked for | 7, four-option + optional classification | First round with named options and an optional question |
| Workshop 4 | India, Hindi + English | 25 random, Hindi, 10+ messages | same 7, new prefix | Speakers USER / AGENT; IST time tags |

Workshops 3 and 4 each had an agreement dashboard hosted as an encrypted page on Vercel; ask your
TAF contact for access rather than looking for the links.
