from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict

from ...enums.task_priority import TaskPriority
from ...enums.task_status import TaskStatus
from .task import TaskBase


class TaskResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    task_id: UUID
    user_id: UUID

    title: str
    description: str | None
    priority: TaskPriority
    status: TaskStatus
    due_date: datetime | None

    created_at: datetime
    updated_at: datetime


class TaskListResponse(BaseModel):
    total: int

    page: int

    page_size: int

    results: list[TaskResponse]
