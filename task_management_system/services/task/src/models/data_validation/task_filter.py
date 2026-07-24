from datetime import datetime

from pydantic import BaseModel, Field

from ...enums.task_priority import TaskPriority
from ...enums.task_status import TaskStatus


class TaskFilter(BaseModel):
    status: TaskStatus | None = None

    priority: TaskPriority | None = None

    due_date: datetime | None = None

    page: int = Field(default=1, ge=1)

    page_size: int = Field(default=10, ge=1, le=100)
