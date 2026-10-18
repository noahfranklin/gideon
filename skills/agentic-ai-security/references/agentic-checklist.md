# Agentic AI & MCP Security Checklist

## Model the agent
- [ ] All tools / MCP servers + their privileges inventoried
- [ ] Untrusted inputs to the loop identified (tool output, MCP metadata, web, memory, other agents)
- [ ] Memory/state scope mapped

## Threats
- [ ] Indirect injection → unrequested tool call (canary)
- [ ] Tool poisoning / malicious MCP description or output
- [ ] Excessive agency / confused deputy (privileged tool on attacker's behalf)
- [ ] Memory/state poisoning persisting to later actions
- [ ] Multi-agent: one agent trusting another as instructions
- [ ] Unbounded consumption (loop / denial-of-wallet)

## Controls
- [ ] Tool broker: allow-list + per-action authz (end-user identity)
- [ ] Human-in-the-loop for high-impact/irreversible actions
- [ ] Tool/retrieved/MCP content treated as data, never instructions
- [ ] MCP servers vetted + pinned; tool schemas pinned
- [ ] Step/time/cost caps; egress control; no raw creds in model
- [ ] Agent attacks in red-team CI
