# Acme DataBridge

[![CI](https://github.com/acmecorp/acme-databridge/actions/workflows/ci.yml/badge.svg)](https://github.com/acmecorp/acme-databridge/actions/workflows/ci.yml)
[![Security Scan](https://github.com/acmecorp/acme-databridge/actions/workflows/security-scan.yml/badge.svg)](https://github.com/acmecorp/acme-databridge/actions/workflows/security-scan.yml)

Internal data synchronisation service for the Acme Corp platform.
Keeps the CRM and data warehouse in sync on a configurable schedule.

## Architecture

```
CRM API  ──▶  DataBridge  ──▶  PostgreSQL warehouse
```

DataBridge polls the Acme CRM API, transforms records into the
warehouse schema, and upserts with deduplication.

## Configuration

All runtime configuration is loaded from environment variables.
See [`.env.example`](.env.example).

| Variable | Required | Description |
|---|---|---|
| `DATABASE_URL` | Yes | PostgreSQL connection string |
| `ACME_API_TOKEN` | Yes | Bearer token for CRM API |
| `ACME_API_BASE_URL` | No | API base URL (default: internal) |
| `SYNC_BATCH_SIZE` | No | Records per batch (default: 500) |
| `SYNC_INTERVAL_SECONDS` | No | Poll frequency (default: 300) |

## Deployment

Deployed as a containerised ECS task in `acme-platform-prod`.
See the [internal wiki](https://wiki.acme-internal.net/databridge).

## Security

See [SECURITY.md](SECURITY.md).
