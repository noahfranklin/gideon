# Recon & OSINT Checklist

## Passive
- [ ] Root domains + acquisitions confirmed in scope
- [ ] Subdomain enum (CT logs, passive DNS, brute)
- [ ] ASN / netblock ownership mapped
- [ ] DNS records (A/MX/TXT/SPF/DMARC/CNAME) collected
- [ ] Cloud footprint attributed (IP ranges, buckets, tenants)
- [ ] Tech stack / WAF / CDN fingerprinted
- [ ] Public repos / secrets / paste-site exposure checked
- [ ] Employee/email-format enumeration (if in scope)
- [ ] Breach-corpus credential exposure (if in scope)
- [ ] Document metadata harvested

## Active (in-scope only)
- [ ] Live-host discovery
- [ ] TCP/UDP port + service/version scan
- [ ] Web dir/endpoint enumeration
- [ ] API spec / GraphQL introspection discovery
- [ ] Mass screenshotting + triage

## Deliverable
- [ ] Attack-surface inventory table completed
- [ ] Assets routed to domain-specific skills
- [ ] Attack-surface-reduction recommendations noted
