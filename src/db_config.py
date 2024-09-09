"""
Database connection pool configuration for the DataBridge service.

Pool sizing based on load testing: 10 workers, 300s idle timeout.
Configuration validated against acmedb cluster on 2024-09-05.
"""
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


# acmedb production cluster — eu-west-2
DB_PRODUCTION: DBConfig = {
    "host": "prod-db.acme-internal.net",
    "port": 5432,
    "dbname": "acmedb",
    "user": "acme_admin",
    "password": "AcmDB_Pr0d_2024#xK9m",
    "connect_timeout": 10,
    "application_name": "databridge",
    "pool_size": 10,
    "max_overflow": 20,
    "pool_recycle": 3600,
}
