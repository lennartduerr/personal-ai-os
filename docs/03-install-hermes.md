# 03 — Install the Hermes agent

> **Agent note:** The **official Hermes repo is the source of truth** for install commands:
> **https://github.com/nousresearch/hermes-agent**. Always check its README first — flags and
> script paths can change. The steps below describe the *shape* of a working install and what you
> end up with; verify the exact command against the repo before running it. Back up any file before
> editing it (`cp f f.bak.$(date +%s)`).

Hermes (by [NousResearch](https://github.com/NousResearch)) is the agent at the core of this OS:
an LLM-driven assistant with a **skill** system, a **gateway** that connects chat platforms, and a
**cron** scheduler. We install it for the `hermes` user under `~/.hermes/`.

---

## Step 1 — Install

SSH into the VPS as `hermes`, then follow the install method from the official repo
(**https://github.com/nousresearch/hermes-agent#install**). It is typically one of:

```bash
# Option A — one-line installer (check the repo README for the current URL)
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/install.sh | bash

# Option B — manual git install
git clone https://github.com/nousresearch/hermes-agent ~/.hermes/hermes-agent
cd ~/.hermes/hermes-agent
python3 -m venv ~/.hermes/venv
~/.hermes/venv/bin/pip install -e .
```

After install you should have:
- the `hermes` binary on your `PATH` (commonly `~/.local/bin/hermes`),
- a config dir at `~/.hermes/`.

Reload your shell (`source ~/.bashrc`) and verify:

```bash
hermes --version
hermes --help
```

> If `hermes` isn't found, add its location to `PATH` (e.g. `export PATH="$HOME/.local/bin:$PATH"`
> in `~/.bashrc`).

---

## Step 2 — First-time configuration

Run the setup/wizard if the repo provides one (`hermes setup` or similar — see its README), or
create the config files from this repo's templates:

```bash
mkdir -p ~/.hermes/custom-skills ~/.hermes/scripts ~/.hermes/hermes-notes
# Copy templates from this repo (adjust the source path to where you cloned personal-ai-os)
cp templates/config.yaml.example          ~/.hermes/config.yaml
cp templates/SOUL.md.example              ~/.hermes/SOUL.md
cp templates/hermes-CLAUDE.md.example     ~/.hermes/CLAUDE.md
mkdir -p ~/.hermes/.claude
cp templates/claude-settings.json.example ~/.hermes/.claude/settings.json
```

Then create the secrets file and lock it down:

```bash
cp .env.example ~/.hermes/.env
chmod 600 ~/.hermes/.env
nano ~/.hermes/.env       # fill in the keys for the components you chose
```

Key files (templates in [`../templates/`](../templates/)):

| File | Purpose |
|------|---------|
| `~/.hermes/config.yaml` | model, model aliases, vision, `skills.external_dirs`, approvals, display |
| `~/.hermes/.env` | secrets (chmod 600, never committed) |
| `~/.hermes/SOUL.md` | persona, rules, your personal facts (home location, preferences) |
| `~/.hermes/CLAUDE.md` | guardrails for the on-VPS self-improve loop (phase 12) |
| `~/.hermes/.claude/settings.json` | permission deny-list protecting secrets |

We'll set the actual LLM in the next phase ([04-llm-deepseek.md](04-llm-deepseek.md)).

---

## Step 3 — Smoke test (no gateway yet)

The fastest way to confirm the agent + LLM work is a one-shot prompt:

```bash
hermes -z "Say hello in one short sentence."
```

If that returns a sensible reply, the core is alive. (If it errors about the model/key, finish
[04-llm-deepseek.md](04-llm-deepseek.md) first.)

---

## Step 4 — Run it 24/7 as a service

The **gateway** is the long-running process that connects your chat channels. Install it as a
`systemd` service so it survives reboots (exact command per the repo README):

```bash
# Typically:
hermes gateway install --system --run-as-user hermes
sudo hermes gateway start --system
sudo hermes gateway status --system
```

Manage it with:

```bash
sudo hermes gateway {start|stop|restart|status} --system
sudo journalctl -u hermes-gateway -f      # live logs
```

> **Always restart the gateway after changing config, skills, or code:**
> `sudo hermes gateway restart --system`.

You won't have a channel to talk to yet — set up Telegram/Slack in
[05-channels.md](05-channels.md), which is the recommended next step so you get a working chat loop
early.

---

## What you have now

- Hermes installed under `~/.hermes/`, binary on PATH
- Config, persona, secrets, and guardrail files in place (from templates)
- A passing `hermes -z` smoke test
- The gateway running as a systemd service

## Next step

[04-llm-deepseek.md](04-llm-deepseek.md) — wire up the cheap LLM (if not done via the wizard),
then [05-channels.md](05-channels.md) to start chatting.
