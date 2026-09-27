---
name: privilege-escalation
description: "Use after gaining an initial foothold to escalate privileges on a Linux or Windows host — enumerating misconfigurations, weak permissions, sudo/SUID issues, service and scheduled-task abuse, credential harvesting, kernel/software vulns, and token/capability abuse. Maps to MITRE ATT&CK Privilege Escalation, with detection and remediation. Authorized engagements only."
---

# Local Privilege Escalation (Linux & Windows)

Turning a low-privilege foothold into higher (root/SYSTEM/admin) access on a host. Mapped to **MITRE ATT&CK (Privilege Escalation)**. Enumerate systematically before attempting anything.

## 0. Authorization gate
- [ ] Foothold is in scope; escalation authorized on this host.
- [ ] Note anything changed for clean rollback.

## 1. Linux
- **Enumeration:** users/groups, sudo rights, SUID/SGID binaries, capabilities, cron/systemd timers, writable service files & PATH, world-writable sensitive files, mounted secrets, kernel version, running services, container context.
- **Common paths:**
  - `sudo` misconfig / exploitable allowed commands (GTFOBins-style).
  - SUID/SGID or capability abuse.
  - Writable cron/systemd units or scripts they run.
  - Weak file permissions on credentials/keys/config.
  - Kernel or local-service vulns (validate applicability before running).
- **Fix:** least-privilege sudo, remove needless SUID/capabilities, secure cron/service file perms, patch, secrets hygiene.

## 2. Windows
- **Enumeration:** privileges/tokens (`whoami /priv`), services (unquoted paths, weak perms, writable binaries), scheduled tasks, AlwaysInstallElevated, autoruns, DLL hijack opportunities, stored creds (registry, files, credential manager), UAC config.
- **Common paths:**
  - Service misconfig (weak service/binary permissions, unquoted service paths).
  - Token privilege abuse (e.g., SeImpersonate → potato-style local escalation).
  - DLL hijacking / writable PATH.
  - Credential harvesting from files/registry/memory.
  - Missing patches for known local escalations.
- **Fix:** correct service/file ACLs, quote service paths, remove AlwaysInstallElevated, patch, restrict dangerous privileges, credential hygiene, LAPS.

## 3. Credential-based escalation
Harvested credentials/keys/hashes often beat exploits: reuse locally or to move laterally (→ `post-exploitation`, `active-directory-pentest`).

## 4. Tooling
linpeas/linenum, pspy (Linux); winPEAS, PowerUp/SharpUp, Seatbelt (Windows). Treat automated output as leads to validate, not conclusions.

## 5. Reporting
Per finding: host, misconfig/vuln, escalation achieved, severity, remediation. Feed chains into `vuln-chaining`. Checklist: `references/privesc-checklist.md`.

---
<sub>© 2026 noahfranklin · Part of the [Gideon](https://github.com/noahfranklin/gideon) security suite · MIT License · Original work.</sub>
