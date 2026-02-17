#!/usr/bin/env python3
"""CLI-based tool execution wrappers for reproducible black-box runs.

We use OpenClaw CLI as the stable interface because in-session tools may be unreliable.
All outputs are JSON (when possible) for oracle parsing.
"""

from __future__ import annotations

import json
import shlex
import subprocess
from dataclasses import dataclass
from typing import Optional, Dict, Any, List


@dataclass
class CmdResult:
    ok: bool
    cmd: List[str]
    stdout: str
    stderr: str
    returncode: int
    json: Optional[Dict[str, Any]] = None


def run(cmd: List[str], timeout_s: int = 60) -> CmdResult:
    p = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout_s)
    out = p.stdout.strip()
    err = p.stderr.strip()
    j = None
    # best-effort JSON parse
    try:
        if out.startswith('{') and out.endswith('}'):
            j = json.loads(out)
    except Exception:
        j = None
    return CmdResult(ok=(p.returncode == 0), cmd=cmd, stdout=out, stderr=err, returncode=p.returncode, json=j)


def telegram_send(target_chat_id: str, message: str, verbose: bool = False) -> CmdResult:
    cmd = [
        "openclaw", "message", "send",
        "--channel", "telegram",
        "--target", str(target_chat_id),
        "--message", message,
    ]
    if verbose:
        cmd.append("--verbose")
    return run(cmd, timeout_s=60)


def cron_add_one_shot_main(name: str, in_minutes: int, text: str, delete_after_run: bool = True) -> CmdResult:
    cmd = [
        "openclaw", "cron", "add",
        "--name", name,
        "--session", "main",
        "--at", f"{in_minutes}m",
        "--system-event", text,
        "--json",
    ]
    if delete_after_run:
        cmd.append("--delete-after-run")
    return run(cmd, timeout_s=60)


def cron_add_recurring_main(name: str, every: str, text: str) -> CmdResult:
    cmd = [
        "openclaw", "cron", "add",
        "--name", name,
        "--session", "main",
        "--every", every,
        "--system-event", text,
        "--json",
    ]
    return run(cmd, timeout_s=60)
