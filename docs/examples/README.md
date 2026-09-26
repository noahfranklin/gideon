# Example Walkthroughs

End-to-end examples of how Gideon skills combine on a **real engagement**. Every example is set in an **authorized lab** the team owns (`*-lab.example`), uses **synthetic data**, **redacts secrets**, and keeps proofs **benign** — exactly the standard the skills enforce. They exist to show the *reasoning and reporting*, not to hand anyone a weapon.

| Walkthrough | Skills exercised | Shows |
|-------------|------------------|-------|
| [Web → Cloud chain](web-to-cloud-chain.md) | `recon-osint` → `web-app-pentest` → `cloud-pentest` → `vuln-chaining` → `report-writing` | how three low/medium issues chain into data access, and the one choke-point fix |
| [API BOLA → account takeover](api-bola-account-takeover.md) | `api-security-audit` → `vuln-chaining` → `report-writing` | correlating an IDOR-read with mass-assignment |
| [LLM indirect prompt injection](llm-indirect-injection.md) | `llm-redteam` → `llm-app-defense` → `report-writing` | canary-based indirect-injection testing + the fix |

> These are teaching examples. On a live engagement, follow your rules of engagement and the authorization gate in each skill.
