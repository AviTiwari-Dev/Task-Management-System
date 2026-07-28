"""Task manager."""

from uuid import UUID

from shared.auth.src.models.current_user import CurrentUser
from sqlalchemy.ext.asyncio import AsyncSession

from ...models.data_storage.task import Task
from ...models.data_validation.task_create import CreateTaskRequest
from ...models.data_validation.task_filter import TaskFilter
from ...models.data_validation.task_response import (
    TaskListResponse,
    TaskResponse,
)
from ...models.data_validation.task_update import UpdateTaskRequest
from ..repositories.task import TaskRepository


class TaskManager:
    """Task manager."""

    def __init__(
        self,
        repository: TaskRepository,
    ) -> None:
        self._repository = repository

    async def create_task(
        self,
        *,
        session: AsyncSession,
        current_user: CurrentUser,
        request: CreateTaskRequest,
    ) -> TaskResponse:
        """Create a task."""

        task = Task(
            title=request.title,
            description=request.description,
            status=request.status,
            priority=request.priority,
            due_date=request.due_date,
            user_id=current_user.user_id,
        )

        task = await self._repository.create(
            session=session,
            task=task,
        )

        return TaskResponse.model_validate(task)

    async def get_task(
        self,
        *,
        session: AsyncSession,
        current_user: CurrentUser,
        task_id: UUID,
    ) -> TaskResponse:
        """Return a task."""

        if current_user.role.lower() == "admin":
            task = await self._repository.get_by_task_id(
                session=session,
                task_id=task_id,
            )
        else:
            task = await self._repository.get_by_task_id_and_user_id(
                session=session,
                task_id=task_id,
                user_id=current_user.user_id,
            )

        if task is None:
            raise ValueError("Task not found.")

        return TaskResponse.model_validate(task)

    async def get_tasks(
        self,
        *,
        session: AsyncSession,
        current_user: CurrentUser,
        filters: TaskFilter,
    ) -> TaskListResponse:
        """Return paginated tasks."""

        task_id = filters.task_id

        # Admin can filter by any user_id.
        # Normal users can only see their own tasks.
        if current_user.role.lower() == "admin":
            user_id = filters.user_id
        else:
            user_id = current_user.user_id

        tasks, total = await self._repository.get_tasks(
            session=session,
            task_id=task_id,
            user_id=user_id,
            priority=filters.priority,
            status=filters.status,
            due_date=filters.due_date,
            page=filters.page,
            page_size=filters.page_size,
        )

        return TaskListResponse(
            total=total,
            page=filters.page,
            page_size=filters.page_size,
            results=[TaskResponse.model_validate(task) for task in tasks],
        )

    async def update_task(
        self,
        *,
        session: AsyncSession,
        current_user: CurrentUser,
        task_id: UUID,
        request: UpdateTaskRequest,
    ) -> TaskResponse:
        """Update a task."""

        if current_user.role.lower() == "admin":
            task = await self._repository.get_by_task_id(
                session=session,
                task_id=task_id,
            )
        else:
            task = await self._repository.get_by_task_id_and_user_id(
                session=session,
                task_id=task_id,
                user_id=current_user.user_id,
            )

        if task is None:
            raise ValueError("Task not found.")

        data = request.model_dump(exclude_unset=True)

        for field, value in data.items():
            setattr(task, field, value)

        task = await self._repository.update(
            session=session,
            task=task,
        )

        return TaskResponse.model_validate(task)

    async def delete_task(
        self,
        *,
        session: AsyncSession,
        current_user: CurrentUser,
        task_id: UUID,
    ) -> None:
        """Delete a task."""

        if current_user.role.lower() == "admin":
            task = await self._repository.get_by_task_id(
                session=session,
                task_id=task_id,
            )
        else:
            task = await self._repository.get_by_task_id_and_user_id(
                session=session,
                task_id=task_id,
                user_id=current_user.user_id,
            )

        if task is None:
            raise ValueError("Task not found.")

        await self._repository.delete(
            session=session,
            task=task,
        )
