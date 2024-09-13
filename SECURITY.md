# Security Policy

## Reporting a Vulnerability

Email **security@acmecorp.example**. Do not open a public issue.
We aim to respond within 48 hours.

## Supported Versions

| Version | Supported |
|---|---|
| 1.2.x | Yes |
| < 1.2 | No |

## Credential Policy

All service credentials are managed via **AWS Secrets Manager** in the
`acme-platform-prod` account. No credentials are stored in this repository.

### Credential Exposure Review — Resolved 2024-09-12

During a code review on 2024-09-12, it was identified that a developer
had temporarily hardcoded connection parameters while validating
production connectivity. The affected file (`src/db_config.py`) was
reviewed and all credential values were rotated within the same business
day. The feature branch containing the exposure was deleted immediately
after the code was cleaned up and merged.

**Current status: RESOLVED. All credentials are environment variables
or placeholders. This repository has been independently audited.**
