from datetime import datetime

from pydantic import BaseModel, Field, field_validator

from ...enums.task_priority import TaskPriority
from ...enums.task_status import TaskStatus


class UpdateTaskRequest(BaseModel):
    title: str | None = Field(default=None, min_length=3, max_length=100)

    description: str | None = Field(default=None, max_length=1000)

    status: TaskStatus | None = None

    priority: TaskPriority | None = None

    due_date: datetime | None = None

    @field_validator("title")
    @classmethod
    def validate_title(cls, value: str | None):
        if value is None:
            return value

        value = value.strip()

        if not value:
            raise ValueError("Title cannot be empty.")

        return value

    @field_validator("description")
    @classmethod
    def validate_description(cls, value: str | None):
        if value is None:
            return value

        value = value.strip()

        if not value:
            return None

        return value

    @field_validator("due_date")
    @classmethod
    def validate_due_date(cls, value: datetime | None):
        if value is None:
            return value

        if value <= datetime.now(value.tzinfo):
            raise ValueError("Due date must be in the future.")

        return value
