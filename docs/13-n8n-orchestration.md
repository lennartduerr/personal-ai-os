# 13 — Workflow automation via n8n (advanced & optional)

> **Agent note:** **Skip this unless the user actively uses [n8n](https://n8n.io).** Most people
> installing this OS don't know or use n8n — don't bring it up proactively. Only offer it at the
> very end, and only if the user mentions n8n or workflow automation. This page is a pointer, not a
> core phase.

If — and only if — you already run n8n, you can give your agent (and Claude Code on the VPS) direct,
structured access to it. The clean way to do that today is the **n8n-MCP server**, which exposes
n8n as MCP tools (search nodes, validate configs, manage and run workflows) that Claude Code and
MCP-aware agents can call.

- **n8n-MCP server:** https://github.com/czlonkowski/n8n-mcp
- **n8n skills (for Claude Code):** https://github.com/czlonkowski/n8n-skills

## Get your n8n API key

In your n8n instance: **Settings → n8n API → Create API Key** (the **JSON**/API access section).
Note the API key and your instance's API URL (e.g. `https://n8n.example.com/api/v1`).

## Two ways to connect

**A) n8n-MCP server (recommended for agents/Claude Code).**
Run the n8n-MCP server pointed at your instance (follow its README), giving it your n8n API URL +
key. Then Claude Code on the VPS — or the agent via MCP — can search nodes, validate workflows, and
create/trigger them. Pair it with the [n8n-skills](https://github.com/czlonkowski/n8n-skills) for
ready-made Claude Code skills.

**B) Claude Code on the VPS terminal.**
Since Claude Code already runs on the VPS for self-improvement ([12](12-self-improve.md)), it can
call the n8n REST API directly with your key to build and manage workflows from the terminal.

## What you can do with it

- Let n8n handle deterministic plumbing (triggers, schedules, integrations) while the agent handles
  reasoning (summarize, decide, draft) — calling back and forth.
- Have Claude Code compose and deploy n8n workflows on request.
- Optional: a daily n8n health-check cron (template: [../templates/crons/n8n-check.md](../templates/crons/n8n-check.md)).

> This is a project in itself. Scope one concrete workflow with the user first and build
> incrementally. n8n self-hosts (Docker) or runs on n8n Cloud.

## Next step

[14-security.md](14-security.md).
