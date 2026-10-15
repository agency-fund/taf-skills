"""Wrap the dashboard in a password page so it can sit on a public static host.

The dashboard is encrypted with AES-256-GCM under a key derived from the password
(PBKDF2-HMAC-SHA256, 600,000 iterations). The output is one HTML page that asks for the password
and decrypts in the browser. The host only ever stores ciphertext.

The password comes from the DASHBOARD_PASSWORD environment variable or a prompt. It is never
written to disk; do not put it in workshop.json, .env or anything that could be committed.

    python encrypt_dashboard.py --config workshop.json          # prompts for the password
    python encrypt_dashboard.py --config workshop.json --rotate-salt   # logs out remembered devices

The salt is kept in dashboard.salt_file so a device that ticked "remember" keeps working after a
redeploy. The salt is public by design (it ships inside the page); only the password is secret.
"""

from __future__ import annotations

import argparse
import base64
import getpass
import hashlib
import html
import json
import os
import secrets
import sys
from pathlib import Path

from workshop_config import add_config_arg, load_config, utf8_console

HERE = Path(__file__).resolve().parent
ITERATIONS = 600_000
MIN_PASSWORD_LENGTH = 10
GUARD_TEXT = "Enter the workshop password"


def b64(data: bytes) -> str:
    return base64.b64encode(data).decode("ascii")


def load_salt(path: Path, rotate: bool) -> bytes:
    if path.exists() and not rotate:
        return base64.b64decode(path.read_text().strip())
    salt = secrets.token_bytes(16)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(b64(salt) + "\n")
    return salt


def encrypt(page: str, password: str, salt: bytes) -> dict:
    from cryptography.hazmat.primitives.ciphers.aead import AESGCM

    iv = secrets.token_bytes(12)
    key = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt, ITERATIONS, dklen=32)
    ciphertext = AESGCM(key).encrypt(iv, page.encode("utf-8"), None)
    if AESGCM(key).decrypt(iv, ciphertext, None).decode("utf-8") != page:
        raise SystemExit("round-trip decryption failed")
    return {"v": 1, "kdf": "PBKDF2-SHA256", "cipher": "AES-256-GCM", "iterations": ITERATIONS,
            "salt": b64(salt), "iv": b64(iv), "ct": b64(ciphertext)}


def main() -> int:
    utf8_console()
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    add_config_arg(ap)
    ap.add_argument("--in", dest="inp", type=Path, default=None, help="Default: dashboard.out_html.")
    ap.add_argument("--out", type=Path, default=None, help="Default: <dashboard.deploy_dir>/index.html.")
    ap.add_argument("--rotate-salt", action="store_true", help="New salt: every remembered device must log in again.")
    args = ap.parse_args()
    cfg = load_config(args.config)

    inp = args.inp or cfg.path("dashboard.out_html")
    out = args.out or (cfg.path("dashboard.deploy_dir") / "index.html")
    if not inp.exists():
        raise SystemExit(f"Dashboard not found: {inp}. Run build_dashboard.py first.")
    password = os.environ.get("DASHBOARD_PASSWORD") or getpass.getpass("Dashboard password: ")
    if len(password) < MIN_PASSWORD_LENGTH:
        raise SystemExit(f"Use a password of at least {MIN_PASSWORD_LENGTH} characters (a short phrase works well).")

    title = cfg.get("dashboard.title") or f"{cfg.get('workshop.name') or 'Workshop'} Agreement Review"
    template = (HERE / "unlock_template.html").read_text(encoding="utf-8")
    template = (
        template.replace("__TITLE__", html.escape(title))
        .replace("__EYEBROW__", html.escape(cfg.get("dashboard.eyebrow") or cfg.get("workshop.name") or "Labeling workshop"))
        .replace("__STORE__", f"{cfg.slug}-review-key")
    )
    payload = encrypt(inp.read_text(encoding="utf-8"), password, load_salt(cfg.path("dashboard.salt_file"), args.rotate_salt))
    page = template.replace("/*__PAYLOAD__*/", json.dumps(payload))
    if GUARD_TEXT not in page:
        raise SystemExit("unlock template lost its password prompt; refusing to write")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(page, encoding="utf-8")
    print(f"Wrote {out} ({len(page) / 1024:.0f} KB): encrypted, opens with the password.")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        sys.exit(1)
