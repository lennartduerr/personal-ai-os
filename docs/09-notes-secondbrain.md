# 09 — Notes & the Second Brain Pipeline

> **Agent note:** Two layers, both optional, both offered separately:
> (1) the **notes skill** — the agent creates/reads documents; (2) the **Second Brain Pipeline** —
> those documents (and any others) get compiled into a queryable knowledge base. The pipeline is a
> headline, first-class part of this OS — present it with enthusiasm, but only install on a yes.

## Layer 1 — The notes skill

Lets the agent create and read documents on the VPS (md / txt / list / docx / pdf). Triggers like
"save this as a document", "make a report/analysis/list".

1. Install the scaffold:
   ```bash
   cp -r skills/notes ~/.hermes/custom-skills/notes
   mkdir -p ~/.hermes/hermes-notes
   sudo hermes gateway restart --system
   ```
2. Use it:
   ```bash
   ~/.hermes/custom-skills/notes/scripts/notes.py new --title "Trip plan" --format pdf --topic "vietnam-trip"
   ~/.hermes/custom-skills/notes/scripts/notes.py list
   ~/.hermes/custom-skills/notes/scripts/notes.py read --path "<path>"
   ~/.hermes/custom-skills/notes/scripts/notes.py append --path "<path>"   # markdown via stdin
   ```

Documents live under `~/.hermes/hermes-notes/`, one subfolder per topic. **The VPS is the single
source of truth** — always edit there, never a synced copy.

### Optional: mirror notes to a local folder (e.g. iCloud)

A one-way mirror (VPS → your machine → iCloud) gives you the documents in Finder/Files for free.
On macOS, a `launchd` job runs an `rsync` every few minutes. Template + plist:
[../templates/sync/](../templates/sync/). It's strictly one-way (VPS wins) so it never clobbers the
agent's edits.

---

## Layer 2 — The Second Brain Pipeline ⭐

> Repo: **https://github.com/lennartduerr/second-brain-pipeline** (MIT)

Drop **any** document into a folder (or hand it to the agent) and it's ingested into a clean
Markdown knowledge base. **No RAG, no chunking, no vector DB** — the compiled brain fits in a modern
context window, so the agent navigates an *index* instead of doing similarity search.

```
Input files → Parse → Extract → Compile → Lint → brain/  (Markdown your agent can read)
```

| Stage | What it does |
|-------|--------------|
| **Parse** | Documents → clean Markdown with a quality score (no LLM) |
| **Extract** | LLM pulls structured facts: entities, topics, references |
| **Compile** | Clusters related docs → canonical knowledge pages |
| **Lint** | Cross-checks pages for contradictions, gaps, staleness |

### Install

On the VPS (or wherever you want the brain to live):

```bash
git clone https://github.com/lennartduerr/second-brain-pipeline.git
cd second-brain-pipeline
./install.sh           # interactive: pick parse tier + LLM backend
# or, as a tool:  uv tool install second-brain-pipeline   (or: pipx install ...)
```

**Choices it asks about:**
- **LLM backend:** OpenRouter (`OPENROUTER_API_KEY`, good for unattended/cron) **or** the keyless
  local `claude` CLI (uses your Claude login).
- **Parse tier:** `lite` (pure Python, zero system deps) or `full` (adds Java OpenDataLoader +
  Tesseract OCR for scanned PDFs).

### Use

```bash
sbp ingest ~/Downloads/report.pdf     # parse → extract → compile → lint
sbp ingest ~/notes/                   # recursive folder ingest
sbp watch                             # auto-ingest dropped files
sbp status --json                     # brain state (great for the dashboard)
sbp lint                              # cross-check the whole brain
```

Output:
```
brain/
  index.md            # navigable topic index
  knowledge/          # canonical .md pages
  sources/            # parsed sources (provenance)
  .sbp/brain.db       # SQLite bookkeeping
```

### How it plugs into this OS

- **Notes → brain:** point `sbp` at `~/.hermes/hermes-notes/` (or `sbp watch` it) so everything the
  agent writes becomes queryable knowledge.
- **Mail/web → brain:** ingest saved attachments or research write-ups for a growing knowledge base.
- **Agent reads the brain:** because it's plain Markdown with an index, the agent can answer from
  `brain/index.md` + `brain/knowledge/` directly — no extra infrastructure.
- **Dashboard:** surface `sbp status --json` as an optional block ([11](11-dashboard-vercel.md)).

## Next step

[10-crons-briefing.md](10-crons-briefing.md) — the morning briefing.
