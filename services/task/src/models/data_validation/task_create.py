from datetime import datetime, timezone

from pydantic import BaseModel, field_validator


class CreateTaskRequest(BaseModel):
    due_date: datetime

    @field_validator("due_date")
    @classmethod
    def validate_due_date(cls, value):
        if value <= datetime.now(timezone.utc):
            raise ValueError("Due date must be in the future.")
        return value
