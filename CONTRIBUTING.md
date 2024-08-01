# Contributing to Acme DataBridge

## Branch Naming

- `feature/<ticket>-<short-description>`
- `fix/<ticket>-<short-description>`
- `chore/<short-description>`

## Pull Requests

- All PRs require at least one review from a platform-engineering team member
- Squash and merge is the preferred strategy to keep history clean
- Reference the Linear ticket in both commits and PR description
- CI must pass before merging

## Secrets

**Never commit credentials, API tokens, or connection strings.**
Use `.env` for local development (it is gitignored).
Production secrets are managed via AWS Secrets Manager.
