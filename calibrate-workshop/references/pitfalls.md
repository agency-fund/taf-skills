# Pitfalls

Each of these cost real time in an earlier workshop. Symptom first, then cause and fix.

## Calibrate

| Symptom | Cause | Fix |
|---|---|---|
| Every call returns 401 although the key is new | The key belongs to a different Calibrate server (hosted vs self-hosted) | Set `calibrate.api_url` to the API address of the server where the key was made |
| A conversation shows as a single "—" in Calibrate; descriptions still show | A transcript role other than `user` / `assistant` (for example "MSE") | Speaker names go in the message text; `build_items.py` already does this |
| Time tags don't appear | `created_at` has microseconds or a zone suffix | Bare `YYYY-MM-DD HH:MM:SS`; convert the zone before upload (`data.display_timezone`) |
| `create` "reuses" questions you meant to be new; old wording appears | An evaluator with the same name exists (same prefix as an earlier workshop) | New `workshop.prefix` per workshop |
| Need more than two named answers | Calibrate has only `binary` and `rating` | `rating` with a named `scale` |
| A question became required again | Optional flags are set as one whole set per task | Mark it in `evaluators.json` and run `create --update` (never set flags one by one) |
| Can't rename a question or change its text from a script | The API key can't edit evaluators (403) | Web app for text; names are permanent, so choose them once |
| Job creation 403 | Some servers don't let the API key create labeling jobs | Create jobs in the web app, then `calibrate_workshop.py links` |
| `get-agreement` / `get-summary` return 404 | Not available on that server version | The dashboard computes agreement from the export |
| No machine-readable API description on a self-hosted server (`/openapi.json` 401) | Not exposed there | The public spec at https://docs.calibrate.artpark.ai/api-reference/openapi.json, or `calibrate <command> --dry-run` to see a request |
| `calibrate whoami` says fine but calls fail | `whoami` never contacts the server | Check with `calibrate annotation-tasks list` or `calibrate_workshop.py check` |
| CLI talks to the wrong server after login | `configure --server-url` was run after `login` | Run `configure` first, then log in again |

## Data and items

| Symptom | Cause | Fix |
|---|---|---|
| A "None" in a message or the panel | A missing value passed through as Python's None | The validator fails the build; empty values become `NA` |
| Validator flags the English word "None" in a sentence | An over-eager check (fixed) | The check only matches None as a whole field |
| Translation left a few rows empty | Transient network errors | `translate.py --resume --confirm-send`, then `--verify` |
| A filter removed nothing you expected | Duplicates or images were in conversations the language filter had already dropped | Read the per-filter counts `make_sample.py` prints |
| Long numeric ids change (1.2e+18) | A spreadsheet or a type-guessing reader | Scripts read every column as text; don't round-trip the export through Excel |
| Rubric says "MSE", transcripts say AGENT | Speaker labels changed between rounds, the rubric didn't | Decide on purpose; match them if you can |

## Dashboard and hosting

| Symptom | Cause | Fix |
|---|---|---|
| Ratings show as numbers (1, 2) or don't match | Wrong `evaluators.json` (names or values differ from the task) | Use the exact spec the task was created from |
| Vercel stuck on "Building" forever | Deployment **blocked**: the CLI attached a git commit author whose email isn't the Vercel account's | `deploy_vercel.py` uploads from a temporary folder outside git |
| Vercel CLI hangs | It's waiting for an interactive answer | The script runs it non-interactively (`CI=1`, `--yes`, no stdin) |
| Password page sits above the dashboard after unlocking | Old unlock code used `document.write` while the page was loading | Fixed in the template (whole-document swap) |
| Everyone logged out after redeploy | The salt changed | Keep `out/.salt`; only `--rotate-salt` changes it |
| An old unencrypted version is still reachable | Each Vercel deployment keeps its own address | Delete old deployments in the Vercel dashboard |

## Machine and tools

| Symptom | Cause | Fix |
|---|---|---|
| Python script dies silently or "Illegal instruction" at the first group-by (Mac) | An Intel Python under Rosetta; polars needs CPU features it lacks | Use a native arm64 Python (`platform.machine()` = `arm64`) |
| `ZoneInfoNotFoundError` on Windows | No time zone database | `pip install tzdata` (in requirements.txt) |
| Garbled characters or a crash printing on Windows | Console code page | Scripts switch output to UTF-8; use Windows Terminal |
| `git push` hangs with no output (inside an IDE) | The IDE's password prompt never appears | `gh auth setup-git`; run with `GIT_TERMINAL_PROMPT=0` to fail fast |
| `brew tap` fails with "unknown option end-of-options" | An old git earlier on PATH | Put Homebrew's bin first on PATH |
| Claude refuses to fetch annotations or search Downloads | A permission or safety check on sensitive data | The person does that step by hand (export, then save into `out/`) |
