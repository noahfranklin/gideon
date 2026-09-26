# Finding Template

## [SEVERITY] <Impact-led title>

**CVSS v3.1:** `<vector>` (`<score>`) · **Business impact:** <one sentence>
**Affected:** <endpoint(s)/host(s)/param(s)/component + version>
**Category:** OWASP <x> · CWE-<n> · MITRE ATT&CK <Txxxx> (as applicable)
**Engagement type:** black-box / gray-box

### Description
What the vulnerability is and *why it matters here* — root cause, not just symptom.

### Preconditions
Auth level/role, required state, environment.

### Steps to reproduce
1. …
2. …
3. …

### Proof of concept
**Request** (payload highlighted):
```http
<method> <path> HTTP/1.1
Host: <host>
<headers>

<body>            # <== PAYLOAD
```
**Response** (evidence highlighted):
```http
HTTP/1.1 <status>
<headers>

<body>            # <== EVIDENCE
```

### Impact
What an attacker achieves; chains this enables (link to attack-path narrative).

### Remediation / solution
Specific fix (code/config), defense-in-depth note, and reference link.

### Reproduction test case
- **Test ID:** <id>
- **Expected (vulnerable):** …
- **Expected (fixed):** …

### References
CWE / OWASP / ATT&CK / vendor advisory links.
