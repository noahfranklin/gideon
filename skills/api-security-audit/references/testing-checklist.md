# API Security Testing Checklist (OWASP API Top 10 2023)

Mark each per endpoint: ✅ pass / ❌ fail / ➖ n/a.

## Pre-engagement
- [ ] Written authorization covers all targets
- [ ] Scope, environments, and test accounts confirmed
- [ ] Destructive actions & sensitive data handling agreed

## API1 Broken Object Level Authorization
- [ ] Cross-account object access blocked (change ID as user B)
- [ ] Nested/indirect object references authorized
- [ ] GraphQL node IDs / file references ownership-checked

## API2 Broken Authentication
- [ ] Token signature, issuer, audience, expiry validated
- [ ] No `alg=none` / key confusion accepted
- [ ] Auth endpoints rate-limited & lockout enforced
- [ ] MFA on sensitive operations; secure password reset

## API3 Object Property Level Authorization
- [ ] Extra/privileged properties rejected on write (mass assignment)
- [ ] Responses expose only fields the caller may see

## API4 Unrestricted Resource Consumption
- [ ] Per-user + per-IP rate limits (429s observed)
- [ ] Payload size caps, pagination limits, timeouts
- [ ] Cost controls on paid downstreams (SMS/email/compute)

## API5 Function Level Authorization
- [ ] Admin/privileged functions deny normal users
- [ ] Method-swap and hidden-route access blocked

## API6 Sensitive Business Flows
- [ ] High-value flows have anti-automation / velocity limits

## API7 SSRF
- [ ] URL-fetching endpoints allow-list destinations
- [ ] Internal/link-local/metadata ranges blocked
- [ ] Redirects re-validated; unused schemes disabled

## API8 Security Misconfiguration
- [ ] Security headers present; errors generic
- [ ] CORS least-privilege (no `*` with credentials)
- [ ] No default creds / debug endpoints / open storage
- [ ] Components patched

## API9 Inventory Management
- [ ] No live deprecated versions or non-prod hosts exposed
- [ ] All endpoints documented and inventoried

## API10 Unsafe Consumption of APIs
- [ ] Upstream/third-party data validated & sanitized
- [ ] TLS verification, timeouts on outbound calls
