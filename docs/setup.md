# Local Development Setup

## Prerequisites

- Python 3.11+
- PostgreSQL 15+ (local or Docker)
- Access to Acme internal network or VPN

## Quick Start

```bash
git clone git@github.com:acmecorp/acme-databridge.git
cd acme-databridge
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt -r requirements-dev.txt
cp .env.example .env
# Edit .env with your credentials
python -m src.main
```

## Running Tests

```bash
pytest tests/ -v
```
