---
name: api-secure-design
description: "Use when designing, reviewing, or hardening an API for security — choosing authentication/authorization, adding rate limiting and quotas, validating input/schemas, managing secrets and TLS, configuring CORS, setting security headers, and logging. Provides a secure-by-design checklist and remediation guidance mapped to OWASP API Top 10 and OWASP ASVS. Defensive/blue-team companion to api-security-audit."
---

# API Secure Design & Hardening

A secure-by-design review and hardening playbook for APIs. Use it during design review, code review, or when remediating findings from `api-security-audit`. Each control names *what good looks like* so you can verify it in code and config.

## How to use
1. Identify the API's trust boundaries and data classifications (pair with the `threat-model` skill).
2. Walk each control area below; mark met / gap / n/a.
3. For gaps, apply the remediation and add a regression test.

## 1. Authentication
- Use standard protocols: **OAuth 2.0 / OIDC** for delegated auth, **mTLS** for service-to-service. Don't invent auth.
- Short-lived access tokens + rotating refresh tokens; validate **signature, issuer, audience, expiry** on every request.
- For JWTs: pin the algorithm server-side (reject `none`/algorithm confusion), verify against the expected key set, keep tokens out of URLs.
- Rate-limit and lock out credential endpoints; support MFA on sensitive operations.
- API keys: scoped, revocable, rotated, never in source control (see Secrets).

## 2. Authorization
- **Deny by default.** Every endpoint requires an explicit allow decision.
- **Object-level checks (BOLA defense):** verify the authenticated principal owns/may access the specific object on *every* read and write — don't trust client-supplied IDs.
- **Function-level checks:** enforce role/permission at the server, independent of the UI.
- Prefer centralized policy (RBAC/ABAC, policy engine) over scattered `if role ==` checks.
- Enforce tenant isolation in multi-tenant systems at the data-access layer.

## 3. Input validation & output handling
- Validate against a **strict schema** (types, ranges, lengths, formats, enum allow-lists) at the edge; reject unknown fields.
- **Property allow-lists** for writable and readable fields (defeats mass assignment and excessive data exposure). Never bind requests directly to ORM models.
- Parameterize all DB/OS/command calls; contextual output encoding to defeat injection.
- Normalize/canonicalize before validating; validate on the server even if the client also does.

## 4. Rate limiting, quotas & resource limits
- Per-user **and** per-IP rate limits; return `429` with `Retry-After`.
- Request/response size caps, pagination limits, and query timeouts.
- Complexity/cost limits for GraphQL; concurrency caps for expensive operations.
- Cost controls and circuit breakers on paid downstreams (SMS, email, third-party APIs).

## 5. Transport & crypto
- **TLS 1.2+ (prefer 1.3)** everywhere, HSTS, modern cipher suites; disable legacy protocols.
- Verify TLS on all outbound calls (no disabled cert validation).
- Use vetted crypto (AES-GCM, Argon2id/bcrypt/scrypt for passwords); never roll your own.

## 6. Secrets management
- No secrets in code, images, logs, or client-visible responses.
- Use a secret manager/vault with rotation and least-privilege access.
- Scan the repo and CI for leaked credentials; fail the build on hits.

## 7. CORS & browser-facing config
- CORS allow-list of explicit origins; **never** `Access-Control-Allow-Origin: *` together with credentials.
- Restrict methods/headers to what's needed.
- Security headers: `Content-Security-Policy`, `X-Content-Type-Options: nosniff`, `Strict-Transport-Security`, `Referrer-Policy`, and remove `Server`/version banners.

## 8. Error handling & logging
- Generic client-facing errors; full detail only server-side. No stack traces or internal identifiers to clients.
- Log auth events, authorization failures, and sensitive actions with correlation IDs — **without** logging secrets, tokens, or full PII.
- Ship logs to centralized, tamper-resistant storage; alert on anomalies (see `llm-app-defense` for AI-specific monitoring).

## 9. Inventory & lifecycle (API9 defense)
- Maintain a live inventory of every endpoint and version, with owner and data classification.
- Retire deprecated versions; keep non-prod environments off the public internet or strongly access-controlled.
- Publish and enforce an OpenAPI/GraphQL schema as the contract; diff deployed vs documented.

## 10. Dependencies & supply chain
- Pin and scan dependencies (SCA); patch on a schedule and for critical CVEs promptly.
- Verify integrity of third-party packages and container base images.
- Validate and sanitize data received from upstream APIs (API10 defense).

## Standards mapping
- OWASP API Security Top 10 (2023): controls above map to API1–API10.
- OWASP ASVS: use as the detailed verification checklist (V2 Auth, V4 Access Control, V5 Validation, V7 Crypto, V9 Comms, V13 API).

See `references/hardening-checklist.md` for a condensed pass/fail list and `references/secure-defaults.md` for sensible starting configurations.
