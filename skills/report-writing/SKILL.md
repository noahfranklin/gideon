---
name: report-writing
description: "Use when writing up security findings and assessment reports — structuring each finding (title, description, impact, affected assets, severity/CVSS), building clear proof-of-concept sections with formatted HTTP request/response and highlighted payloads, step-by-step reproduction, and remediation/solution, then assembling the full executive + technical report. Works for black-box and gray-box engagements across web, API, mobile, cloud, network, AD/identity, and AI/LLM. The deliverable that makes all the other skills count."
---

# Security Report Writing

The findings only matter if the report lands. This skill standardizes how every Gideon assessment is written up so it's clear, reproducible, and actionable — for both a CISO skimming the summary and an engineer applying the fix. Works for **black-box** (external, no internals) and **gray-box** (partial knowledge/creds) engagements; note which was used, since it affects coverage caveats.

## 1. Report anatomy
```
Cover & metadata ─► Executive summary ─► Scope & methodology ─►
Findings (severity-ranked) ─► Attack-path narrative ─► Remediation roadmap ─► Appendices
```

- **Executive summary (non-technical):** what was tested, overall posture, count by severity, top 3–5 risks in business terms, and headline recommendations. No jargon.
- **Scope & methodology:** targets, dates, black-box vs gray-box, standards used (OWASP/ATT&CK/PTES), accounts/roles provided, and limitations/caveats.
- **Findings:** the core — one per issue, ranked by severity (see finding template).
- **Attack-path narrative:** how findings chain into real impact (pull from `vuln-chaining` / `red-team-ops`).
- **Remediation roadmap:** prioritized fixes, incl. choke-point fixes that break multiple paths.
- **Appendices:** raw evidence index, tooling, full activity timeline (for red team).

## 2. The finding template (use for every finding)
Each finding must contain, in order:
1. **Title** — specific and impact-led: *"Unauthenticated BOLA in /api/orders/{id} exposes all customer orders"* — not *"IDOR found"*.
2. **Severity** — CVSS v3.1 vector + score, *and* a business-impact sentence (they can diverge; explain if so).
3. **Affected assets** — exact endpoints/hosts/params/components/versions.
4. **Description** — what the flaw is and *why it matters here* (root cause, not just the symptom).
5. **Steps to reproduce** — numbered, exact, copy-pasteable; include preconditions (auth level, role, state). A competent engineer must be able to reproduce it from these steps alone.
6. **Proof of concept (PoC)** — the request(s)/response(s) or commands that demonstrate it, with the **payload highlighted** (see §3).
7. **Impact** — what an attacker achieves; reference any chain this finding enables.
8. **Remediation / solution** — specific, actionable fix (code/config level where possible), plus a defense-in-depth note and a reference (OWASP/CWE/vendor).
9. **References** — CWE ID, OWASP category, ATT&CK technique, vendor advisory.

See `references/finding-template.md`.

## 3. PoCs: HTTP request/response & payload highlighting
Format PoCs so the reader instantly sees *what you sent* and *what proved it*.

- Put request and response in fenced code blocks labelled `http`.
- **Highlight the payload / the key line** with an inline marker so it's unmistakable — e.g. a `# <== PAYLOAD` / `# <== EVIDENCE` comment, or bold call-out text above the block. (Markdown code blocks don't color arbitrary spans, so use explicit markers.)
- Redact secrets/PII (`Authorization: Bearer <redacted>`), but keep enough to reproduce.
- Show the **minimal** request that triggers it; trim noise.
- For non-HTTP PoCs (CLI, SQL, mobile, cloud), show the exact command + salient output the same way.

Example:
````
**Request** (payload highlighted):
```http
GET /api/orders/1043 HTTP/1.1
Host: target.example
Authorization: Bearer <userB-token-redacted>      # <== authenticated as User B
```
**Response** (evidence highlighted):
```http
HTTP/1.1 200 OK
Content-Type: application/json

{"orderId":1043,"customer":"User A","total":"$4,210.00"}   # <== User B reads User A's order
```
````
See `references/poc-formatting.md` for more patterns (SQLi, XSS, SSRF, auth bypass, cloud, CLI).

## 4. Reproduction test cases
Make each finding a repeatable **test case** so the client can verify the fix and add a regression check:
- **Test ID**, precondition/state, exact steps, expected-vulnerable result, expected-fixed result.
- For chains, provide the ordered multi-step case.
- This is what turns a report into lasting value (and feeds `llm-redteam`'s eval harness or an app's test suite).

## 5. Severity & prioritization
- Use CVSS for a common scale, but let **business impact** and **chain role** drive the priority order (a "medium" that's the choke point in a path to crown jewels outranks an isolated "high").
- Provide a remediation-priority table: finding × severity × effort × priority × paths-broken.

## 6. Black-box vs gray-box notes
- **Black-box:** state coverage limits (what couldn't be reached without internals); frame confidence accordingly.
- **Gray-box:** document the access/knowledge provided; deeper coverage expected; note anything still out of reach.
- Keep evidence reproducible in *both* — a black-box PoC should not depend on privileged info the client didn't grant you.

## 7. Quality bar (self-check before delivery)
- [ ] Every finding reproducible from its steps alone.
- [ ] Every PoC has request/response (or command/output) with the payload/evidence highlighted and secrets redacted.
- [ ] Every finding has a concrete, actionable solution + reference.
- [ ] Severity justified; priority reflects business impact + chains.
- [ ] Exec summary readable by a non-technical stakeholder.
- [ ] Chains and root-cause correlations captured (see `vuln-chaining`).

Templates: `references/finding-template.md`, `references/poc-formatting.md`, `references/report-skeleton.md`.
