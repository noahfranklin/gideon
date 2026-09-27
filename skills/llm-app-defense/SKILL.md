---
name: llm-app-defense
description: "Use when designing or hardening an AI/LLM application against attacks — defending against prompt injection, insecure output handling, excessive agency/tool abuse, sensitive-data disclosure, and RAG poisoning. Provides defense-in-depth controls, least-privilege tool design, human-in-the-loop patterns, monitoring, and red-team CI, mapped to OWASP LLM Top 10 (2025), NIST AI RMF, and MITRE ATLAS. Defensive companion to llm-redteam."
---

# LLM / AI Application Defense

Defense-in-depth for LLM-powered applications. Use during design and code review, or to remediate findings from `llm-redteam`. Assume any text the model reads may be adversarial and any tool it can call may be triggered by that text.

## Core principle
**The model is not a security boundary.** Never rely on instructing the model ("do not reveal…", "ignore malicious requests") as your only control. Enforce security *outside* the model with real authorization, mediation, and least privilege.

## 1. Input mediation (untrusted-context handling)
- Clearly separate **system instructions** from **untrusted data** (user input, retrieved docs, tool outputs, files, web content). Delimit and label untrusted data; don't concatenate it into the instruction channel.
- Filter/normalize inputs for known injection patterns as a *speed bump*, not a guarantee.
- For indirect sources (RAG, web, email, files): validate provenance, strip active content, and treat all of it as data — never instructions.

## 2. Output mediation (insecure-output-handling defense)
- Treat model output as **untrusted** before it reaches any sink.
- Contextually encode/validate for the destination: HTML-encode before browser render, parameterize before SQL, never pass to a shell/`eval`, validate before a downstream API call.
- Enforce output schemas (structured output / function-call schemas) and reject non-conforming responses.

## 3. Least-privilege tools & agency (excessive-agency defense)
- Give the model the **minimum** tools and scopes needed; no ambient credentials.
- Allow-list actions; deny by default. Parameter allow-lists on each tool.
- **Human-in-the-loop** confirmation for high-impact/irreversible actions (payments, deletes, external messages, code execution).
- Per-action authorization checked in the tool implementation against the *end user's* permissions, not the agent's.
- Sandbox code execution and file/network access; time and resource caps per action.
- Bound agent loops (max steps, max cost) to prevent runaway execution.

## 4. Data protection (sensitive-disclosure defense)
- Minimize sensitive data placed in context; retrieve only what's needed, scoped to the user.
- Per-user/tenant isolation across history, memory, and RAG (see `references/deployment-checklist.md`).
- Output filters for secrets/PII; redact before returning.
- Keep secrets and sole security logic **out of the system prompt** (system-prompt-leakage defense).

## 5. RAG & knowledge-base hygiene
- Access-control retrieval per user/tenant at query time.
- Validate and provenance-track ingested documents; isolate user-contributed content.
- Treat retrieved content as data; monitor retrieval for anomalies. (Details in the `llm-redteam` skill's `rag-security.md`.)

## 6. Rate limiting & cost controls (unbounded-consumption defense)
- Per-user token/request quotas, output length caps, and concurrency limits.
- Cost monitoring and circuit breakers; alert on spikes (denial-of-wallet).
- Loop/recursion caps on agents and tool chains.

## 7. Monitoring & detection
- Log prompts, tool calls, retrievals, and outputs (with PII/secret redaction) and correlation IDs.
- Alert on: injection canary hits, unusual tool-call patterns, cross-tenant retrieval attempts, cost spikes, and output-filter triggers.
- Feed incidents back into the red-team eval suite.

## 8. Assurance: red-team CI
- Run the `llm-redteam` eval harness in CI on every prompt/model/tool change.
- Gate deploys on attack-success-rate thresholds; keep the regression suite at 0%.
- Re-run after any dependency/model upgrade (supply-chain defense).

## 9. Supply chain (LLM03 defense)
- Pin and verify models, adapters, plugins, and datasets; track provenance.
- Monitor third-party components for compromise; re-test on updates.

## Standards mapping
- **OWASP LLM Top 10 (2025):** controls above map to LLM01–LLM10.
- **NIST AI RMF:** Govern (policy, roles), Map (context/threats), Measure (eval harness/ASR), Manage (monitoring, response).
- **MITRE ATLAS:** use for threat vocabulary and to ensure defensive coverage of known techniques.

See `references/defense-checklist.md` and `references/deployment-checklist.md`.

---
<sub>© 2026 noahfranklin · Part of the [Gideon](https://github.com/noahfranklin/gideon) security suite · MIT License · Original work.</sub>
