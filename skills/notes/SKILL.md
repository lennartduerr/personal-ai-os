---
name: notes
description: Create and read documents (md/txt/list/docx/pdf) on the VPS. Use for "save this as a
  document", "write a report/analysis/list", "append to the X doc". One subfolder per topic.
---

# notes

The agent's document store. Content is written as Markdown; `docx`/`pdf` are rendered from it.
Documents live under `~/.hermes/hermes-notes/`, one subfolder per topic. The VPS is the single
source of truth (optionally mirrored locally — see templates/sync/).

## Setup
- `pip install python-docx reportlab` for docx/pdf output.
- See [docs/09](../../docs/09-notes-secondbrain.md).

## Commands
```
notes.py new --title T --format {md|txt|list|docx|pdf} --topic TOPIC
notes.py list [--folder TOPIC]
notes.py list-folders
notes.py read --path PATH
notes.py append --path PATH        # reads Markdown from stdin
```
