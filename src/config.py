import os

from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_url: str = Field(..., description="PostgreSQL connection string")
    acme_api_base_url: str = Field(
        default="https://api.acme-internal.net",
    )
    acme_api_token: str = Field(..., description="Bearer token for Acme API")
    sync_batch_size: int = Field(default=500)
    sync_interval_seconds: int = Field(default=300)
    log_level: str = Field(default="INFO")

    class Config:
        env_file = ".env"
        case_sensitive = False


_settings: Settings | None = None


def get_settings() -> Settings:
    global _settings
    if _settings is None:
        _settings = Settings()
    return _settings
