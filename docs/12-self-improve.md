# 12 — Self-improvement via Claude Code

> **Agent note:** This is the "package manager" of the OS — it lets the *running* agent build its
> own new skills by delegating to Claude Code **on the VPS**. Powerful, so the guardrails matter:
> diff-review before commit, a permission deny-list protecting secrets, no auto-restart without an OK.

## The idea

The user says "build me a skill that does X" in chat. Hermes delegates to **Claude Code running on
the VPS**, which reads the Hermes code/skills, makes changes, and returns a summary + `git diff`.
Hermes shows you the diff and only ships it (commit + gateway restart) after you say yes.

```
You (chat) ──► Hermes ──► self-improve skill ──► Claude Code (headless, on VPS)
                                                      │ edits skills/config in a git repo
                                                      ▼
                              summary + `git diff`  ──► you approve? ──► commit + gateway restart
                                                                   └─ no ──► git checkout -- .
```

## Step 1 — Install Claude Code on the VPS

```bash
npm i -g @anthropic-ai/claude-code
claude --version
```

## Step 2 — Authenticate (token, not interactive)

The user runs `claude setup-token` (with their Claude plan) and pastes the token:

```bash
# in ~/.hermes/.env
CLAUDE_CODE_OAUTH_TOKEN=...
```

> Model availability depends on the user's Claude plan; the headless path commonly has Sonnet
> available. For top-tier models you may need an API key (pay-as-you-go) or a higher plan. Keep
> token-heavy self-improve runs modest.

## Step 3 — Install the self-improve skill + guardrails

```bash
cp -r skills/self-improve ~/.hermes/custom-skills/self-improve     # if you include this scaffold
# guardrail files (already placed in phase 03):
#   ~/.hermes/CLAUDE.md                 → standing instructions for on-VPS Claude
#   ~/.hermes/.claude/settings.json     → permission deny-list (protects secrets)
```

The deny-list (template: [../templates/claude-settings.json.example](../templates/claude-settings.json.example))
prevents the self-improve loop from reading/writing secrets:

```json
{ "permissions": { "deny": [
  ".env", "*.pass", "*credentials*.json", "*_token.json", "~/.config/gh/**", "hosts.yml"
] } }
```

Make the Hermes dir a git repo so changes are reviewable and revertible:
```bash
cd ~/.hermes && git init && printf '.env\n*.pass\n*credentials*.json\nsessions/\nlogs/\n' > .gitignore
```

## Step 4 — The loop in practice

1. Hermes runs Claude Code with edits allowed but **no auto-commit**.
2. It returns a human summary + `git diff`.
3. Hermes posts that to you; **you decide**.
4. Yes → `git add -A && git commit -m "..."` + `sudo hermes gateway restart --system`.
   No → `git checkout -- .`.

## Safety

- Never let the loop touch secrets (the deny-list enforces this).
- Always review the diff; keep changes small.
- Restart the gateway only after a passing quick test (`hermes -z`).

## Next step

[13-n8n-orchestration.md](13-n8n-orchestration.md).
