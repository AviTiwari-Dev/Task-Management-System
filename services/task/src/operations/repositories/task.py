"""Task repository."""

from datetime import datetime
from uuid import UUID

from sqlalchemy import Select, func, select
from sqlalchemy.ext.asyncio import AsyncSession

from ...enums.task_priority import TaskPriority
from ...enums.task_status import TaskStatus
from ...models.data_storage.task import Task


class TaskRepository:
    """Repository for Task model."""

    async def create(
        self,
        *,
        session: AsyncSession,
        task: Task,
    ) -> Task:
        """Create a new task."""

        session.add(task)
        await session.commit()
        await session.refresh(task)

        return task

    async def get_by_task_id(
        self,
        *,
        session: AsyncSession,
        task_id: UUID,
    ) -> Task | None:
        """
        Return a task by its ID.
        """

        statement = select(Task).where(Task.task_id == task_id)

        result = await session.execute(statement)

        return result.scalar_one_or_none()

    async def get_by_task_id_and_user_id(
        self,
        *,
        session: AsyncSession,
        task_id: UUID,
        user_id: UUID,
    ) -> Task | None:
        """
        Return a task by task ID and owner.
        """
        statement = select(Task).where(
            Task.task_id == task_id,
            Task.user_id == user_id,
        )

        result = await session.execute(statement)

        return result.scalar_one_or_none()

    async def get_tasks(
        self,
        *,
        session: AsyncSession,
        task_id: UUID | None = None,
        user_id: UUID | None = None,
        priority: TaskPriority | None = None,
        status: TaskStatus | None = None,
        due_date: datetime | None = None,
        page: int = 1,
        page_size: int = 10,
    ) -> tuple[list[Task], int]:
        """
        Return paginated tasks.
        """

        statement: Select[tuple[Task]] = select(Task)

        if task_id is not None:
            statement = statement.where(Task.task_id == task_id)

        if user_id is not None:
            statement = statement.where(Task.user_id == user_id)

        if priority is not None:
            statement = statement.where(Task.priority == priority)

        if status is not None:
            statement = statement.where(Task.status == status)

        if due_date is not None:
            statement = statement.where(Task.due_date <= due_date)

        count_statement = select(func.count()).select_from(statement.subquery())

        total = await session.scalar(count_statement)
        total = total or 0

        statement = (
            statement.order_by(Task.created_at.desc())
            .offset((page - 1) * page_size)
            .limit(page_size)
        )

        result = await session.execute(statement)

        return list(result.scalars().all()), total

    async def update(
        self,
        *,
        session: AsyncSession,
        task: Task,
    ) -> Task:
        """Persist task updates."""

        await session.commit()
        await session.refresh(task)

        return task

    async def delete(
        self,
        *,
        session: AsyncSession,
        task: Task,
    ) -> None:
        """Delete task."""

        await session.delete(task)
        await session.commit()
