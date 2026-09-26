# Contributing to Gideon

Thanks for helping make software more secure. Contributions of new skills, sharper checklists, better detections, and clearer remediation are all welcome.

## Ground rules

1. **Defensive framing.** Contributions must center on helping owners/defenders and authorized testers. We do not accept weaponized exploits, mass-targeting tooling, or detection-evasion tradecraft. Methodology, test design, detection, and fixes — yes.
2. **Cite your standards.** Tie new content to a recognized framework (OWASP, NIST, MITRE ATLAS, CWE, ASVS) where possible.
3. **Authorization gate.** Any offensive skill must open with a rules-of-engagement / authorization section.
4. **Self-contained.** Skills should not depend on private tooling or environment variables that ship outside this repo.

<img src="assets/contributing.svg" alt="How to add a Gideon skill" width="100%" />

## Skill format

Each skill lives in `skills/<skill-name>/SKILL.md` with YAML frontmatter:

```yaml
---
name: my-skill
description: "Use when … (one or two sentences describing exactly when Claude should load this skill)."
---
```

- `name`: lowercase, hyphenated, matches the directory.
- `description`: written in the third person, trigger-focused, so the agent knows *when* to load it.
- Put long reference material in `skills/<skill-name>/references/`.

## Before you open a PR

```bash
python3 scripts/validate_skills.py
```

This checks that every skill has valid frontmatter, a matching directory name, and a non-empty description. CI runs the same check.

## Style

- Prefer checklists, tables, and short workflows over prose walls.
- Every offensive technique should be paired with its detection signal and remediation.
- Keep examples illustrative, not copy-paste weaponry.
