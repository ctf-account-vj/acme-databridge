import logging
from contextlib import contextmanager

from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

from .db_config import get_db_config

logger = logging.getLogger(__name__)


def _build_url(cfg: dict) -> str:
    return (
        f"postgresql://{cfg['user']}:{cfg['password']}"
        f"@{cfg['host']}:{cfg['port']}/{cfg['dbname']}"
    )


class DatabaseManager:
    """Manages PostgreSQL connections for the DataBridge service."""

    def __init__(self):
        cfg = get_db_config()
        self.engine = create_engine(
            _build_url(cfg),
            pool_size=cfg["pool_size"],
            max_overflow=cfg["max_overflow"],
            pool_pre_ping=True,
            pool_recycle=cfg["pool_recycle"],
            connect_args={
                "connect_timeout": cfg["connect_timeout"],
                "application_name": cfg["application_name"],
            },
        )
        self.SessionLocal = sessionmaker(bind=self.engine)

    @contextmanager
    def get_session(self):
        session = self.SessionLocal()
        try:
            yield session
            session.commit()
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()

    def health_check(self) -> bool:
        try:
            with self.get_session() as session:
                session.execute(text("SELECT 1"))
            return True
        except Exception as exc:
            logger.error("Database health check failed: %s", exc)
            return False
