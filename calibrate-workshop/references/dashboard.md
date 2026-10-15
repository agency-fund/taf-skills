# The agreement dashboard (phase 9)

One HTML file, built from the annotation export, that makes it obvious who disagreed with the
majority, on which conversation and question, and why. It was built for the discussion in the
room, not for a report.

## 1. Get the export (the person does this)

On the task page in Calibrate, download the items export (CSV). Save it as
`out/annotations_export.csv` in the workshop folder (or set `dashboard.export_csv`). This is the
raters' answers; don't confuse it with the conversation export in `data/`.

Claude does not pull annotations through the API: the file contains every conversation plus
every rater's reasoning, and a manual download keeps it out of the chat. (Some Claude Code
permission settings block the API route anyway.)

What's inside, one row per conversation:

| Column | Holds |
|---|---|
| `name`, `description`, `conversation_history` | the conversation exactly as uploaded |
| `<rater>_<Question_Name>/value` and `/reasoning` | each rater's answer and reason; spaces in the question name become `_` |
| `<rater>/comment` | a rater's note on the whole conversation |
| `evaluator_<Question_Name>_v<N>/value` and `/reasoning` | the AI judge, version N (only if it was run) |

Raters' answers are stored as the option's **value** (1, 2, `true`); the judge's as the option's
**name** ("Yes"). The builder maps both back to names using `evaluators.json`, so it must be the
same spec (same names, same prefix) the task was created from.

## 2. Build

```
python <skill>/scripts/build_dashboard.py --config workshop.json
```

Expect: `Conversations: 25   messages: 459   questions: 7` and the list of raters. Warnings mean:

- *"rating column(s) match no question"*: the spec's names or prefix differ from the task's.
- *"answers did not match any option"*: an option was renamed or re-valued after labeling began.
- *"AI evaluator (not run)"*: there were no judge columns; everything still works without them.
- If the judge was run more than once, the newest version's column is used.

Settings under `dashboard` in `workshop.json`: `title`, `rater_names` (`{"asha": "Asha R."}`),
`rater_order`, `hint_fields` (panel labels to show under each conversation id in the list, such
as `["RES condition area", "User state"]`), `speaker_acronyms` (speaker names to keep in capitals,
such as `["MSE"]`).

To demo without real data: `make_synthetic_data.py annotations --config workshop.json` writes a
fake export from the built items.

## 3. What the dashboard shows

Two tabs and two switches.

**Switches** (top right, and they change every number):
- *Majority from*: humans only (default) or humans plus AI.
- *Options*: as rated, or "Yes vs. not Yes", which folds every answer except the first option
  into one (useful when the real question is "did it meet the standard?"). Only shown when a
  question has more than two options.

**Agreement overview**
- Answer options and their colours, as raters saw them.
- Per question: share of conversations where humans were unanimous; average agreement between
  each pair of humans; agreement corrected for chance (Krippendorff's alpha, nominal) among
  humans and with the AI added; how often the AI matched the human majority; number of splits (a
  tie, no majority); answers per rater.
- *Who disagrees with the majority*: rater by question, darker = more often off the majority.
- *Pairwise agreement*: every pair of raters, AI included, per question or pooled.
- *How each rater used the options*: shows, for example, someone who never answers "No".

**Conversations**
- A list sortable by most disagreement, by "AI off the majority", or original order, with a
  focus filter for one question. Each row has a strip of squares, one per question: darker =
  more raters off the majority, striped = split, outlined = AI off the majority.
- For the selected conversation: the ratings grid with the majority and its tally (≠ marks each
  dissent); "Where raters part ways", which lists the dissenters' reasoning first; rater
  comments; the transcript (English, with a switch for the original); every rating and reason in
  a table at the bottom. Arrow keys move between conversations, and each one has its own link
  (`#c-<id>`) for pointing the room at it.

How to read alpha: 1 is perfect, 0 is what chance would give, below 0 is worse than chance. A
common rule of thumb (Krippendorff) treats 0.8 and above as reliable and 0.67 to 0.8 as tentative.
With 25 conversations the numbers are rough; use them to choose what to discuss, not to grade
anyone.

## 4. Share it

The HTML file contains every conversation and every rater's reasoning. Treat it like the export.

**Default: a file.** The person opens `out/dashboard.html` in any browser; it works offline. To share, put it in
a Google Drive folder restricted to the workshop group, and have people download and open it.
(Drive's preview does not run it.) Never post it in a public place or commit it to git.

**Optional: a password-protected web page on the person's own free Vercel account.** Useful when
people need a link that works on any device. Vercel's own password feature is a paid add-on, so
the page is encrypted instead: Vercel only ever stores ciphertext, and the browser decrypts it
with the password.

```
python <skill>/scripts/encrypt_dashboard.py --config workshop.json            # asks for a password
python <skill>/scripts/deploy_vercel.py --config workshop.json --create <unguessable-project-name>
```

- One-time: Node.js installed, `npx vercel login` done (https://vercel.com/docs/cli).
- Password: at least 10 characters; a short phrase works. The person types it at the prompt or
  sets `DASHBOARD_PASSWORD` for that one command. Never store it in a file. Send the link and the
  password through different channels.
- `--create <name>` makes the Vercel project and links `out/site/` to it. The site lives at
  `https://<name>.vercel.app`, so choose a name nobody would guess (add a random suffix). Later
  redeploys: `encrypt_dashboard.py` then `deploy_vercel.py` without `--create`.
- What the page does: asks for the password; "remember on this device" keeps it unlocked for 30
  days; otherwise a reload stays unlocked for 8 hours in that tab. Search engines are told not to
  index it (`assets/vercel.json`).
- `encrypt_dashboard.py --rotate-salt` logs out every remembered device (use it if a password
  leaks, along with a new password).
- Why the upload goes through a temporary folder: the Vercel CLI attaches the latest git commit's
  author to each deployment, and the free plan blocks deployments whose author email isn't the
  account's. Blocked deployments look like an endless "Building" in the Vercel dashboard. The
  script copies the two files outside any git repo first.
- The script refuses to upload anything that is not the encrypted password page.
- Old deployments keep their own addresses. If an unencrypted version was ever deployed, delete
  that deployment in the Vercel dashboard.

Not GitHub Pages: on most organisation plans those sites are public, and the data would have to be
committed to a repository.
