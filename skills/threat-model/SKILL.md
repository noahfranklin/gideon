---
name: threat-model
description: "Use when threat modeling a system — a web app, API, or AI/LLM application — to identify assets, trust boundaries, and threats before or during development. Guides STRIDE and PASTA analysis, attack trees, and data-flow diagrams, and produces a prioritized, ready-to-fill threat model with mitigations. Pairs with api-secure-design and llm-app-defense for remediation."
---

# Threat Modeling

A practical workflow to answer four questions (Shostack's framing):
**1) What are we building? 2) What can go wrong? 3) What are we going to do about it? 4) Did we do a good job?**

Use early in design, then keep it live as the system changes. Pairs with `api-secure-design` and `llm-app-defense` for concrete fixes.

## Step 1 — Model the system (what are we building?)
- Inventory **assets**: data (by classification), credentials, functionality, availability, reputation.
- Draw a **data-flow diagram (DFD)**: external entities, processes, data stores, and data flows.
- Mark **trust boundaries** — every point where data crosses from less-trusted to more-trusted (internet→API, user input→parser, untrusted text→LLM context, tenant→shared store).
- List **entry points** and the **privilege** at each.

## Step 2 — Find threats (what can go wrong?)

### STRIDE (per element / per boundary)
| Threat | Property violated | Ask |
|--------|-------------------|-----|
| **S**poofing | Authentication | Can someone impersonate a user/service? |
| **T**ampering | Integrity | Can data/code be modified in transit or at rest? |
| **R**epudiation | Non-repudiation | Can an actor deny an action? Is it logged? |
| **I**nformation disclosure | Confidentiality | Can data leak to the unauthorized? |
| **D**enial of service | Availability | Can it be exhausted or crashed? |
| **E**levation of privilege | Authorization | Can someone gain rights they shouldn't have? |

Apply STRIDE to each process, store, flow, and boundary in the DFD.

### PASTA (when you need risk-centric, business-aligned depth)
Seven stages: define objectives → define technical scope → decompose the application → analyze threats → analyze vulnerabilities → model attacks (attack trees) → analyze risk & impact. Use for higher-stakes systems needing business risk alignment.

### Attack trees
For a critical asset, put the attacker goal at the root and enumerate AND/OR paths to it. Useful for prioritizing which boundaries matter most.

## Step 3 — Decide mitigations (what will we do?)
For each credible threat choose: **mitigate / eliminate / transfer / accept** (with an owner and rationale for accepts). Map mitigations to controls in:
- `api-secure-design` for API/auth/input/rate-limit/crypto controls.
- `llm-app-defense` for LLM-specific injection/agency/output controls.
- Standards: OWASP ASVS, NIST controls, MITRE ATLAS (for AI).

Prioritize by **likelihood × impact**; track as issues with owners and due dates.

## Step 4 — Validate (did we do a good job?)
- Confirm each high/critical threat has a mitigation and a test.
- Feed offensive validation from `api-security-audit` / `llm-redteam` back into the model.
- Re-review on architecture changes, new integrations, or new data types.

## AI/LLM systems — extra elements to model
- Untrusted text reaching the model (direct + indirect via RAG/tools/files/web) is a trust boundary.
- Tools/agents = new entry points for elevation-of-privilege and tampering.
- Model/plugin/dataset supply chain and RAG corpus as assets and tampering targets.

## Deliverable
Fill `references/threat-model-template.md`. Keep it in the repo next to the design docs so it evolves with the system.

---
<sub>© 2026 noahfranklin · Part of the [Gideon](https://github.com/noahfranklin/gideon) security suite · MIT License · Original work.</sub>
