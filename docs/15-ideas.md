# 15 — Ideas & extensions (beyond the core)

> **Agent note:** This is a menu of *optional extras* to mention near the end, once the core OS is
> running — not part of the default install. Don't push them; surface them as "here's where you can
> take this next" and build any the user wants. Same rules apply (consent-first, you do the work,
> never leak secrets).

The core OS (channels, skills, briefing, notes/second-brain, dashboard, self-improve) is the
foundation. Here are popular ways people extend it.

## 📱 More channels

- **WhatsApp (Business)** — connect a **WhatsApp Business** account via the WhatsApp Business
  Platform / Cloud API (Meta). Note: this needs a **Business** account — a normal personal WhatsApp
  won't work for API access. You get a phone-number id + access token from Meta's developer console
  and wire it as another channel/skill. Good for people who live in WhatsApp.
- **Signal** — via `signal-cli` on the VPS (privacy-focused, no business account needed).
- **Discord** — a bot for community/server-style use.
- **SMS / phone** — via a provider like Twilio for text or voice.

## 🎙️ Voice & multimodal

- **Voice notes in → text** — transcribe incoming Telegram/WhatsApp voice messages (e.g. Whisper)
  so you can talk to the agent.
- **Text → voice replies** — TTS for spoken answers.
- **Better vision** — richer image/document understanding (mind the "no confidential docs to cloud
  vision" rule).

## 🏠 Life integrations

- **Home automation** — Home Assistant / smart-home control via a skill.
- **Finance** — read-only balance/transaction summaries (never store bank credentials in cloud).
- **Health/fitness** — pull summaries from a wearable/API into the briefing.
- **Location & travel** — set your home in `SOUL.md` and add commute/weather/travel-time helpers.

## 🧠 Smarter memory

- **Auto-ingest everything** — `sbp watch` a folder so saved docs/attachments enter the second brain
  automatically.
- **Per-topic briefings** — scheduled digests drawn from the brain ("what changed in <project>").

## 📤 Outbound & reports

- **Mail sending** — finish the SMTP relay so the agent can send (not just draft) on request.
- **Scheduled reports** — recurring research/analysis delivered to chat or saved as PDF.

## 🧩 Orchestration (advanced)

- **Workflow automation with n8n** — only if you already use n8n. See
  [13-n8n-orchestration.md](13-n8n-orchestration.md).
- **Multi-agent / multi-user** — run separate personas, or share a hardened instance with family.

## 🖥️ Dashboard upgrades

The [dashboard](../dashboard/) is a template — extend it with more blocks, charts, theming, a
calendar view, mobile polish, or stronger auth. See its README's "Ideas to extend it".

---

> Pick one, scope it small, build it with the user, verify, ship. The self-improvement loop
> ([12](12-self-improve.md)) makes adding new skills for any of these straightforward.
