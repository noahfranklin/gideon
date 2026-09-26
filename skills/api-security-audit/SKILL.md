---
name: api-security-audit
description: "Use when testing or auditing an API for security vulnerabilities — REST, GraphQL, gRPC, or WebSocket — including authentication/authorization, BOLA/IDOR, mass assignment, SSRF, rate limiting, and security misconfiguration. Maps findings to the OWASP API Security Top 10 (2023) and produces test steps, detection signals, and remediation for each. For authorized engagements only."
---

# API Security Audit

A complete, standards-mapped methodology for assessing the security of an API you own or are **authorized** to test. Every technique below is paired with what to look for (detection) and how to fix it (remediation) so the output is actionable for the product team.

## 0. Authorization gate (do this first)

Before any active testing, confirm:

- [ ] Written authorization / rules of engagement (RoE) covering these hosts and endpoints.
- [ ] In-scope base URLs, environments (prod vs staging), and accounts provided.
- [ ] Out-of-scope paths, data, and destructive actions explicitly listed.
- [ ] Testing window, rate limits, and an emergency contact.
- [ ] Handling rules for any sensitive data encountered.

If scope is unclear, pause and ask the engagement owner. Never test systems you don't own without documented permission.

## 1. Methodology overview

```
Scope & RoE ─► Recon & inventory ─► Map auth & roles ─► Per-endpoint tests
     ▲                                                        │
     └──────────────  Report & remediate  ◄──────────────────┘
```

Work one endpoint at a time, tracking: method, path, params, auth required, roles allowed, object ownership model.

## 2. Recon & inventory

- Collect the OpenAPI/Swagger, GraphQL introspection, or gRPC `.proto` definitions.
- Enumerate versions (`/v1`, `/v2`), hidden/undocumented routes, and deprecated hosts.
- Diff documented vs. observed endpoints (proxy your own client traffic to discover real calls).
- Record data classifications per endpoint (PII, secrets, financial).

**Detection signal for the org:** endpoints in traffic but not in the spec → inventory drift (see API9).

## 3. The OWASP API Security Top 10 (2023) — test & fix

### API1 — Broken Object Level Authorization (BOLA/IDOR)
- **Test (authorized):** with a low-privilege account, request objects owned by a *different* account by changing the identifier (`/orders/{id}`, GraphQL node IDs, filenames). Try sequential, UUID, and encoded IDs.
- **Detection:** server returns another tenant's/user's data without an ownership check.
- **Fix:** enforce an object-level authorization check on every data access, keyed to the authenticated principal — never trust a client-supplied ID alone. Use unguessable IDs as defense-in-depth, not as the control.

### API2 — Broken Authentication
- **Test:** weak/absent token validation, JWT `alg=none` or key confusion, missing expiry, credential stuffing resistance, password reset token predictability, missing MFA on sensitive flows.
- **Detection:** accepted forged/expired tokens; endpoints reachable without auth.
- **Fix:** validate signature + issuer + audience + expiry; short-lived tokens with rotation; rate-limit and lock out on auth endpoints; enforce MFA on sensitive operations.

### API3 — Broken Object Property Level Authorization (incl. mass assignment / excessive data exposure)
- **Test:** send extra properties in write requests (`"role":"admin"`, `"isVerified":true`); inspect read responses for fields the caller shouldn't see.
- **Detection:** privileged fields accepted from the client; responses leak internal/other-user fields.
- **Fix:** explicit allow-lists for readable and writable fields (DTOs/serializers); never bind requests straight to ORM models.

### API4 — Unrestricted Resource Consumption
- **Test:** absent rate limits, large payloads, expensive queries, unbounded pagination, costly third-party calls (SMS/email) triggerable by attackers.
- **Detection:** no 429s under load; a single caller can exhaust CPU/memory/spend.
- **Fix:** per-user + per-IP rate limits and quotas, request size caps, pagination limits, timeouts, and cost controls on paid downstreams.

### API5 — Broken Function Level Authorization
- **Test:** call admin/privileged functions with a normal-user token; swap HTTP methods; access `/admin/*` routes.
- **Detection:** privileged functions execute for under-privileged roles.
- **Fix:** deny-by-default authorization; enforce role/permission checks at the function level on the server, not the UI.

### API6 — Unrestricted Access to Sensitive Business Flows
- **Test:** can a flow meant for humans (purchase, signup, comment, booking) be automated at scale to cause harm (scalping, spam, inventory exhaustion)?
- **Detection:** no bot/abuse protection on high-value flows.
- **Fix:** device/behavior detection, CAPTCHAs where appropriate, per-account velocity limits, business-logic guards.

### API7 — Server Side Request Forgery (SSRF)
- **Test:** endpoints that fetch a user-supplied URL (webhooks, import-from-URL, image proxies). Try internal hosts, `169.254.169.254` metadata, and redirect chains — **only within authorized scope**.
- **Detection:** server fetches attacker-controlled internal targets.
- **Fix:** allow-list destinations, resolve+validate DNS, block link-local/internal ranges, disable unused URL schemes, isolate egress.

### API8 — Security Misconfiguration
- **Test:** missing security headers, verbose errors/stack traces, permissive CORS (`*` with credentials), default creds, unpatched components, open cloud storage, debug endpoints.
- **Detection:** any of the above exposed.
- **Fix:** hardened config baseline, least-privilege CORS, generic error messages, patch management, and config-as-code review. (See the `api-secure-design` skill.)

### API9 — Improper Inventory Management
- **Test:** old API versions, staging/debug hosts, undocumented/"shadow" endpoints still live.
- **Detection:** deprecated or non-prod endpoints reachable from the internet.
- **Fix:** maintain a live API inventory, retire old versions, separate/lock non-prod environments, document every endpoint.

### API10 — Unsafe Consumption of APIs
- **Test:** how the API trusts data from third-party/upstream APIs it calls (injection, redirects, oversized responses).
- **Detection:** upstream data used without validation.
- **Fix:** validate and sanitize data from integrated APIs; apply timeouts, TLS verification, and the same input hygiene you'd apply to end users.

## 4. Protocol-specific notes

- **GraphQL:** test introspection exposure, query depth/complexity limits (DoS), field-level authorization, batching abuse, and injection through resolvers. See `references/graphql-checklist.md`.
- **gRPC:** verify TLS/mTLS, per-method authorization, message-size limits, and reflection exposure.
- **WebSocket:** check origin validation, auth on upgrade, per-message authorization, and message flooding limits.

## 5. Reporting

For each finding record: title, OWASP API category, affected endpoint(s), severity (CVSS + business impact), reproduction steps, evidence, and concrete remediation. Group by severity, lead with an executive summary, and provide a remediation-priority table.

See `references/report-template.md` for a ready-to-fill format and `references/testing-checklist.md` for a printable pass/fail matrix.
