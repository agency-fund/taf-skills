# Creating and running the task on Calibrate (phases 6 to 8)

Everything here goes through `scripts/calibrate_workshop.py`, which calls Calibrate's public REST
API with the workspace API key (`X-API-Key` header). It runs the same on macOS, Windows and
Linux. API reference: https://docs.calibrate.artpark.ai/api-reference/introduction

```
python <skill>/scripts/calibrate_workshop.py <command> --config workshop.json [--dry-run | --offline]
```

- `--dry-run` reads from Calibrate but writes nothing; each write it would make is printed.
- `--offline` makes no network calls at all and prints every request. Use it for practice runs
  and to show the person what will be sent.
- Previews summarise: conversation uploads show the count and ids only (never message text), and
  questions show name, options and model. `--show-prompts` (with `create` or `update-evaluators`)
  prints each AI judge prompt in full; prompts are built from the settings and contain no
  conversation text.
- `<skill>` below is this skill's folder; run from the workshop folder.

Every command is safe to re-run: questions are matched by name, conversations by their id, links
by rater name.

## Phase 6: create

```
python <skill>/scripts/calibrate_workshop.py check  --config workshop.json
python <skill>/scripts/calibrate_workshop.py create --config workshop.json --dry-run --show-prompts
python <skill>/scripts/calibrate_workshop.py create --config workshop.json
```

`check` confirms the key works on `calibrate.api_url` and warns if questions with this workshop's
prefix, or a task with this name, already exist.

`create`, in order:

