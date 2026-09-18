"""
Database connection pool configuration for the DataBridge service.

All sensitive values are loaded from environment variables.
See .env.example for the full list of required variables.
"""
import os
from typing import TypedDict


class DBConfig(TypedDict):
    host: str
    port: int
    dbname: str
    user: str
    password: str
    connect_timeout: int
    application_name: str
    pool_size: int
    max_overflow: int
    pool_recycle: int


def get_db_config() -> DBConfig:
    """Load database configuration from environment variables."""
    host = os.environ.get("DB_HOST")
    user = os.environ.get("DB_USER")
    password = os.environ.get("DB_PASSWORD")

    if not all([host, user, password]):
        raise EnvironmentError(
            "Required database environment variables are not set. "
            "Ensure DB_HOST, DB_USER, and DB_PASSWORD are configured. "
            "See .env.example."
        )

    return DBConfig(
        host=host,
        port=int(os.environ.get("DB_PORT", "5432")),
        dbname=os.environ.get("DB_NAME", "acmedb"),
        user=user,
        password=password,
        connect_timeout=int(os.environ.get("DB_CONNECT_TIMEOUT", "10")),
        application_name=os.environ.get("DB_APP_NAME", "databridge"),
        pool_size=int(os.environ.get("DB_POOL_SIZE", "10")),
        max_overflow=int(os.environ.get("DB_MAX_OVERFLOW", "20")),
        pool_recycle=int(os.environ.get("DB_POOL_RECYCLE", "3600")),
    )
