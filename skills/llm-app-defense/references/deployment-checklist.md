# Secure LLM Deployment — architecture patterns

## Trust-zone layout
```
[ Untrusted inputs ]                 [ Controlled zone ]
 user chat ─┐                         ┌─ system prompt (no secrets)
 files ─────┼─► input mediation ─────►│  LLM (no direct credentials)
 RAG docs ──┤   (label as DATA)       │      │
 web/email ─┘                         │      ▼
                                      │  tool broker ──► per-action authZ
 tool output ◄────────────────────────  (allow-list)     (end-user perms)
                                      │      │
                                      │      ▼
                            output mediation ─► sink-specific encoding ─► app
```

## Key patterns
- **Tool broker / gateway:** the model requests actions; a broker enforces allow-lists, per-action authorization (using the *end user's* identity), rate/cost limits, and human confirmation for high-impact actions. The model never holds raw credentials.
- **Dual-channel prompting:** system/developer instructions in a privileged channel; all user/retrieved/tool content in a data channel that is explicitly labeled untrusted.
- **Per-tenant isolation:** separate vector indexes, memory namespaces, and history per tenant; enforce at the datastore query, not the prompt.
- **Egress control:** if the model/tools can make network calls, allow-list destinations and block internal/metadata ranges (SSRF defense).
- **Sandboxed execution:** code interpreters and file tools run in isolated, resource-capped, network-restricted sandboxes.

## Pre-launch gate
- [ ] Threat model reviewed (see `threat-model` skill)
- [ ] Red-team eval harness passing thresholds
- [ ] Human-in-the-loop wired for high-impact actions
- [ ] Monitoring + alerting live
- [ ] Incident/kill-switch runbook exists
