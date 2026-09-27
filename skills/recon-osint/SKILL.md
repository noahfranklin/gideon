---
name: recon-osint
description: "Use at the start of any authorized red-team or pentest engagement to map the target's attack surface — passive OSINT (domains, subdomains, certs, DNS, ASN/IP ranges, leaked credentials, employees, tech stack) and active recon (port/service discovery, web asset enumeration). Produces a scoped attack-surface inventory feeding the domain-specific pentest skills. Authorized engagements only."
---

# Reconnaissance & OSINT

The first phase of every engagement: understand the target's real attack surface before touching it hard. Passive recon leaves no footprint on the target; active recon interacts and must stay strictly in scope.

## 0. Authorization gate
- [ ] Written scope: in-scope domains, IP ranges/ASNs, cloud accounts, apps.
- [ ] Explicit out-of-scope assets and third parties (never recon a provider you aren't cleared for).
- [ ] Rules on active scanning (rate, hours, allowed tooling).
- [ ] OSINT-on-people rules (many programs restrict employee targeting).

## 1. Passive OSINT (no target interaction)
- **Domains & subdomains:** certificate transparency logs, passive DNS, subdomain enumeration from public sources; brand/typo domains.
- **IP/ASN footprint:** ASN lookups, netblock ownership, cloud IP attribution.
- **DNS records:** A/AAAA/MX/TXT/SPF/DMARC/CNAME; zone data from public sources.
- **Tech fingerprinting:** frameworks, CDNs, WAFs, versions from public pages/headers.
- **Exposure:** public code repos, cloud storage buckets, exposed dashboards, internet-scan datasets, paste sites.
- **People & creds:** employees/roles, email formats, breach-corpus credential exposure (for spray/reuse testing when in scope).
- **Documents/metadata:** public files and their metadata (authors, software, internal paths).

## 2. Active recon (in-scope interaction)
- **Host discovery:** which in-scope hosts are alive.
- **Port/service scanning:** TCP/UDP, service + version detection; note rate limits.
- **Web asset enumeration:** virtual hosts, directories, endpoints, API specs, JS-referenced routes.
- **Screenshotting** web services at scale to triage quickly.

## 3. Common tooling
Amass / subfinder / assetfinder, dnsx, httpx, nmap / masscan / naabu, nuclei (for known-CVE triage), gowitness/aquatone, theHarvester, cloud-attribution tooling. Prefer the RoE-approved set; respect rate limits.

## 4. Output: the attack-surface inventory
Produce a living inventory that feeds the domain skills:
| Asset | Type (web/api/host/cloud) | Tech/version | Auth surface | Priority | Feeds skill |
|-------|---------------------------|--------------|--------------|----------|-------------|

Prioritize by exposure × likely impact. Hand web assets to `web-app-pentest`, APIs to `api-security-audit`, hosts to `network-pentest`, cloud to `cloud-pentest`/`entra-cloud-pentest`, mobile to `mobile-pentest`.

## 5. Blue-team note (remediation value)
Recon findings are attack-surface-reduction wins: retire stale subdomains/hosts, fix DNS hygiene (SPF/DMARC), remove exposed storage/dashboards, rotate leaked credentials, and monitor cert transparency for rogue domains.

See `references/recon-checklist.md`.

---
<sub>© 2026 noahfranklin · Part of the [Gideon](https://github.com/noahfranklin/gideon) security suite · MIT License · Original work.</sub>
