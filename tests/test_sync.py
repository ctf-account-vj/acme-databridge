"""Basic smoke tests for the sync engine."""

import pytest
from src.models import SyncJob, SyncStatus


def test_sync_job_initial_status():
    job = SyncJob(job_id="test-001", status=SyncStatus.PENDING)
    assert job.status == SyncStatus.PENDING
    assert job.records_processed == 0


def test_sync_job_completion():
    from datetime import datetime, timezone
    job = SyncJob(
        job_id="test-002",
        status=SyncStatus.COMPLETED,
        records_processed=150,
        completed_at=datetime.now(timezone.utc),
    )
    assert job.records_processed == 150
    assert job.status == SyncStatus.COMPLETED
