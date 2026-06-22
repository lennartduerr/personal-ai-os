# skills/ — custom skill scaffolds

These are **generalized scaffolds**, not finished products — clean starting points the installing
agent copies onto the VPS and fills in. Each folder has:

- `SKILL.md` — what the skill does + the commands it exposes (agent-facing description).
- `scripts/*.py` — a script skeleton with `# TODO:` markers where credentials/IDs go.

## How custom skills work in Hermes

Skills live in a directory registered via `skills.external_dirs` in `~/.hermes/config.yaml`:

```yaml
skills:
  external_dirs:
    - /home/hermes/.hermes/custom-skills
```

To install one:

```bash
cp -r skills/<name> ~/.hermes/custom-skills/<name>
# fill in credentials in ~/.hermes/.env (and any *.json/*.pass files)
sudo hermes gateway restart --system
# test the script directly:
~/.hermes/custom-skills/<name>/scripts/<name>.py --help
```

> **Verify the manifest format** against the Hermes repo
> (https://github.com/nousresearch/hermes-agent) — the `SKILL.md` frontmatter here uses a common
> `name` + `description` convention; adjust if the installed Hermes version expects something else.

## Available scaffolds

| Folder | Purpose | Docs |
|--------|---------|------|
| [`calendar-caldav/`](calendar-caldav/) | calendar via CalDAV (Apple iCloud example) | [docs/06](../docs/06-calendar-tasks.md) |
| [`tasks-google/`](tasks-google/) | to-dos/reminders via Google Tasks | [docs/06](../docs/06-calendar-tasks.md) |
| [`mail-himalaya/`](mail-himalaya/) | email read/tidy via himalaya (+ Brevo relay notes) | [docs/07](../docs/07-mail.md) |
| [`notes/`](notes/) | create/read documents (md/txt/list/docx/pdf) | [docs/09](../docs/09-notes-secondbrain.md) |
| [`youtube/`](youtube/) | YouTube transcripts (+ Apify fallback) | [docs/08](../docs/08-web-internet.md) |

Secrets never live in these files — they're read from `~/.hermes/.env` or chmod-600 files at runtime.
