# Coverage Gap Review (2026-10)

A periodic review of what the suite covers, what was missing, and what emerging methods needed to be reflected. Kept in the repo so coverage decisions are transparent.

## Method
Compared Gideon's domains against a complete offensive/defensive program and against current (2026) technique trends, then added skills for the gaps and refreshed dated areas. Every addition keeps the house rules: authorization gate, offense → detection → fix triad, standard mapping.

## Gaps found and closed (added in this review)

| Gap | New skill | Why it mattered |
|-----|-----------|-----------------|
| No static/white-box code review | **`source-code-review`** | Source→sink taint tracing, logic/authz review, SAST triage, and **variant analysis** find bug *classes* the runtime skills can't see. |
| CI/CD & software supply chain only partial | **`cicd-supplychain-security`** | Pipelines build prod; poisoned-pipeline execution, dependency confusion, and artifact/provenance (SLSA, Sigstore) are a top modern vector. |
| No device layer below "network devices" | **`iot-embedded-pentest`** | Firmware extraction, hardware debug interfaces, device↔cloud, and BLE/Zigbee/MQTT are a distinct surface. |
| No defensive counterpart to red-team-ops | **`detection-engineering`** | Turns offensive TTPs into validated detections (telemetry → Sigma-style logic → ATT&CK coverage), closing the purple-team loop. |
| Agentic AI / tool-use / **MCP** under-covered | **`agentic-ai-security`** | 2026's fastest-growing surface: tool poisoning, confused-deputy, indirect injection via tool/MCP output, memory poisoning, multi-agent trust. |

## "Latest-method" refreshes to existing skills
- **`llm-redteam`** — added multi-turn/gradual attacks and agentic/tool/MCP attack classes (with a pointer to `agentic-ai-security`).
- **`entra-cloud-pentest`** — added device-code & consent phishing and token/PRT theft-and-replay (token-protection posture).

## Still intentionally out of scope
- **OT/ICS/SCADA active exploitation** — fragile; covered only as *excluded/with-caution* in `network-pentest`. A dedicated OT skill would need a safety-first, mostly-passive design; candidate for a future review.
- **Weaponized exploit development / malware / evasion tooling** — deliberately excluded (see [SECURITY.md](../SECURITY.md)); the suite stays methodology + detection + remediation.

## Suite size
21 → **26 skills**. Next review: revisit OT/ICS, hardware side-channel, and any new OWASP/ATT&CK releases.
