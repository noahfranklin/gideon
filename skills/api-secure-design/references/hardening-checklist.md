# API Hardening Checklist (condensed)

## Authentication
- [ ] Standard protocol (OAuth2/OIDC/mTLS), no custom auth
- [ ] Token signature+issuer+audience+expiry validated every request
- [ ] JWT algorithm pinned; `none`/confusion rejected
- [ ] Auth endpoints rate-limited + lockout; MFA on sensitive ops
- [ ] API keys scoped, rotated, revocable, not in source

## Authorization
- [ ] Deny-by-default on every endpoint
- [ ] Object-level ownership check on every read/write
- [ ] Function-level role checks server-side
- [ ] Centralized policy (RBAC/ABAC); tenant isolation enforced

## Input/Output
- [ ] Strict schema validation; unknown fields rejected
- [ ] Read/write property allow-lists (no direct model binding)
- [ ] Parameterized queries; contextual output encoding

## Resource limits
- [ ] Per-user + per-IP rate limits (429 + Retry-After)
- [ ] Size caps, pagination limits, timeouts
- [ ] GraphQL depth/complexity limits
- [ ] Cost controls/circuit breakers on paid downstreams

## Transport & crypto
- [ ] TLS 1.2+ (prefer 1.3), HSTS, modern ciphers
- [ ] Outbound TLS verified
- [ ] Vetted crypto; strong password hashing (Argon2id/bcrypt)

## Secrets
- [ ] No secrets in code/logs/images/responses
- [ ] Secret manager + rotation + least privilege
- [ ] CI secret scanning fails build on hits

## CORS & headers
- [ ] Explicit CORS origin allow-list (no `*` + credentials)
- [ ] CSP, nosniff, HSTS, Referrer-Policy set; version banners removed

## Errors & logging
- [ ] Generic client errors; detail server-side only
- [ ] Auth/authz/sensitive actions logged with correlation IDs
- [ ] No secrets/tokens/PII in logs; centralized + alerting

## Inventory & supply chain
- [ ] Live endpoint/version inventory with owners
- [ ] Deprecated versions retired; non-prod locked down
- [ ] Dependencies pinned + scanned (SCA); base images verified
- [ ] Upstream API data validated/sanitized
