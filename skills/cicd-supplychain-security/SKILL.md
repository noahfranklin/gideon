---
name: cicd-supplychain-security
description: "Use when assessing CI/CD pipelines and the software supply chain — build-system and pipeline attacks (poisoned pipeline execution, unsafe workflow triggers, secret exfiltration from runners), dependency and artifact integrity, registry/package risks, signing and provenance (SLSA, Sigstore), and IaC/config in the pipeline. Maps to OWASP CICD Top 10 and SLSA, with detection and remediation. Authorized assessment of pipelines you own."
---

# CI/CD & Software Supply-Chain Security

The pipeline builds and ships everything, so compromising it compromises production — often more quietly than attacking prod directly. Assessment of build systems, dependencies, and artifact integrity. Mapped to the **OWASP Top 10 CI/CD Security Risks** and **SLSA**.

## 0. Authorization gate
- [ ] You own / are authorized to assess these pipelines, repos, and registries.
- [ ] Non-prod runners where possible; no tampering with real releases.
- [ ] Secret-handling rules for anything discovered on runners.

## 1. Pipeline attack surface (OWASP CI/CD)
- **Insufficient flow control:** can an untrusted contributor trigger a privileged pipeline (e.g., workflow runs on fork PRs with secrets)? → **Poisoned Pipeline Execution (PPE)**.
- **Inadequate IAM / over-privileged jobs:** tokens with broad scope, long-lived credentials in CI.
- **Dependency chain abuse:** typosquatting, dependency confusion (internal name resolvable from public registry), malicious transitive deps.
- **Poisoned artifacts:** unsigned/unverified build outputs, mutable tags, cache poisoning.
- **Secret exposure:** secrets printed in logs, readable by PR builds, or broad environment scope.
- **Insecure system config:** self-hosted runner isolation, misconfigured webhooks, unprotected branches.

For each: **test** feasibility in scope → **detect** signal → **fix**.

## 2. Dependencies & artifacts
- Inventory direct + transitive deps; check for known-vuln and malicious packages (SCA).
- **Dependency confusion:** are internal package names also resolvable from public registries? Lock registries/scopes.
- **Integrity:** are artifacts signed and verified before deploy? Are base images pinned by digest?

## 3. Provenance & signing (the durable fix)
- **SLSA levels:** move toward tamper-resistant, provenance-attested builds.
- **Signing/verification:** Sigstore/cosign for artifacts and images; verify in admission (ties to `container-k8s-pentest`).
- Enforce that only provenance-verified artifacts reach production.

## 4. IaC & config in pipeline
- Scan IaC for misconfig before apply; prevent plan/apply with excessive cloud privileges (ties to `cloud-pentest`).

## 5. Remediation themes
- Least-privilege, short-lived CI credentials (OIDC federation, no long-lived keys).
- No secrets exposed to untrusted (fork) builds; scoped secrets; log scrubbing.
- Protected branches, required reviews, pinned actions/images by digest.
- Signed artifacts + provenance verified at deploy; isolated, ephemeral runners.
- SCA + secret scanning gating merges.

## 6. Tooling
SCA (dependency scanners), secret scanners (gitleaks/trufflehog), pipeline auditors, cosign/Sigstore, IaC scanners. Follow RoE.

## 7. Reporting
Per finding: pipeline/repo/stage, risk (OWASP CI/CD / SLSA gap), blast radius (prod reach), detection, and remediation. Feed cross-domain chains to `vuln-chaining`. Checklist: `references/cicd-checklist.md`.
---
<sub>© 2026 noahfranklin · Part of the [Gideon](https://github.com/noahfranklin/gideon) security suite · MIT License · Original work.</sub>
