---
name: red-team-ops
description: "Use to plan and run a full authorized red-team engagement end to end — scoping and rules of engagement, threat-actor emulation, the attack lifecycle (recon → initial access → execution → escalation → lateral movement → objectives), C2 concepts, deconfliction and safety, evidence handling, and executive + technical reporting. Maps the engagement to MITRE ATT&CK and orchestrates the other Gideon skills. Authorized engagements only."
---

# Red Team Operations (Engagement Lifecycle)

The umbrella methodology that ties the domain skills together into a coherent, **authorized** red-team engagement emulating a real threat actor against defined objectives. Mapped to **MITRE ATT&CK** and aligned with PTES / TIBER-style structured testing.

## 0. Authorization & safety gate
- [ ] Signed authorization / statement of work with named signatories.
- [ ] Rules of engagement: scope, objectives ("flags"), off-limits systems/data, allowed techniques, hours, intensity.
- [ ] **Deconfliction process** and 24/7 emergency contacts; SOC awareness level (announced/unannounced) agreed.
- [ ] Safety rules: no destruction, fragile-system exclusions, data-minimization, secure evidence handling.
- [ ] Legal review and get-out-of-jail letter for on-site work.

## 1. Threat model & emulation plan
- Choose a threat profile appropriate to the org; define objectives in business terms (reach X data, prove Y impact).
- Map planned TTPs to MITRE ATT&CK for coverage and later blue-team comparison. Pair with `threat-model`.

## 2. The attack lifecycle (orchestration map)
```
Recon ─────────────► recon-osint
Initial access ────► web-app-pentest / api-security-audit / social-engineering /
                     wireless-pentest / network-device-pentest / external network-pentest
Execution/foothold ► (payload delivery per RoE)
Priv esc ──────────► privilege-escalation
Discovery/cred ────► post-exploitation
Lateral movement ──► post-exploitation / active-directory-pentest / entra-cloud-pentest
Cloud/container ───► cloud-pentest / container-k8s-pentest
Objectives/impact ─► post-exploitation (prove + document)
Correlate paths ───► vuln-chaining
Report ────────────► this skill
```
Work objective-first: pick the shortest credible path to each flag, then broaden coverage.

## 3. C2 & infrastructure (concepts)
Understand command-and-control and redirector concepts for realistic emulation and, crucially, to advise **detection**. Use established frameworks under RoE. Keep operator OPSEC professional (protect the engagement and client data); do not build tooling whose purpose is evading defenses for malicious use.

## 4. Deconfliction, logging & safety
- Log every action with timestamps and source; embed engagement identifiers.
- Real-incident check: if the blue team responds, follow the deconfliction procedure.
- Continuous scope awareness; stop and consult on ambiguity.

## 5. Purple-teaming & detection value
- Compare executed ATT&CK techniques against what the SOC detected → a detection gap matrix.
- Deliver detection/hardening recommendations, not just "we got DA."

## 6. Reporting (two audiences)
- **Executive:** objectives, whether reached, business risk, strategic recommendations — plain language.
- **Technical:** full attack narrative (kill chain), each finding with evidence + remediation, ATT&CK mapping, and the detection-gap matrix.
- Prioritize fixes by how many attack paths they break (see `vuln-chaining`).

See `references/roe-template.md` and `references/redteam-report-template.md`.
