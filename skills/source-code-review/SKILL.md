---
name: source-code-review
description: "Use when reviewing source code for security vulnerabilities (white-box / gray-box) — tracing untrusted input from source to dangerous sink, auditing authentication/authorization logic, finding injection, deserialization, SSRF, path traversal, secrets, and unsafe crypto, triaging SAST output, and performing variant analysis to find every instance of a bug class. Produces findings with the vulnerable code path and a fix. Authorized review of code you own or are cleared to audit."
---

# Secure Source Code Review

White-box security review: read the code, follow the data, and find the flaw at its root — then fix the whole class, not just the one instance. Complements the black/gray-box runtime skills (`web-app-pentest`, `api-security-audit`) with the view an attacker doesn't have but a defender does.

## 0. Authorization gate
- [ ] You own the code or are authorized to audit it (repo access granted).
- [ ] Scope: which services/languages/branches; handling of any secrets found.

## 1. Orient before reading line-by-line
- Map the app: entry points (routes, handlers, consumers, CLI, deserializers), trust boundaries, authn/authz model, data stores, and outbound calls.
- Identify the **sources** (where untrusted input enters) and the **dangerous sinks** (DB, OS/exec, file path, template, serializer, HTTP client, HTML response).
- Note the tech stack's footguns (framework-specific unsafe APIs).

## 2. Source → sink tracing (taint analysis by hand)
For each sink, walk backwards: does attacker-controlled data reach it without adequate validation/encoding? Record the full path (file:line → file:line).

| Sink | Bug class if tainted | What a safe path looks like |
|------|----------------------|-----------------------------|
| SQL/ORM raw query | SQL/NoSQL injection | parameterized queries / bound params |
| `exec`/shell/`system` | command injection | no shell; arg arrays; strict allow-list |
| file path join | path traversal / LFI | canonicalize + confine to base dir |
| template render | SSTI / XSS | context-aware autoescaping, no raw eval |
| deserializer | insecure deserialization | safe formats, type allow-lists, no gadget-prone libs |
| HTTP client w/ user URL | SSRF | destination allow-list, block internal ranges |
| response/DOM write | XSS | contextual output encoding |

## 3. Logic & design review (what SAST misses)
- **Authorization:** is every sensitive operation checked server-side against the authenticated principal and the *specific object* (BOLA/IDOR at the code level)? Deny-by-default?
- **Authentication/session:** token validation, expiry, fixation, password handling.
- **Business logic:** state-machine assumptions, race conditions/TOCTOU, limit/price/quantity trust.
- **Crypto:** hardcoded keys, weak algorithms, custom crypto, predictable randomness for security use.
- **Secrets:** credentials/keys in source, config, or history.

## 4. Triaging SAST output
- Treat scanner findings as **leads**, not verdicts: confirm reachability (is the sink actually attacker-reachable?), rule out compensating controls, and discard false positives.
- Prioritize by exploitability × impact; feed confirmed items to `vuln-chaining`.

## 5. Variant analysis (high leverage)
Once you confirm one bug, **grep the codebase for the same pattern** — the unsafe API, the missing check, the dangerous sink. Root-cause mistakes repeat. Fixing the class (e.g., a safe wrapper + a lint rule) beats fixing one line.

## 6. Tooling
Language SAST (semgrep rules, CodeQL queries), secret scanners (gitleaks/trufflehog), dependency SCA, and plain `grep`/IDE for taint tracing. Prefer precise semgrep/CodeQL queries you can read over opaque scanners.

## 7. Reporting
Per finding: file:line source → sink path, bug class (CWE), exploitability, impact, and a concrete code-level fix (plus a lint/query to prevent regressions). Use `report-writing`. Checklist: `references/review-checklist.md`.
---
<sub>© 2026 noahfranklin · Part of the [Gideon](https://github.com/noahfranklin/gideon) security suite · MIT License · Original work.</sub>
