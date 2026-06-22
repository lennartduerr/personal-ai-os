#!/usr/bin/env python3
"""notes — create/read documents (md/txt/list/docx/pdf) under ~/.hermes/hermes-notes/.

SCAFFOLD: md/txt/list and the file ops work as-is; docx/pdf rendering is marked TODO
(install python-docx / reportlab).
"""
import argparse
import os
import re
import sys
from pathlib import Path

ROOT = Path(os.environ.get("NOTES_ROOT", Path.home() / ".hermes" / "hermes-notes"))


def _slug(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-") or "untitled"


def _topic_dir(topic: str) -> Path:
    d = ROOT / _slug(topic)
    d.mkdir(parents=True, exist_ok=True)
    return d


def new(title, fmt, topic):
    d = _topic_dir(topic)
    base = _slug(title)
    body = sys.stdin.read() if not sys.stdin.isatty() else f"# {title}\n\n"
    if fmt in ("md", "txt", "list"):
        ext = "md" if fmt == "md" else ("txt" if fmt == "txt" else "md")
        path = d / f"{base}.{ext}"
        path.write_text(body, encoding="utf-8")
    elif fmt == "docx":
        path = d / f"{base}.docx"
        # TODO: render Markdown `body` to a .docx with python-docx.
        raise NotImplementedError("TODO: docx rendering (python-docx).")
    elif fmt == "pdf":
        path = d / f"{base}.pdf"
        # TODO: render Markdown `body` to a .pdf with reportlab.
        raise NotImplementedError("TODO: pdf rendering (reportlab).")
    else:
        sys.exit(f"Unknown format: {fmt}")
    print(path)


def list_notes(folder):
    base = _topic_dir(folder) if folder else ROOT
    for p in sorted(base.rglob("*")):
        if p.is_file():
            print(p.relative_to(ROOT))


def list_folders():
    ROOT.mkdir(parents=True, exist_ok=True)
    for p in sorted(ROOT.iterdir()):
        if p.is_dir():
            print(p.name)


def read(path):
    p = Path(path)
    if not p.is_absolute():
        p = ROOT / path
    if not p.exists():
        sys.exit(f"Not found: {p}")
    print(p.read_text(encoding="utf-8", errors="replace"))


def append(path):
    p = Path(path)
    if not p.is_absolute():
        p = ROOT / path
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open("a", encoding="utf-8") as f:
        f.write("\n" + sys.stdin.read())
    print(p)


def main():
    ap = argparse.ArgumentParser(description="notes skill")
    sub = ap.add_subparsers(dest="cmd", required=True)

    pn = sub.add_parser("new")
    pn.add_argument("--title", required=True)
    pn.add_argument("--format", default="md", choices=["md", "txt", "list", "docx", "pdf"])
    pn.add_argument("--topic", required=True)

    pl = sub.add_parser("list")
    pl.add_argument("--folder", default=None)

    sub.add_parser("list-folders")

    pr = sub.add_parser("read")
    pr.add_argument("--path", required=True)

    pa = sub.add_parser("append")
    pa.add_argument("--path", required=True)

    args = ap.parse_args()
    if args.cmd == "new":
        new(args.title, args.format, args.topic)
    elif args.cmd == "list":
        list_notes(args.folder)
    elif args.cmd == "list-folders":
        list_folders()
    elif args.cmd == "read":
        read(args.path)
    elif args.cmd == "append":
        append(args.path)


if __name__ == "__main__":
    main()
