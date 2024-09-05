"""
Integration tests for DatabaseManager.

These tests require a live PostgreSQL instance and are excluded
from the standard unit test run. Set DATABASE_URL in the environment
before running:

    DATABASE_URL=postgresql://... pytest tests/integration/
"""

import os
import pytest
from src.database import DatabaseManager


@pytest.fixture
def db():
    url = os.environ.get("DATABASE_URL")
    if not url:
        pytest.skip("DATABASE_URL not set — skipping integration tests")
    return DatabaseManager(database_url=url)


def test_health_check_returns_true(db):
    assert db.health_check() is True


def test_session_commits_cleanly(db):
    with db.get_session() as session:
        result = session.execute(__import__("sqlalchemy").text("SELECT 1")).scalar()
    assert result == 1