1. **Questions.** For each entry in `evaluators.json` (names prefixed), reuse the evaluator if one
   with that exact name exists, else create it with its first version (judge model, judge
   instructions, answer scale) live.
   [docs](https://docs.calibrate.artpark.ai/api-reference/evaluators/create-evaluator)
2. **Task.** A `conversation` task named `task.name` with `task.description`, linked to the
   questions. [docs](https://docs.calibrate.artpark.ai/api-reference/annotation-tasks/create-annotation-task)
3. **Order and optional questions.** Sets the full ordered list plus which are optional, as one
   set. [docs](https://docs.calibrate.artpark.ai/api-reference/annotation-tasks/update-task-evaluators)
4. **Conversations.** Updates ones already on the task (matched by id) and adds the rest in
   batches of 50. [add](https://docs.calibrate.artpark.ai/api-reference/annotation-tasks/bulk-create-items),
   [update](https://docs.calibrate.artpark.ai/api-reference/annotation-tasks/bulk-update-items)
5. **Read back.** Prints the item count and each question with its options and optional flag, the
   task page address, and saves ids to `task.ids_file` (`out/task_ids.json`).

If the task name already exists, `create` stops. `--update` syncs the existing task instead (after
editing questions or rebuilding conversations). `--limit 3` sends only three conversations, for a
first look.

**Then the person checks the task page.** Ask them to open two conversations and confirm:
speaker names, original and English text, time tags, the panel on the right, every question with
the right options, optional questions marked. Problems here are cheap to fix; after raters start,
they are not.

## Phase 7: raters and links

Names go in `workshop.json` as `"annotators": ["asha", "ravi", ...]`: first names, lowercase,
unique in the workspace. The links sheet shows them capitalised.

```
python <skill>/scripts/calibrate_workshop.py annotators --config workshop.json   # create any that don't exist
python <skill>/scripts/calibrate_workshop.py jobs       --config workshop.json   # one labeling job per rater
```

`jobs` writes `out/annotator_links.csv` (Name, Annotation link, Conversations, Completed,
Status). Settings in `workshop.json` under `jobs`: `reasoning_mode` (`optional`, `required`,
`hidden`; the reasoning box raters see) and `comments_enabled`.
[docs](https://docs.calibrate.artpark.ai/api-reference/annotation-tasks/create-labelling-jobs)

**If Calibrate refuses with the API key** (401/403; Noora's self-hosted server did in Aug to Sep
2026), the script stops and prints the steps:

1. The person opens the task page and creates a labeling job for each rater, all conversations.
2. Then: `python <skill>/scripts/calibrate_workshop.py links --config workshop.json`. Reading jobs works with the
   API key, so this writes the same links file.

The same applies to `annotators`: if creating them is refused, the person adds them on the
Annotators page of the web app.

**The links are keys.** Each `annotate-job/<token>` address opens that rater's labeling page with
no login. Anyone holding it can answer as that rater. Share each link only with its owner; keep
the file out of email threads and shared chats.

**Links sheet.** With the Google Drive connector, offer to create a Google Sheet from the CSV in a
folder the person names (create a file with `text/csv` content; Drive converts it to a Sheet).
Read it back to confirm. Previous workshops used two columns, Name and Annotation link, in a
restricted team folder. Without the connector, the person imports the CSV into Sheets.

**During labeling**, `python <skill>/scripts/calibrate_workshop.py status --config workshop.json`
shows each rater's progress (completed / total).

With `--offline` (practice runs), `jobs` prints the requests but writes no links file, and
`links` / `status` are skipped, because links only exist on a live task.

## Phase 8: the AI judge

```
python <skill>/scripts/calibrate_workshop.py run-judge --config workshop.json --wait
```

Runs every question's live judge version on every conversation and polls until done.
[docs](https://docs.calibrate.artpark.ai/api-reference/annotation-tasks/run-evaluators-on-items)
If the API key is refused, the person starts the run from the task page in the web app (select
all questions and all conversations). Run it after raters finish, so it uses the same final
wording; the export then has one `evaluator_<question>_v<N>` column per question.

## Changing questions after creation

```
python <skill>/scripts/calibrate_workshop.py update-evaluators --config workshop.json --dry-run --show-prompts
python <skill>/scripts/calibrate_workshop.py update-evaluators --config workshop.json
```

- Changed **options or judge instructions**: publishes a new live version for each changed question
  (API key is enough). [docs](https://docs.calibrate.artpark.ai/api-reference/evaluators/create-evaluator-version)
- Changed **question text** (`description`): the API key cannot edit it. The script lists which ones;
  the person edits them in the web app (Evaluators page). Do this before raters start.
- **Names** cannot be changed this way. Mid-workshop, keep them; for the next workshop, use a new
  prefix.

## What the API key can and can't do (as of Oct 2026)

| Action | API key | Otherwise |
|---|---|---|
| List or create questions, tasks, conversations; set optional questions | yes | |
| New judge version (prompt, options) | yes | |
| Edit a question's text or name | no | web app |
| Create raters, labeling jobs, AI judge runs | yes per public docs; job creation was refused on Noora's server in Sep 2026 | web app, then `links` |
| Read jobs and their links | yes | |
| Download the annotations | the export button on the task page | |
| `get-agreement` / `get-summary` | 404 on Noora's server in Oct 2026 | the dashboard computes agreement itself |

## Doing the same with Calibrate's CLI or MCP

For people on macOS or Linux who installed the CLI (see `setup.md`), the equivalents are below;
the MCP server exposes the same operations as tools
([tools list](https://docs.calibrate.artpark.ai/mcp/tools)). Prefer the Python helper for the
actual setup, because it builds the judge prompts, applies the prefix and keeps reruns safe.

| Helper command | CLI ([annotation-tasks](https://docs.calibrate.artpark.ai/cli/calibrate/annotation-tasks), [annotators](https://docs.calibrate.artpark.ai/cli/calibrate/annotators), [evaluators](https://docs.calibrate.artpark.ai/cli/calibrate/evaluators)) |
|---|---|
| `check` | `calibrate annotation-tasks list` |
| `create` | `calibrate evaluators create ...`, `calibrate annotation-tasks create --type conversation ...`, `set-evaluators --evaluator-ids ... --optional-evaluator-ids ...`, `add-items -t <task> -i items.json` |
| `annotators` | `calibrate annotators create --name asha` |
| `jobs` | `calibrate annotation-tasks create-labelling-jobs -t <task> -a <ids> --select-all` |
| `links`, `status` | `calibrate annotation-tasks get -t <task>` |
| `run-judge` | `calibrate annotation-tasks create-evaluator-run -t <task> -e <ids> --select-all`, then `get-evaluator-run` |
| `update-evaluators` | `calibrate evaluators create-version ... --make-live true` |

Any CLI command with `--dry-run` prints the exact request without sending it, which is the
quickest way to learn a request's shape on a server whose API description is not public.
