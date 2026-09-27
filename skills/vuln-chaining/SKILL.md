---
name: vuln-chaining
description: "Use to move beyond isolated findings — combine low-severity primitives into high-impact exploit chains, reason about attack paths across domains (web+api+cloud+identity+network), correlate related weaknesses, and hunt for novel/logic vulnerabilities that scanners miss. Provides a primitive taxonomy, chaining and correlation methodology, and attack-path graphing to prioritize the fixes that break the most paths. Authorized engagements only."
---

# Vulnerability Chaining, Correlation & Novel-Bug Hunting

The skill that turns a list of findings into an attack. Real-world compromise is rarely one critical bug — it's a *chain* of small ones, and the real risk is the *path*, not the individual issue. This skill teaches how to combine, correlate, and discover.

## 0. Authorization gate
- [ ] Chaining/exploitation across the in-scope assets is authorized.
- [ ] Cross-domain movement (e.g., web → cloud → identity) is within the agreed scope before you traverse it.

## 1. Think in primitives, not "vulns"
Reframe each finding as a **capability primitive** — what it grants an attacker:
| Primitive | Example sources | Grants |
|-----------|-----------------|--------|
| Info disclosure | verbose errors, IDOR-read, metadata leak | recon, IDs, versions |
| Arbitrary read | LFI, SSRF, path traversal, IDOR | files, secrets, tokens |
| Arbitrary write | upload, mass assignment, writable config | foothold, config change |
| Auth context | leaked token/key, session flaw, SSRF-to-metadata creds | identity, API access |
| Code/command exec | injection, deserialization, SSTI | foothold |
| Privilege change | privesc, dangerous ACL, IAM combo | escalation |
| Trust/pivot | SSRF, delegation, cross-account role, hybrid identity | reach new zones |

A chain is a sequence of primitives where each unlocks the inputs for the next.

## 2. Chaining methodology
1. **Inventory primitives** from all skills' findings (web, api, cloud, AD, network...).
2. **Define goals** (crown-jewel data, DA, cloud org-admin).
3. **Backward-chain** from each goal: what capability would achieve it? What primitive yields that capability? Repeat until you reach a primitive you already hold or can obtain.
4. **Forward-chain** from your current access to see what it unlocks.
5. **Bridge domains** — the highest-impact chains cross boundaries:
   - Web SSRF → cloud metadata creds → cloud IAM privesc → data.
   - Phish → workstation foothold → local privesc → AD cred access → DA.
   - Leaked repo secret → API key → over-permissive cloud role → lateral.
   - On-prem AD compromise → hybrid sync → Entra global admin (and reverse).
6. **Validate** each link actually works end to end (a chain is only as strong as its weakest assumption).

## 3. Correlation
- **Same root cause, many symptoms:** cluster findings that share a cause (e.g., one missing authorization layer causing IDOR across many endpoints) → fix the cause once.
- **Compounding:** individually-low findings that together cross a severity threshold (rate-limit gap + weak password policy + no MFA = practical account takeover).
- **Cross-tool correlation:** merge outputs from the domain skills into one graph; a finding trivial in isolation may be the missing edge in a critical path.
- **Temporal/behavioral:** correlate what defenders can/can't see per step (feeds the purple-team detection-gap matrix in `red-team-ops`).

## 4. Attack-path graphing
Model the environment as a graph: **nodes** = assets/identities/data; **edges** = primitives/relationships that let you move between them. Then:
- Find shortest paths from an entry point to each goal.
- Identify **choke-point edges**: the single edge appearing in the most paths to crown jewels — fixing it breaks many chains at once (maximum-leverage remediation).
- BloodHound does this for AD; apply the same reasoning manually across web/api/cloud/identity.

## 5. Hunting novel & logic vulnerabilities (what scanners miss)
Scanners find known patterns; novel bugs live in *your* system's unique logic and assumptions.
- **Model intended behavior, then break the assumption:** every "the client will always…" or "this can only be reached after…" is a hypothesis to test.
- **Business-logic classes:** state-machine skips, race conditions/TOCTOU, quantity/price/limit manipulation, replay, workflow reordering, trust of client-controlled data, inconsistent authorization between endpoints doing the "same" thing.
- **Boundary & type confusion:** how components disagree about parsing/encoding/identity (parser differentials, unicode/normalization, request smuggling between proxy and app).
- **Emergent/integration bugs:** vulnerabilities that exist only in how two secure-looking components interact (e.g., trust of an internal header, SSO assertion reuse).
- **Hypothesis-driven PoC loop:** form a hypothesis → craft a minimal test → observe → refine → confirm with a reproducible PoC. Document the reasoning, not just the payload.
- **Variant analysis:** once you find one novel bug, systematically look for the same mistake elsewhere in the codebase/app — root-cause patterns repeat.

## 6. Prioritization output
Deliver a ranked list where severity reflects **chain impact**, not just individual CVSS, plus the choke-point fixes that break the most paths. This is what makes remediation efficient and the report credible.

## 7. Reporting
Present: primitive inventory, the attack-path graph, each realized chain (with the goal reached), correlated root causes, and choke-point remediations. Feed into `red-team-ops` reporting. See `references/chaining-playbook.md`.

---
<sub>© 2026 noahfranklin · Part of the [Gideon](https://github.com/noahfranklin/gideon) security suite · MIT License · Original work.</sub>
