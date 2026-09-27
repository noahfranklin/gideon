---
name: social-engineering
description: "Use when planning or running an AUTHORIZED social-engineering assessment — phishing/spear-phishing simulations, vishing, pretext design, and security-awareness measurement — as part of a sanctioned engagement. Covers scoping, campaign design, safe execution, metrics, and awareness remediation. Strictly for authorized, consented programs; never for deceiving people outside an approved engagement."
---

# Social Engineering (Authorized Assessment)

Methodology for **sanctioned** human-layer testing that measures and improves an organization's resilience to social attacks. This is about strengthening the workforce — every action requires organizational authorization and follows agreed rules that protect employees.

## 0. Authorization & ethics gate (mandatory)
- [ ] Written authorization from an executive sponsor who can consent on the org's behalf.
- [ ] Defined scope: which groups, channels (email/phone/SMS), and pretext limits.
- [ ] **Employee-protection rules:** no capturing real passwords into attacker-held stores, no lasting harm, no coercion/harassment, no sensitive-topic lures (medical, layoffs, etc.) unless explicitly agreed.
- [ ] Data handling: PII minimization, secure storage, defined retention/deletion.
- [ ] Legal/HR review and a debrief/awareness plan for participants.

This skill is for programs where the target *organization* consents. It must not be used to deceive individuals outside such a program.

## 1. Recon (for realism, within scope)
- Public info that a real attacker would use: email formats, org structure, tech/vendors, current events (from `recon-osint`). Keep pretexts plausible but non-harmful.

## 2. Campaign design
- **Objective:** measure click / credential-submit / report rates, or test a specific control (e.g., MFA prompt handling), not to "catch" individuals.
- **Pretext:** believable, within agreed sensitivity limits.
- **Landing pages:** training-oriented; if credentials are entered, do **not** store real passwords — record the *event*, then redirect to just-in-time training.
- **Segmentation:** track by group for awareness metrics, not individual punishment.

## 3. Channels
- **Phishing/spear-phishing** (email), **vishing** (phone), **smishing** (SMS), **pretext calls** — only those in scope. Use sending infrastructure and templates you control.

## 4. Safe execution
- Coordinate with the sponsor and (as agreed) the SOC to avoid a real incident response burn.
- Include an internal identifier so the blue team can distinguish the simulation.
- Provide an easy "report phishing" path and measure reporting as a positive metric.

## 5. Metrics & remediation
- Report **aggregate** rates: delivered, opened, clicked, submitted, reported, time-to-report.
- Deliver awareness training tied to results; re-test to show improvement.
- Recommend technical controls that reduce human risk: phishing-resistant MFA, email authentication (SPF/DKIM/DMARC), attachment/link protection, and reporting tooling.

## 6. Reporting
Aggregate metrics + trends + recommended controls and training. Never single out individuals for blame. Checklist: `references/se-checklist.md`.

---
<sub>© 2026 noahfranklin · Part of the [Gideon](https://github.com/noahfranklin/gideon) security suite · MIT License · Original work.</sub>
