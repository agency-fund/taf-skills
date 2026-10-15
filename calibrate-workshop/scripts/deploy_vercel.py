"""Publish the ENCRYPTED dashboard to a free Vercel (Hobby) project. Optional step.

Only the password page made by encrypt_dashboard.py is ever uploaded; the script refuses anything
else. Needs Node.js (for npx) and a Vercel account you are logged in to (`npx vercel login`).

    python deploy_vercel.py --config workshop.json --create my-workshop-review-7f3a
    python deploy_vercel.py --config workshop.json            # later redeploys

--create makes the Vercel project and links the deploy folder to it. Pick a name nobody would
guess: the site lives at https://<name>.vercel.app.

Why the upload runs from a temporary folder: the Vercel CLI attaches the enclosing git repo's
latest commit author to each deployment, and the free plan BLOCKS deployments whose author email
is not the Vercel account's (the dashboard then shows an endless "Building"). Copying the two
files outside any git repo avoids that.
"""

from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
import tempfile
import urllib.request
from pathlib import Path

from workshop_config import add_config_arg, load_config, utf8_console

HERE = Path(__file__).resolve().parent
GUARD_TEXT = "Enter the workshop password"
PLAINTEXT_MARKERS = ('id="data"', '"conversation_history"', '"transcript"')


def npx() -> str:
    found = shutil.which("npx") or shutil.which("npx.cmd")
    if not found:
        raise SystemExit("npx not found. Install Node.js (https://nodejs.org, LTS) and open a new terminal.")
    return found


def vercel(args: list[str], cwd: Path) -> subprocess.CompletedProcess:
    env = dict(os.environ, CI="1", VERCEL_TELEMETRY_DISABLED="1")
    return subprocess.run([npx(), "--yes", "vercel@latest", *args], cwd=cwd, env=env,
                          stdin=subprocess.DEVNULL, text=True, capture_output=True)


def inside_git(folder: Path) -> bool:
    git = shutil.which("git")
    if not git:
        return False
    result = subprocess.run([git, "-C", str(folder), "rev-parse", "--is-inside-work-tree"], capture_output=True, text=True)
    return result.returncode == 0


def create_project(name: str, deploy_dir: Path, scope: str | None) -> None:
    extra = ["--scope", scope] if scope else []
    result = vercel(["project", "add", name, *extra], cwd=Path(tempfile.gettempdir()))
    if result.returncode != 0 and "already exists" not in (result.stdout + result.stderr):
        raise SystemExit(f"Could not create the Vercel project:\n{result.stderr or result.stdout}")
    with tempfile.TemporaryDirectory() as scratch:
        result = vercel(["link", "--yes", "--project", name, *extra], cwd=Path(scratch))
        if result.returncode != 0:
            raise SystemExit(f"Could not link the project (are you logged in? run: npx vercel login):\n{result.stderr or result.stdout}")
        deploy_dir.mkdir(parents=True, exist_ok=True)
        shutil.rmtree(deploy_dir / ".vercel", ignore_errors=True)
        shutil.copytree(Path(scratch) / ".vercel", deploy_dir / ".vercel")
    print(f"Linked {deploy_dir} to Vercel project {name}.")


def main() -> int:
    utf8_console()
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    add_config_arg(ap)
    ap.add_argument("--create", metavar="PROJECT_NAME", default=None, help="Create and link a new Vercel project first.")
    ap.add_argument("--scope", default=None, help="Vercel team slug, if the project belongs to a team.")
    args = ap.parse_args()
    cfg = load_config(args.config)

    deploy_dir = cfg.path("dashboard.deploy_dir")
    if args.create:
        create_project(args.create, deploy_dir, args.scope)
    project_file = deploy_dir / ".vercel" / "project.json"
    if not project_file.exists():
        raise SystemExit(f"{deploy_dir} is not linked to a Vercel project yet. Re-run with --create <project-name>.")
    page = deploy_dir / "index.html"
    if not page.exists():
        raise SystemExit(f"{page} not found. Run encrypt_dashboard.py first.")
    text = page.read_text(encoding="utf-8")
    if GUARD_TEXT not in text or any(marker in text for marker in PLAINTEXT_MARKERS):
        raise SystemExit(f"{page} is not the encrypted password page; refusing to upload.")

    with tempfile.TemporaryDirectory() as stage_name:
        stage = Path(stage_name)
        if inside_git(stage):
            raise SystemExit(f"Temporary folder {stage} is inside a git repo; Vercel would block the upload.")
        shutil.copy2(page, stage / "index.html")
        shutil.copy2(HERE.parent / "assets" / "vercel.json", stage / "vercel.json")
        shutil.copytree(deploy_dir / ".vercel", stage / ".vercel")
        print("Uploading the encrypted page to Vercel ...")
        result = vercel(["deploy", "--prod", "--yes", "--no-color"], cwd=stage)
        if result.returncode != 0:
            raise SystemExit(f"Deploy failed:\n{result.stderr or result.stdout}")

    project = json.loads(project_file.read_text(encoding="utf-8"))
    name = project.get("projectName") or deploy_dir.name
    url = f"https://{name}.vercel.app/"
    try:
        with urllib.request.urlopen(url, timeout=30) as response:
            live = response.read().decode("utf-8", "replace")
        ok = GUARD_TEXT in live
        print(f"Live: {url}  ({'password page served' if ok else 'WARNING: unexpected content'})")
    except Exception as exc:
        print(f"Deployed. Check {url} in a minute ({exc}).")
    print("Share the link and the password through different channels.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
