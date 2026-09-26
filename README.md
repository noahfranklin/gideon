<div align="center">

# 🛡️ Gideon

### Offensive & defensive security skills for Claude Code and Codex

*"With the three hundred… I will save you." — Judges 7:7*
*A small, disciplined force — recon, precision, and clever tactics — beats a bigger enemy. That's red-teaming done right.*

[![Skills](https://img.shields.io/badge/skills-5-blue)](#-the-skills)
[![License: MIT](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Validate Skills](https://github.com/noahfranklin/gideon/actions/workflows/validate-skills.yml/badge.svg)](.github/workflows/validate-skills.yml)
[![OWASP](https://img.shields.io/badge/mapped-OWASP%20API%20%2B%20LLM%20Top%2010-orange)](#-standards-mapping)

</div>

---

## What is this?

**Gideon** is a battle-tested collection of [Agent Skills](https://docs.claude.com/en/docs/claude-code/skills) that turn Claude Code (and Codex-style coding agents) into a rigorous, *authorized* security engineer. It covers both halves of the job:

- **🔴 Offense** — structured red-team methodology for APIs and AI/LLM applications, so you find the holes before an attacker does.
- **🔵 Defense** — secure-by-design checklists, hardening playbooks, and threat models, so you build products that don't have the holes in the first place.

Every skill is **defensive in purpose**: the goal is to help teams keep their own products (or clients they're authorized to test) safe. There are no drop-in weaponized exploits, no mass-scanning tooling, and no detection-evasion tradecraft. What you get is *methodology, test design, detection signals, and concrete remediation* — the stuff that actually makes software secure.

## Why you'll want it

- **Standards-mapped, not vibes-based.** Grounded in OWASP API Security Top 10 (2023), OWASP Top 10 for LLM Applications (2025), OWASP ASVS, NIST AI RMF, and MITRE ATLAS.
- **Portable.** Drop the `skills/` folder into `~/.claude/skills/` (Claude Code) or wherever your agent loads skills. Plain Markdown + frontmatter — no runtime, no lock-in.
- **Complete workflows.** Each skill is an end-to-end playbook: scope → recon → test → verify → remediate → report, with copy-paste checklists and report templates.
- **Authorization-first.** Every skill opens with a rules-of-engagement gate so the agent tests only what it's cleared to test.

## 🧩 The skills

| Skill | Color | What it does |
|-------|-------|--------------|
| [`api-security-audit`](skills/api-security-audit/SKILL.md) | 🔴 | Full API pentest methodology mapped to OWASP API Top 10 — REST, GraphQL, gRPC, WebSocket. Test design, detection, and fixes for BOLA, broken auth, SSRF, and more. |
| [`api-secure-design`](skills/api-secure-design/SKILL.md) | 🔵 | Secure-by-design review + hardening checklist for APIs: authN/authZ, rate limiting, schema validation, secrets, TLS, logging, CORS, inventory. |
| [`llm-redteam`](skills/llm-redteam/SKILL.md) | 🔴 | Red-team methodology for AI/LLM apps mapped to OWASP LLM Top 10 — prompt injection (direct + indirect), tool/agent abuse, RAG poisoning, system-prompt leakage, plus an eval-harness approach for repeatable testing. |
| [`llm-app-defense`](skills/llm-app-defense/SKILL.md) | 🔵 | Defense-in-depth for LLM apps: input/output mediation, least-privilege tool design, human-in-the-loop gates, RAG source hygiene, monitoring, and red-team CI. |
| [`threat-model`](skills/threat-model/SKILL.md) | ⚪ | STRIDE + PASTA + attack-tree threat modeling for web, API, and AI systems, with data-flow diagrams and a ready-to-fill deliverable. |

## 🚀 Install

**Claude Code (per-user):**
```bash
git clone https://github.com/noahfranklin/gideon.git
cp -r gideon/skills/* ~/.claude/skills/
```

**Project-scoped (share with your team via the repo):**
```bash
mkdir -p .claude/skills
cp -r gideon/skills/* .claude/skills/
```

Then just ask, e.g. *"Audit this API against the OWASP API Top 10"* or *"Red-team our chatbot for prompt injection"* — Claude picks the matching skill from its description.

**Codex / other agents:** the skills are provider-neutral Markdown. Point your agent's skill/instruction loader at the `skills/` directory.

## 📐 Standards mapping

| Standard | Covered by |
|----------|-----------|
| OWASP API Security Top 10 (2023) | `api-security-audit`, `api-secure-design` |
| OWASP Top 10 for LLM Applications (2025) | `llm-redteam`, `llm-app-defense` |
| OWASP ASVS | `api-secure-design` |
| NIST AI RMF (Govern/Map/Measure/Manage) | `llm-app-defense`, `threat-model` |
| MITRE ATLAS | `llm-redteam`, `llm-app-defense` |
| STRIDE / PASTA | `threat-model` |

## ⚖️ Use responsibly

These skills are for **authorized** security work only: your own systems, or targets you have explicit written permission to test (a signed engagement, a bug-bounty scope, a CTF, or a lab you own). Testing systems you don't own or aren't cleared for is illegal in most jurisdictions. See [SECURITY.md](SECURITY.md).

## 🤝 Contributing

New skills, better checklists, and fresh detections are welcome — see [CONTRIBUTING.md](CONTRIBUTING.md). Run `python3 scripts/validate_skills.py` before you open a PR.

## 📄 License

MIT © noahfranklin — see [LICENSE](LICENSE).
