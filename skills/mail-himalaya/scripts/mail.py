#!/usr/bin/env python3
"""mail-himalaya — thin wrapper over the himalaya CLI (read/search/move).

SCAFFOLD: shells out to `himalaya`. Adjust subcommands/flags to your installed himalaya version
(`himalaya --help`). Read-mostly by design — no send command is exposed here on purpose.
"""
import argparse
import shutil
import subprocess
import sys


def _himalaya(*args):
    exe = shutil.which("himalaya")
    if not exe:
        sys.exit("himalaya not found on PATH. See docs/07-mail.md.")
    return subprocess.run([exe, *args], check=False)


def list_mail(account, folder):
    args = ["envelope", "list"]
    if account:
        args += ["-a", account]
    if folder:
        args += ["-f", folder]
    _himalaya(*args)


def read_mail(msg_id, account):
    args = ["message", "read", msg_id]
    if account:
        args += ["-a", account]
    _himalaya(*args)


def move_mail(msg_id, to, account):
    # TODO: confirm the move/copy subcommand for your himalaya version.
    args = ["message", "move", msg_id, to]
    if account:
        args += ["-a", account]
    _himalaya(*args)


def main():
    ap = argparse.ArgumentParser(description="himalaya mail wrapper (read-mostly)")
    sub = ap.add_subparsers(dest="cmd", required=True)

    pl = sub.add_parser("list")
    pl.add_argument("--account", default=None)
    pl.add_argument("--folder", default=None)

    pr = sub.add_parser("read")
    pr.add_argument("--id", required=True)
    pr.add_argument("--account", default=None)

    pm = sub.add_parser("move")
    pm.add_argument("--id", required=True)
    pm.add_argument("--to", required=True)
    pm.add_argument("--account", default=None)

    args = ap.parse_args()
    if args.cmd == "list":
        list_mail(args.account, args.folder)
    elif args.cmd == "read":
        read_mail(args.id, args.account)
    elif args.cmd == "move":
        move_mail(args.id, args.to, args.account)


if __name__ == "__main__":
    main()
