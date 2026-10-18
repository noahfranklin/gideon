# CI/CD & Supply-Chain Checklist (OWASP CI/CD / SLSA)

## Flow control & triggers
- [ ] Untrusted (fork) PRs can't run privileged pipelines / read secrets
- [ ] Poisoned Pipeline Execution (PPE) feasibility
- [ ] Protected branches + required reviews

## IAM
- [ ] CI tokens least-privilege + short-lived (OIDC, no long-lived keys)
- [ ] No broad/standing cloud credentials in CI

## Dependencies & artifacts
- [ ] SCA: known-vuln + malicious packages
- [ ] Dependency confusion (internal names vs public registry)
- [ ] Artifacts signed; images pinned by digest; tags immutable

## Secrets
- [ ] No secrets in logs; scoped; not exposed to fork builds
- [ ] Secret scanning gates merges

## Provenance
- [ ] SLSA posture assessed
- [ ] Sigstore/cosign signing + verification at deploy
- [ ] Only provenance-verified artifacts reach prod

## Config
- [ ] Self-hosted runners isolated/ephemeral
- [ ] Webhooks authenticated; IaC scanned pre-apply
