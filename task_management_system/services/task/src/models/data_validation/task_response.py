from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict

from .task import TaskBase


class TaskResponse(TaskBase):
    task_id: UUID

    user_id: UUID

    created_at: datetime

    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


class TaskListResponse(BaseModel):
    total: int

    page: int

    page_size: int

    results: list[TaskResponse]
