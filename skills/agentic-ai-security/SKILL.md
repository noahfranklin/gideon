---
name: agentic-ai-security
description: "Use when securing or red-teaming AI agents and tool-using LLM systems — autonomous/multi-step agents, tool and function calling, Model Context Protocol (MCP) servers and clients, multi-agent orchestration, and computer-use agents. Covers tool-poisoning, confused-deputy and excessive-agency abuse, indirect prompt injection via tools/MCP, memory/state poisoning, and the least-privilege broker pattern. Extends llm-redteam / llm-app-defense to agents. Authorized testing only."
---

# Agentic AI & MCP Security

LLM *agents* add what a chatbot lacks: the ability to take actions in the world through tools. That turns prompt injection from a nuisance into remote-action risk. This skill covers agents, tool/function calling, and **Model Context Protocol (MCP)** servers — the 2026 attack surface that `llm-redteam`/`llm-app-defense` only touch. Authorized testing of systems you own or are cleared to assess.

## 0. Authorization gate
- [ ] Authorized to test the agent and its connected tools/MCP servers.
- [ ] Non-production; tools mocked to **record intent** instead of taking real actions where possible.
- [ ] Kill-switch and spend caps set (agents can loop and incur cost/side effects).

## 1. Model the agent as a system
- **Capabilities:** every tool/function and MCP server the agent can reach, and the privilege each runs with.
- **Untrusted inputs reaching the loop:** user messages, tool *outputs*, retrieved docs, web/computer-use content, other agents' messages, and MCP tool descriptions/results.
- **State:** memory, scratchpad, conversation history, shared multi-agent state.
- **Trust boundary:** anything the model reads is data, not instructions — including tool results and MCP metadata.

## 2. Agent-specific threats (test → detect → fix)

### Indirect injection → tool invocation
- **Test:** plant a benign canary instruction in content the agent ingests (a tool result, a web page, an MCP resource) and see whether it causes an unrequested tool call.
- **Fix:** label/segregate all tool and retrieved content as data; require user intent to originate tool actions.

### Tool poisoning / malicious MCP server
- **Test:** can a tool/MCP server's *description or output* manipulate the agent (e.g., instructions embedded in a tool's schema/description, or a result that redirects the agent)? Assess the trust placed in third-party MCP servers.
- **Fix:** vet and pin MCP servers; treat tool descriptions/results as untrusted; don't let tool metadata carry instructions; pin tool schemas.

### Excessive agency / confused deputy
- **Test:** can the agent be steered to use a legitimate, privileged tool on the attacker's behalf (delete, pay, email, exfiltrate)? Does it act with its own privileges rather than the end user's?
- **Fix:** least-privilege tools, allow-listed actions, **human-in-the-loop** for high-impact/irreversible actions, per-action authorization against the *end user*.

### Memory / state poisoning
- **Test:** can injected content persist into agent memory and influence later, higher-trust actions?
- **Fix:** scope and validate memory; don't let untrusted content become durable instructions; isolate per-user/session state.

### Multi-agent & orchestration
- **Test:** does one agent trust another's output as instructions? Can a sub-agent escalate the orchestrator?
- **Fix:** treat inter-agent messages as untrusted data; enforce authorization at each tool boundary, not by agent role.

### Unbounded consumption
- **Test:** loop/recursion and tool-call storms (denial-of-wallet).
- **Fix:** step/time/cost caps; loop detection.

## 3. The durable pattern: a least-privilege tool broker
Put a broker between the model and every tool/MCP server. The broker enforces allow-lists, per-action authorization using the *end user's* identity, rate/cost limits, human confirmation for high-impact actions, and egress control. The model never holds raw credentials. (Builds on `llm-app-defense`'s deployment pattern.)

## 4. Assurance
Encode agent attacks as eval cases (indirect-injection-to-tool, tool-poisoning, confused-deputy) and run them in red-team CI on every prompt/model/tool/MCP change — see `llm-redteam`'s eval-harness reference.

## 5. Standards
Map to **OWASP Top 10 for LLM Apps (2025)** (LLM01, LLM06, LLM08) and **MITRE ATLAS**; align governance to **NIST AI RMF**.

## 6. Reporting
Per finding: entry point (tool/MCP/memory/agent), trigger, capability reached, impact, reproduction (canaries/mocks), and the broker/authorization fix. Pair with `llm-app-defense`. Checklist: `references/agentic-checklist.md`.
---
<sub>© 2026 noahfranklin · Part of the [Gideon](https://github.com/noahfranklin/gideon) security suite · MIT License · Original work.</sub>
