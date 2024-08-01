from datetime import datetime
from enum import Enum

from pydantic import BaseModel, EmailStr


class SyncStatus(str, Enum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    FAILED = "failed"


class CustomerRecord(BaseModel):
    id: str
    email: EmailStr
    first_name: str
    last_name: str
    account_tier: str
    created_at: datetime
    updated_at: datetime


class SyncJob(BaseModel):
    job_id: str
    status: SyncStatus
    records_processed: int = 0
    records_failed: int = 0
    started_at: datetime | None = None
    completed_at: datetime | None = None
    error_message: str | None = None
