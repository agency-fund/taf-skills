# The rubric and the conversation items (phases 4 and 5)

## How Calibrate models a rubric

Each rubric question is an **evaluator** in Calibrate. One evaluator serves two audiences at once:
human raters see its description and answer buttons; the AI judge gets a written instruction
(the "system prompt") built from the same text. Calibrate has only two kinds
([evaluator docs](https://docs.calibrate.artpark.ai/api-reference/evaluators/create-evaluator)):

- `binary`: two answers, stored as `true` / `false`. The two can be renamed (Workshop 3 and 4:
  `false` = Routine, `true` = Emergency).
- `rating`: any number of answers, stored as whole numbers 1, 2, 3 ...

There is **no categorical type**. For more than two named answers, use `rating` with a named
scale. That is how Workshops 3 and 4 got Yes / No / Not enough Information / Not Applicable.
(It also means Calibrate's own statistics treat those answers as numbers; the dashboard here
treats them as categories.)

## `evaluators.json`

A list, one entry per question, in the order raters see them:

```json
{
  "name": "Empathetic",
  "description": "Is the MSE's response empathetic?",
  "rubric": "Response acknowledges the patient's concerns and does not dismiss any of the patient's worries or concerns.",
  "output_type": "rating",
  "optional": false,
  "focus": "Judge the nurse's response(s) across the whole conversation.",
  "scale": [
    {"value": 1, "name": "Yes", "description": "Response acknowledges the patient's concerns and does not dismiss any of the patient's worries or concerns.", "color": "#16a34a"},
    {"value": 2, "name": "No", "description": "The response does not meet this standard.", "color": "#dc2626"},
    {"value": 3, "name": "Not enough Information", "description": "The conversation does not contain enough information to judge this.", "color": "#ca8a04"},
    {"value": 4, "name": "Not Applicable", "description": "This criterion does not apply to this conversation.", "color": "#6b7280"}
  ]
}
```

| Field | Meaning |
|---|---|
| `name` | Short label. The workshop prefix is added in front (`NH W5 - Empathetic`). Becomes the column name in the export, so keep it short and stable. |
| `description` | The question exactly as raters read it. A bare question; definitions go on the options. |
| `rubric` | The standard for "Yes", in one sentence. Kept for the record and the dashboard tooltip; for two-option questions without a `scale` it also goes into the judge's instructions. |
| `output_type` | `rating` or `binary` (default `binary`). |
| `scale` | The answer buttons, in order: `value` (1, 2, 3 ... for rating; `true` / `false` for binary), `name`, `description` (what choosing it means; shown to raters and given to the judge), `color` (hex, used in Calibrate and the dashboard). Without a scale a question is plain Yes/No. |
| `optional` | `true` lets raters skip it. Set per task: `create` applies all optional flags as one set. |
| `focus` | One sentence telling the AI judge what to look at, when it differs from `judge.focus` (for example a question about the user's message, not the agent's reply). |

Starting points: `assets/evaluators.noora-rubric.json` (the 7 questions of Workshops 3 and 4),
`assets/evaluators.starter.json` (two generic questions), or the previous workshop's file.

## Writing good questions

Lessons from four rounds:

- **One idea per question.** "Accurate and safe" gets split answers that mean different things.
- **The question stays bare; the definition lives on the "Yes" option.** Workshop 3's first draft
  repeated the standard in both places; it was cut back to keep the screen simple. Write "Is the MSE's response easy to
  understand?" and put "Response is clear and avoids medical jargon." on Yes.
- **Give an honest way out.** "Not enough Information" and "Not Applicable" stop raters from forcing
  Yes or No onto conversations that never raised the issue. Look at how often they are used in
  the dashboard; heavy use usually means the question needs narrowing.
- **Make skipping explicit.** If a question only applies sometimes (a classification of the user's
  query, say), mark it `optional` rather than adding "N/A" guesses.
- **Match the transcript's words.** If speakers are labelled AGENT, a question about "the MSE"
  makes raters translate in their head. (Workshop 4 kept "MSE" in the questions with AGENT labels
  to stay identical to Workshop 3; decide this on purpose.)
- **Pin down external definitions.** Workshop 3's classification question said "as defined by
  CoPilot's definition", but the definition itself never reached the AI judge, which then used a
  generic one. Paste the actual definition into the option descriptions.
- **Choose names once.** Calibrate matches evaluators by name, and an API key cannot rename them.
  A new workshop gets a new prefix rather than renamed questions.

## The AI judge's instructions

`calibrate_workshop.py create` writes each judge prompt from the question, its options, and the
`judge` block of `workshop.json`:

```json
"judge": {
  "subject": "a conversation between a nurse and a patient",
  "context": "The context is Noora Health's Remote Engagement Services, where nurses (MSEs) answer patients' questions over WhatsApp in India.",
  "message_format": "Each message shows its message type and medical/emergency tags, followed by the original Hindi text and its English translation.",
  "focus": "Judge the nurse's (MSE's) response(s) across the whole conversation.",
  "judged": "the nurse"
}
```

The result reads: "You are a highly accurate evaluator assessing {subject}. {context} You will be
given a full conversation. {message_format} {focus} Question: ... Choose exactly one of these
answers ... - Yes: ... - No: ... Respond with the chosen answer's name exactly as written above,
and a one-sentence reason grounded in the conversation." With the Noora values above it is,
word for word, the prompt used in Workshops 3 and 4. The judge model is `calibrate.judge_model`
(default `openai/gpt-5.4-mini`).

To read every prompt before anything is created, run
`calibrate_workshop.py create --config workshop.json --offline --show-prompts`.

## Phase 5: build the items

```
python <skill>/scripts/build_items.py --config workshop.json
```

(To try Calibrate with a few conversations first, `calibrate_workshop.py create --limit 3` uploads
only the first three; a later full `create --update` adds the rest without duplicates.)

It reads the translated sample if there is one (else the sample), groups messages by
conversation, sorts them, and writes `task.items_file`. Expect:

```
Items:       25   messages: 459   roles: ['assistant', 'user']
Speakers:    *** AGENT ***, *** USER ***
Time zone:   IST (UTC+05:30)
Validation:  PASS
```

What each conversation looks like in Calibrate, and why:

```
*** USER ***
Type: text | Medical tag: True | Emergency tag: False

[Hindi — original]
<message as sent>

[English — translation]
<translation>
```

- **Speaker name in the text, role `user` / `assistant` underneath.** Calibrate's transcript view
  only understands those two roles. Any other role is accepted and stored, but the whole
  conversation then shows as a single dash; it looks like a data problem and isn't. The builder
  refuses other roles.
- **Time tags in the bare form `YYYY-MM-DD HH:MM:SS`.** Microseconds or a zone suffix stop the tag
  from rendering. The builder converts to `data.display_timezone` first and writes the zone into
  the panel.
- **Panel on the right** = the item description: conversation id, message count, then
  `data.description_fields`, the time zone, and the expert's note for hand-picked conversations.
- **Empty values show as `NA`**, never as a blank or the word "None"; the validator fails the build
  if a "None" slips through.
- **The dashboard reads this layout back** out of the export (speaker, tags, both languages). Keep it.

`Validation: PASS` checks unique names, non-empty conversations, the two roles, time tag format
and stray "None" values. On FAIL it lists the first 20 problems and exits with an error; nothing
is uploaded until it passes.
