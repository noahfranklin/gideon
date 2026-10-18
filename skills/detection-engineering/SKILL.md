---
name: detection-engineering
description: "Use to turn offensive findings into defenses that catch the next attacker — building and validating detections for the techniques the red-team skills exercise. Covers log/telemetry sourcing, MITRE ATT&CK coverage mapping, writing detection logic (Sigma-style, portable), reducing false positives, and purple-team validation. The blue-team companion that closes the loop from red-team-ops and vuln-chaining. For your own environment."
---

# Detection Engineering (Purple Team)

An engagement that ends at "we got Domain Admin" leaves the organization no safer. This skill closes the loop: for each technique the offensive skills use, build a **detection**, validate it, and measure coverage. The defensive counterpart to `red-team-ops`.

## 0. Scope
- [ ] Your own environment / telemetry (or an authorized SOC engagement).
- [ ] Log sources and SIEM/EDR platform identified.

## 1. Start from the attack
Detection is cheapest when driven by real TTPs. Take the techniques from the engagement (`red-team-ops` detection-gap matrix, `post-exploitation`, `active-directory-pentest`, `entra-cloud-pentest`, etc.) and build a detection per technique.

## 2. Telemetry first (you can't detect what you don't log)
For each technique, identify the data source that reveals it:
- **Endpoint:** process creation + command line, auth events, service/scheduled-task creation, LSASS access, module loads.
- **Identity:** AD/Kerberos logs (TGS/AS anomalies), Entra sign-in + audit logs, consent grants, risky sign-ins.
- **Network:** DNS, flow, proxy, poisoning/relay signatures.
- **Cloud:** CloudTrail / Activity / Audit logs; API calls, IAM changes.
- **App:** auth/authz failures, LLM prompt/tool-call logs (for `agentic-ai-security`).
Record gaps where the needed telemetry isn't collected — that's finding #1.

## 3. Write the detection (portable logic)
- Express detections in a portable, reviewable form (Sigma-style rules you can translate to your SIEM) tied to an **ATT&CK technique ID**.
- Favor behavior over brittle IOCs (e.g., "service binary written then started from a user-writable path" beats a hash).
- Each rule: data source, logic, ATT&CK mapping, severity, and a triage/response note.

## 4. Tune for false positives
- Baseline normal first; add scoped exclusions (not blanket ones).
- Prefer correlation (several weak signals) over one noisy rule.
- Track precision; a rule nobody trusts is worse than none.

## 5. Validate (purple team)
- Safely reproduce the technique in a controlled way (atomic tests / the authorized red-team action) and confirm the detection fires with useful context.
- Build an **ATT&CK coverage matrix**: technique × telemetry present × detection present × validated. Empty cells are the roadmap.

## 6. Close the loop
Feed validated detections and remaining gaps back into `red-team-ops` reporting so each engagement raises the detection baseline.

## 7. Tooling
SIEM/EDR query languages, Sigma + converters, ATT&CK Navigator for coverage, atomic/adversary-emulation test libraries. Keep detections in version control and test them like code.

## 8. Reporting
Deliver: coverage matrix, new/updated detection rules (with ATT&CK IDs), telemetry gaps to close, and tuning notes. Checklist: `references/detection-checklist.md`.
---
<sub>© 2026 noahfranklin · Part of the [Gideon](https://github.com/noahfranklin/gideon) security suite · MIT License · Original work.</sub>
