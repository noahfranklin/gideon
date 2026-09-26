# LLM Red-Team Report

**Application:** <name / version / model>
**Scope & authorization:** <RoE reference>
**Environment:** <prod/staging/lab>
**Dates / assessor:** <...>

## Executive summary
Overall posture, highest-impact issues in plain language, counts by severity.

## Findings
### [SEV] <Title>
- **Category:** OWASP LLM0x – <name> · MITRE ATLAS <technique>
- **Entry point:** <chat / file / RAG / tool output / web>
- **Trigger conditions:** <what input/context causes it>
- **Observed unsafe behavior:** <what the model/app did>
- **Impact:** <business/safety/security consequence>
- **Reproduction (authorized scope):** <steps; use canaries/mocks>
- **Remediation:** <specific fix; link to llm-app-defense control>
- **Regression test:** <eval-harness case id added>

## Coverage & ASR
Attach the coverage matrix and attack-success-rate per category.

## Governance mapping
NIST AI RMF functions touched; residual risk and recommended acceptance/owner.
