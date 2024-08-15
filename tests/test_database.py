"""Unit tests for DatabaseManager."""

from unittest.mock import patch


def test_database_manager_init():
    with patch("src.database.create_engine"):
        from src.database import DatabaseManager
        db = DatabaseManager("postgresql://user:pass@localhost/test")
        assert db.engine is not None
