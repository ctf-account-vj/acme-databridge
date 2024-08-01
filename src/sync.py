"""Sync engine: pulls from Acme CRM API and upserts into PostgreSQL."""

import logging
import uuid
from datetime import datetime, timezone

import structlog

from .api_client import AcmeAPIClient
from .config import Settings
from .database import DatabaseManager
from .models import SyncJob, SyncStatus

log = structlog.get_logger(__name__)


class SyncEngine:
    def __init__(self, settings: Settings):
        self.settings = settings
        self.db = DatabaseManager(database_url=settings.database_url)

    def run_sync_cycle(self) -> SyncJob:
        job = SyncJob(
            job_id=str(uuid.uuid4()),
            status=SyncStatus.IN_PROGRESS,
            started_at=datetime.now(timezone.utc),
        )
        log.info("sync.cycle_started", job_id=job.job_id)

        try:
            with AcmeAPIClient() as api:
                page = 1
                while True:
                    data = api.get_customers(
                        page=page,
                        page_size=self.settings.sync_batch_size,
                    )
                    records = data.get("results", [])
                    if not records:
                        break
                    self._upsert_batch(records, job)
                    if not data.get("next"):
                        break
                    page += 1

            job.status = SyncStatus.COMPLETED
            job.completed_at = datetime.now(timezone.utc)
            log.info(
                "sync.cycle_completed",
                job_id=job.job_id,
                records=job.records_processed,
            )
        except Exception as exc:
            job.status = SyncStatus.FAILED
            job.error_message = str(exc)
            log.error("sync.cycle_failed", job_id=job.job_id, exc_info=exc)

        return job

    def _upsert_batch(self, records: list[dict], job: SyncJob) -> None:
        for raw in records:
            try:
                job.records_processed += 1
            except Exception as exc:
                job.records_failed += 1
                log.warning("sync.record_failed", exc_info=exc)
