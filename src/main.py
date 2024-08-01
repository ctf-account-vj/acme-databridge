"""Acme DataBridge — main entry point."""

import logging
import signal
import sys
import time

import structlog

from .config import get_settings
from .sync import SyncEngine

log = structlog.get_logger(__name__)


def setup_logging(level: str) -> None:
    structlog.configure(
        processors=[
            structlog.processors.TimeStamper(fmt="iso"),
            structlog.stdlib.add_log_level,
            structlog.processors.StackInfoRenderer(),
            structlog.dev.ConsoleRenderer(),
        ],
        wrapper_class=structlog.BoundLogger,
        context_class=dict,
        logger_factory=structlog.PrintLoggerFactory(),
    )
    logging.basicConfig(level=getattr(logging, level.upper(), logging.INFO))


def main() -> None:
    settings = get_settings()
    setup_logging(settings.log_level)
    log.info("databridge.startup", version="1.2.0")

    engine = SyncEngine(settings)

    def shutdown(sig, frame):  # noqa: ANN001
        log.info("databridge.shutdown", signal=sig)
        sys.exit(0)

    signal.signal(signal.SIGINT, shutdown)
    signal.signal(signal.SIGTERM, shutdown)

    while True:
        try:
            engine.run_sync_cycle()
        except Exception as exc:
            log.error("databridge.sync_cycle_error", exc_info=exc)
        time.sleep(settings.sync_interval_seconds)


if __name__ == "__main__":
    main()
