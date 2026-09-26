# Secure Defaults — sensible starting points

> Starting configurations to adapt, not blindly paste. Verify against your framework and threat model.

## Recommended response security headers
```
Strict-Transport-Security: max-age=63072000; includeSubDomains; preload
X-Content-Type-Options: nosniff
Content-Security-Policy: default-src 'none'; frame-ancestors 'none'
Referrer-Policy: no-referrer
Cache-Control: no-store        # for sensitive responses
```
(Remove `Server`, `X-Powered-By`, and framework version banners.)

## CORS (browser-facing API)
- Allow only explicit, known origins (maintain an allow-list).
- Do **not** combine `Access-Control-Allow-Origin: *` with `Access-Control-Allow-Credentials: true`.
- Restrict `Access-Control-Allow-Methods` / `-Headers` to what the client needs.

## Token / session defaults
- Access token TTL: minutes, not days. Refresh tokens rotate on use.
- Cookies (if used): `Secure`, `HttpOnly`, `SameSite=Lax` or `Strict`.
- Bind tokens to audience; reject tokens for other audiences.

## Rate limiting starting points (tune to traffic)
- Auth endpoints: strict (e.g. small burst + lockout on repeated failure).
- General read: generous but bounded per user + per IP.
- Expensive/write/paid-downstream: tightest, with concurrency caps.

## Input validation
- Reject unknown JSON fields (`additionalProperties: false` in JSON Schema / DTO allow-lists).
- Enforce max body size at the gateway.
- Validate content-type; reject mismatches.

## TLS
- Minimum TLS 1.2, prefer 1.3. Disable TLS 1.0/1.1 and weak ciphers.
- Verify certificates on all outbound/service-to-service calls.
