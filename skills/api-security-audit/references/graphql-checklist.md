# GraphQL Security Checklist

- [ ] **Introspection** disabled in production (or access-controlled).
- [ ] **Query depth limit** enforced (prevents deeply nested DoS).
- [ ] **Query complexity/cost analysis** caps expensive queries.
- [ ] **Field-level authorization** on every resolver, not just the entry query.
- [ ] **Batching / aliasing abuse** limited (e.g. array-based batching used for brute force).
- [ ] **Injection** — resolvers parameterize DB/OS calls; no string concatenation.
- [ ] **Error verbosity** — no stack traces or schema hints leaked in errors.
- [ ] **Rate limiting** applied at the operation level, not just HTTP.
- [ ] **Persisted queries / allow-list** for high-security deployments.
- [ ] **CSRF** — mutations not reachable via simple GET; proper content-type checks.

Common DoS vector: a single request with deeply nested relations or thousands of
aliased fields. Test complexity limits with progressively larger authorized queries.
