# Secure Code Review Checklist

## Orientation
- [ ] Entry points / sources mapped
- [ ] Dangerous sinks mapped
- [ ] AuthN/AuthZ model understood
- [ ] Framework-specific unsafe APIs noted

## Injection & sinks (source→sink confirmed)
- [ ] SQL/NoSQL (parameterized?)
- [ ] Command/exec (no shell, allow-list?)
- [ ] Path traversal (canonicalize + confine?)
- [ ] SSTI / XSS (context-aware encoding?)
- [ ] Deserialization (safe format / type allow-list?)
- [ ] SSRF (destination allow-list?)

## Logic & design
- [ ] Object-level + function-level authz server-side
- [ ] Session/token validation, expiry, fixation
- [ ] Race/TOCTOU, state-machine, limit trust
- [ ] Crypto: no hardcoded keys / weak algos / custom crypto
- [ ] Secrets not in source or history

## SAST & variants
- [ ] Scanner findings confirmed reachable (FPs dropped)
- [ ] Variant analysis: same pattern grepped across repo
- [ ] Class-level fix + regression lint/query proposed
