# Full Report Skeleton

1. **Cover** — client, assessment type (black/gray-box), dates, classification, version, authors.
2. **Confidentiality & authorization** — RoE reference, distribution limits.
3. **Executive summary** — plain-language posture, severity counts, top risks, headline recommendations.
4. **Scope & methodology** — targets, black/gray-box, standards (OWASP/ATT&CK/PTES/NIST), accounts/roles, limitations.
5. **Severity summary table**
   | Severity | Count |
   |----------|-------|
6. **Remediation priority table**
   | # | Finding | Severity | Effort | Paths broken | Priority |
7. **Findings** — one per finding using `finding-template.md`, ranked by severity.
8. **Attack-path narrative** — how findings chain to impact (`vuln-chaining` / `red-team-ops`).
9. **Detection-gap matrix** (red/purple team) — ATT&CK technique × detected? × recommendation.
10. **Strategic recommendations** — root-cause/program-level fixes.
11. **Appendices** — evidence index, tooling, full activity timeline, cleanup confirmation.
