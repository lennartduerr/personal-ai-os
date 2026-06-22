# 02 — VPS setup (your agent's home)

> **Agent note:** Go slow here — this is where non-technical users get stuck. Explain *why* each
> step exists, paste the exact commands, and **confirm before anything destructive** (disabling
> root login, firewall changes). If the user already has a VPS + SSH access, skip to the hardening
> checklist at the end and then go to [03-install-hermes.md](03-install-hermes.md).

A VPS ("virtual private server") is a small always-on Linux computer in a data center. It's where
your agent lives so it can run 24/7 without your laptop being on. Any provider works; we use
**[Hetzner Cloud](https://www.hetzner.com/cloud)** as the worked example because it's cheap and
reliable. ~€5–6/month gets you more than enough.

---

## Step 1 — Create the server

1. Sign up at **https://www.hetzner.com/cloud** and open the **Cloud Console**
   (**https://console.hetzner.cloud**).
2. Click **+ New Project**, name it (e.g. `personal-ai-os`), open it.
3. Click **Add Server** and choose:
   - **Location:** pick one near you (e.g. Falkenstein/Nuremberg in EU, Helsinki, Ashburn in US).
   - **Image:** **Ubuntu** (latest LTS).
   - **Type:** **Shared vCPU** → **CPX22** (2 vCPU / 4 GB RAM / 40 GB) is the sweet spot.
     (Smaller works too; 4 GB is comfortable.)
   - **SSH key:** add your **public** key here (see Step 2 — do that first if you don't have one).
   - Leave the rest default. Click **Create & Buy now**.
4. Note the server's **public IPv4 address** — you'll use it everywhere as `<VPS_IP>`.

> 💡 Other providers (DigitalOcean, Hetzner dedicated, a Raspberry Pi at home, etc.) work the same
> way from Step 2 on — you just need Ubuntu + SSH.

---

## Step 2 — Create your SSH key (how you and the agent control the VPS)

An SSH key is a pair of files: a **private** key (stays on your machine, secret) and a **public**
key (you give it to the server). They let you log in without a password — and they're how
**Claude Code will run commands on the VPS for you**.

On your local machine (macOS/Linux; on Windows use Git Bash or WSL):

```bash
ssh-keygen -t ed25519 -C "personal-ai-os" -f ~/.ssh/personal_ai_os
```

- Press Enter to accept the path; optionally set a passphrase.
- This creates `~/.ssh/personal_ai_os` (private — **never share**) and
  `~/.ssh/personal_ai_os.pub` (public — safe to paste).

Show the **public** key to paste into Hetzner (Step 1.3) or to add later:

```bash
cat ~/.ssh/personal_ai_os.pub
```

If you created the server before adding the key, add it now from your machine:

```bash
ssh-copy-id -i ~/.ssh/personal_ai_os.pub root@<VPS_IP>
```

---

## Step 3 — First login + create a non-root user

Logging in as `root` all the time is risky. We create a normal user (`hermes`) with `sudo`.

```bash
# Log in as root the first time
ssh -i ~/.ssh/personal_ai_os root@<VPS_IP>

# Create the user and give it sudo
adduser hermes                 # set a password when prompted
usermod -aG sudo hermes

# Copy your SSH key so you can log in as 'hermes' too
rsync --archive --chown=hermes:hermes ~/.ssh /home/hermes
# (or: mkdir -p /home/hermes/.ssh && cp ~/.ssh/authorized_keys /home/hermes/.ssh/ && chown -R hermes:hermes /home/hermes/.ssh)

# (optional but convenient) allow passwordless sudo for this single-user box
echo "hermes ALL=(ALL) NOPASSWD:ALL" | sudo tee /etc/sudoers.d/hermes
```

Now log out and log back in **as `hermes`** to confirm it works:

```bash
ssh -i ~/.ssh/personal_ai_os hermes@<VPS_IP>
```

### Make logins effortless (and agent-friendly)

Add a host alias on your local machine so you (and Claude Code) can just say `ssh personal-ai-os`:

```bash
cat >> ~/.ssh/config <<'EOF'

Host personal-ai-os
    HostName <VPS_IP>
    User hermes
    IdentityFile ~/.ssh/personal_ai_os
EOF
```

> **How the agent gets access:** Claude Code runs on *your* machine and uses this SSH key to run
> commands on the VPS (e.g. `ssh personal-ai-os 'hermes ...'`). You never hand anyone your private
> key — the agent just uses your local SSH the same way you do. You can revoke access any time by
> removing the public key from `~/.ssh/authorized_keys` on the server.

---

## Step 4 — Harden the box (do this once)

> ⚠️ Confirm with the user before running these — locking yourself out is the classic mistake.
> Keep your current SSH session open and test a **new** session before closing the old one.

```bash
# Firewall: allow SSH only, then enable
sudo apt update && sudo apt -y install ufw fail2ban
sudo ufw allow OpenSSH
sudo ufw --force enable

# fail2ban bans IPs after repeated failed logins (defaults are fine)
sudo systemctl enable --now fail2ban

# Disable root SSH login and password auth (keys only)
sudo sed -i 's/^#\?PermitRootLogin.*/PermitRootLogin no/' /etc/ssh/sshd_config
sudo sed -i 's/^#\?PasswordAuthentication.*/PasswordAuthentication no/' /etc/ssh/sshd_config
sudo systemctl restart ssh
```

**Test now, before closing your session:** open a new terminal and run
`ssh personal-ai-os` — it should log you in as `hermes` with the key. ✅

---

## Step 5 — Base packages

```bash
sudo apt -y install git curl build-essential python3-venv python3-pip
# Node.js (v22 LTS) — needed by the gateway and (optionally) Claude Code
curl -fsSL https://deb.nodesource.com/setup_22.x | sudo -E bash -
sudo apt -y install nodejs
node -v && python3 --version
```

---

## Hardening checklist (for "I already have a VPS")

- [ ] Non-root user with sudo, SSH-key login working
- [ ] Root SSH login disabled, password auth disabled
- [ ] `ufw` enabled, only SSH (22) open
- [ ] `fail2ban` running
- [ ] `git`, `curl`, `python3-venv`, Node.js v22 installed
- [ ] You can reach it via `ssh personal-ai-os`

## Next step

[03-install-hermes.md](03-install-hermes.md).
