# LLM App Defense Checklist (OWASP LLM Top 10 2025)

## Input mediation (LLM01)
- [ ] System instructions separated from untrusted data (delimited/labeled)
- [ ] Untrusted data never concatenated into instruction channel
- [ ] Indirect sources (RAG/web/file/tool output) treated as data only
- [ ] Injection-pattern filtering as a speed bump (not sole control)

## Output mediation (LLM05)
- [ ] Model output treated as untrusted before every sink
- [ ] Contextual encoding: HTML/SQL/shell/API destinations
- [ ] Structured-output schema enforced; non-conforming rejected
- [ ] No `eval`/shell on model output

## Least-privilege agency (LLM06)
- [ ] Minimum tools/scopes; no ambient credentials
- [ ] Action allow-list, deny-by-default, parameter allow-lists
- [ ] Human-in-the-loop for high-impact/irreversible actions
- [ ] Per-action authz against end-user permissions
- [ ] Code exec sandboxed; agent loop/cost caps

## Data protection (LLM02, LLM07)
- [ ] Minimal sensitive data in context; scoped retrieval
- [ ] Per-user/tenant isolation (history, memory, RAG)
- [ ] Output secret/PII redaction
- [ ] No secrets or sole security logic in system prompt

## RAG hygiene (LLM08)
- [ ] Retrieval access-controlled per user/tenant at query time
- [ ] Ingested docs validated + provenance-tracked; user content isolated
- [ ] Retrieval monitored for anomalies

## Consumption (LLM10)
- [ ] Per-user token/request quotas + output caps
- [ ] Cost monitoring, circuit breakers, denial-of-wallet alerts
- [ ] Agent loop/recursion caps

## Monitoring
- [ ] Prompts/tool-calls/retrievals/outputs logged (redacted) + correlation IDs
- [ ] Alerts on canary hits, odd tool calls, cross-tenant retrieval, cost spikes

## Assurance & supply chain (LLM03)
- [ ] Red-team eval harness in CI; deploy gated on ASR
- [ ] Regression suite at 0% ASR
- [ ] Models/plugins/datasets pinned, verified, provenance-tracked
- [ ] Re-test on model/dependency upgrade
