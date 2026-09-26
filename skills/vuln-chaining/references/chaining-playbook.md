# Chaining, Correlation & Novel-Bug Playbook

## Primitive inventory (fill from all findings)
| # | Finding (source skill) | Primitive type | Capability granted | Preconditions |
|---|------------------------|----------------|--------------------|---------------|

## Goals
1. __  2. __  3. __

## Chain worksheet
| Goal | Step 1 (primitive→capability) | Step 2 | Step 3 | Validated? | Domains crossed |
|------|-------------------------------|--------|--------|-----------|-----------------|

## Classic cross-domain chains to check
- [ ] SSRF → cloud metadata creds → IAM privesc → data
- [ ] Phish → workstation → local privesc → AD creds → DA
- [ ] Leaked secret/repo → API key → over-permissive cloud role → lateral
- [ ] On-prem AD → hybrid sync/federation → Entra global admin (and reverse)
- [ ] IDOR-read (IDs) → mass assignment (privileged field) → account takeover
- [ ] File upload → path control → code exec

## Correlation
- [ ] Cluster findings by shared root cause
- [ ] Identify compounding low-sevs crossing a threshold
- [ ] Merge domain-skill outputs into one graph

## Attack-path graph
- Nodes: assets / identities / data
- Edges: primitives / trust relationships
- [ ] Shortest paths entry → each goal
- [ ] Choke-point edge(s) = max-leverage fix

## Novel / logic-bug hunting
- [ ] Enumerate "the system assumes…" statements; test each
- [ ] State-machine skips / workflow reorder
- [ ] Race / TOCTOU
- [ ] Quantity/price/limit/replay abuse
- [ ] Parser/encoding differentials; request smuggling
- [ ] Cross-component trust (internal headers, SSO reuse)
- [ ] Variant analysis: find the same bug elsewhere
- [ ] Reproducible PoC + documented reasoning

## Prioritized output
- [ ] Findings ranked by chain impact (not just CVSS)
- [ ] Choke-point remediations listed first
