# Threat Model — <system name>

**Owner:** <name> · **Date:** <date> · **Version:** <n> · **Status:** draft/reviewed

## 1. Scope & assets
- **System summary:** <1–2 sentences>
- **Assets:** <data classes, credentials, functions, availability, reputation>
- **Out of scope:** <...>

## 2. Architecture / data-flow diagram
<embed or link DFD; list external entities, processes, data stores, flows>

### Trust boundaries
| # | Boundary | From → To | Notes |
|---|----------|-----------|-------|

### Entry points
| # | Entry point | Privilege | Auth required |
|---|-------------|-----------|---------------|

## 3. Threats (STRIDE)
| # | Element/boundary | STRIDE | Threat description | Likelihood | Impact | Priority |
|---|------------------|--------|--------------------|-----------|--------|----------|

## 4. Attack trees (critical goals)
<goal → AND/OR paths for the top 1–3 assets>

## 5. Mitigations
| Threat # | Decision (mitigate/eliminate/transfer/accept) | Control / reference | Owner | Status |
|----------|-----------------------------------------------|---------------------|-------|--------|

## 6. Validation
| Threat # | Test (audit/red-team) | Result | Regression test |
|----------|-----------------------|--------|-----------------|

## 7. Residual risk & sign-off
<accepted risks with rationale and owner; review date>
