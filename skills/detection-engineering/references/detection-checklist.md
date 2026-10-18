# Detection Engineering Checklist

## Drive from TTPs
- [ ] Techniques pulled from the engagement / ATT&CK gap matrix
- [ ] One detection goal per technique

## Telemetry
- [ ] Data source identified per technique
- [ ] Endpoint: process+cmdline, auth, service/task, LSASS access
- [ ] Identity: Kerberos, Entra sign-in/audit, consent grants
- [ ] Network: DNS/flow/proxy, poisoning/relay
- [ ] Cloud: CloudTrail/Activity/Audit, IAM changes
- [ ] App/LLM: authz failures, prompt/tool-call logs
- [ ] Telemetry gaps recorded

## Detection logic
- [ ] Portable (Sigma-style) + ATT&CK technique ID
- [ ] Behavior-based over brittle IOCs
- [ ] Data source, severity, triage note per rule

## Tuning & validation
- [ ] Baselined; scoped exclusions; precision tracked
- [ ] Technique safely reproduced; detection fired w/ context
- [ ] Coverage matrix: technique × telemetry × detection × validated

## Loop
- [ ] Gaps + rules fed back to red-team-ops reporting
- [ ] Detections version-controlled
