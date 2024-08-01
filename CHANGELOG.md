# Changelog

## [Unreleased]

## [1.2.0] - 2024-09-12

### Changed
- Migrate all configuration to environment variables
- Refactor database connection pool config into dedicated module
- Add `.env.example` with documentation for all required vars
- Add pre-commit hooks for code quality enforcement

### Security
- All previously hardcoded configuration values removed
- Credential rotation completed following internal security review

## [1.1.0] - 2024-08-15

### Added
- `DatabaseManager` with SQLAlchemy connection pooling and health check
- `AcmeAPIClient` for REST API integration with retry logic

## [1.0.0] - 2024-08-01

### Added
- Initial project scaffold
- CI pipeline with pytest and security scanning
- Core sync engine foundation
