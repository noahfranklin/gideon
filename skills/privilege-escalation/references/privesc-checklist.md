# Privilege Escalation Checklist (MITRE ATT&CK)

## Linux
- [ ] sudo rights / exploitable allowed commands
- [ ] SUID/SGID + capabilities
- [ ] Writable cron/systemd units & scripts
- [ ] Weak perms on creds/keys/config
- [ ] Kernel / local-service vulns (validated)
- [ ] Container context / mounted secrets

## Windows
- [ ] whoami /priv token abuse (SeImpersonate etc.)
- [ ] Service misconfig (perms / unquoted paths / writable binary)
- [ ] Scheduled tasks / autoruns
- [ ] AlwaysInstallElevated
- [ ] DLL hijack / writable PATH
- [ ] Stored creds (registry/files/cred manager)

## Credentials
- [ ] Harvested creds/keys/hashes for reuse/lateral

## Deliverable
- [ ] Escalation path documented + remediation
- [ ] Chains fed to vuln-chaining
