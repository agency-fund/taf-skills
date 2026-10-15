# Setup

Everything a machine needs before the first workshop, then the workshop folder itself. Do it in
this order; each step says how to check it worked.

## 1. Claude Code

Install: https://code.claude.com/docs/en/setup (macOS, Windows and Linux; quickstart at
https://code.claude.com/docs/en/quickstart). The person signs in with their Claude account.

## 2. This skill

From a terminal (needs Node.js for `npx`, see step 7, or use the manual route):

```
npx skills add agency-fund/taf-skills --skill calibrate-workshop -a claude-code -g
```

`-g` installs it for every project (into `~/.claude/skills/`); leave it off to install into the
current project only (`./.claude/skills/`). Update later with `npx skills update calibrate-workshop`.
Tool docs: https://github.com/vercel-labs/skills

Manual route: download https://github.com/agency-fund/taf-skills, copy the `calibrate-workshop`
folder into `~/.claude/skills/` (Windows: `%USERPROFILE%\.claude\skills\`).

Check: start `claude`, type `/` and look for `calibrate-workshop`. How skills work:
https://code.claude.com/docs/en/skills

The skill runs local scripts against the person's files and API keys, so it needs Claude Code,
not the claude.ai chat.

## 3. Python 3.10 or newer, and the packages

The scripts use polars (data), requests (Calibrate), python-dotenv (keys), cryptography
(dashboard password), openai (translation only) and tzdata (time zones on Windows).

macOS:
```
python3 --version                       # 3.10+? If not: https://www.python.org/downloads/
python3 -m venv ~/.venvs/calibrate-workshop
source ~/.venvs/calibrate-workshop/bin/activate
pip install -r ~/.claude/skills/calibrate-workshop/scripts/requirements.txt
```

Windows (PowerShell):
```
py --version                            # 3.10+? If not: https://www.python.org/downloads/ (tick "Add to PATH")
py -m venv $HOME\.venvs\calibrate-workshop
$HOME\.venvs\calibrate-workshop\Scripts\Activate.ps1
pip install -r $HOME\.claude\skills\calibrate-workshop\scripts\requirements.txt
```

Alternative for either: `uv` (https://docs.astral.sh/uv/getting-started/installation/), then
`uv venv` and `uv pip install -r .../requirements.txt`.

Check: `python -c "import polars, requests, cryptography; print('ok')"`.

Use the same interpreter for every script. On an Apple Silicon Mac, make sure it is a native
(arm64) Python: an Intel build running under Rosetta makes polars crash without an error message
(`python -c "import platform; print(platform.machine())"` should print `arm64`).

## 4. Calibrate account, server and API key

1. Get invited to the right Calibrate workspace (organisation). Noora Health staff: ask your TAF
   contact for an invite to **TAF | Noora Health** on Noora's server (see `noora-profile.md`).
2. Know which server you are on. There are two kinds:
   - Calibrate's hosted service: web app `https://calibrate.artpark.ai`, API `https://api.calibrate.artpark.ai`
   - a self-hosted copy with its own web and API addresses (Noora's is one).
   Put both addresses in `workshop.json` under `calibrate.web_url` and `calibrate.api_url`. The
   API address is the one the scripts talk to; never put the web address there.
3. Create an API key in the web app: Workspace settings, API keys, Create key. It is shown once.
   Docs: https://docs.calibrate.artpark.ai/reference/api-keys
4. The person pastes it into the workshop folder's `.env` themselves:
   ```
   CALIBRATE_API_KEY=...
   ```

Check: `python <skill>/scripts/calibrate_workshop.py check --config workshop.json` prints
"Key works". A 401 almost always means the key belongs to the other server.

## 5. Optional: Calibrate's own command-line tool and MCP server

Not needed for this skill (the Python helper covers every step on every OS), but handy for
looking things up.

- **CLI** (macOS and Linux, via Homebrew): `brew install dalmia/tap/calibrate`. For a self-hosted
  server, set the address *before* logging in:
  `calibrate configure --no-interactive --server-url <api address>`, then `calibrate login`
  (newer versions: `calibrate auth login`). Check with `calibrate annotation-tasks list`
  (`whoami` does not contact the server). Docs: https://docs.calibrate.artpark.ai/cli/calibrate/overview,
  source https://github.com/dalmia/calibrate-cli. Add `--dry-run` to any command to see the exact
  request without sending it.
- **MCP server**, so Claude can call Calibrate as tools (any OS, needs Node.js):
  hosted service:
  `claude mcp add --transport http calibrate https://mcp.calibrate.artpark.ai/mcp --header "X-API-Key: <key>"`;
  self-hosted (not in the official docs; uses the local server's `--server-url` flag):
  `claude mcp add calibrate -- npx -y @dalmia/calibrate-mcp start --api-key-auth <key> --server-url <api address>`.
  Either way the key is stored in Claude Code's config file, so only do this on a personal
  machine. Docs: https://docs.calibrate.artpark.ai/mcp/installation, https://code.claude.com/docs/en/mcp
- **Calibrate's own skills** (agent testing, judge tuning against human labels):
  `npx skills add dalmia/calibrate-skills -a claude-code -g`. Docs:
  https://docs.calibrate.artpark.ai/agents/skills. Their `calibrate-evaluator` skill is useful
  after a workshop, for tuning an AI judge against the human labels.

## 6. Optional: OpenAI key (translation only)

Create a key at https://platform.openai.com/api-keys and add `OPENAI_API_KEY=...` to `.env`. Only
needed if messages must be translated and the data owner has agreed to send them to OpenAI.

## 7. Optional: Google Drive connector, Node.js, Vercel

- **Google Drive connector**, so Claude can turn the links file into a Google Sheet: connect
  Google Drive in claude.ai under Settings, Connectors. Connectors on the person's account are
  also available in Claude Code. Docs:
  https://support.claude.com/en/articles/10166901-use-google-workspace-connectors and
  https://support.claude.com/en/articles/11176164-use-connectors-to-extend-claude-s-capabilities.
  Without it, the person imports `out/annotator_links.csv` into a Sheet by hand.
- **Node.js** (https://nodejs.org/en/download, LTS): for `npx skills`, the MCP server and Vercel.
- **Vercel** (https://vercel.com, free Hobby plan) only to host the encrypted dashboard. Log in
  once with `npx vercel login`. See `dashboard.md`.

## 8. The workshop folder

One folder per workshop. Keep it out of any shared git repository; a private or team-restricted
synced folder is fine. Claude creates it with the person:

```
<workshop>/
  workshop.json      settings. Start from assets/workshop.noora-*.json or scripts/workshop.example.json
  evaluators.json    the rubric. Start from the last workshop, assets/evaluators.noora-rubric.json or assets/evaluators.starter.json
  .env               keys, typed in by the person
  .gitignore         see below
  progress.md        one line per finished phase, for resuming
  data/              the export, the sample, the translation
  out/               items.json, task_ids.json, annotator_links.csv, annotations_export.csv, dashboard.html, site/
```

`.gitignore`:
```
.env
data/
out/
*.csv
```

`progress.md` starts as:
```
# <workshop name>
- <date> setup: folder created, Calibrate key works (server <api address>)
```

All relative paths in `workshop.json` are relative to the folder `workshop.json` is in.
