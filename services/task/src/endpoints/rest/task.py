"""Task endpoints."""

from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Depends
from shared.auth.src.models.current_user import CurrentUser
from sqlalchemy.ext.asyncio import AsyncSession

from ...dependencies.auth import get_current_user
from ...dependencies.get_task_manager import get_task_manager
from ...dependencies.session import get_session
from ...models.data_validation.task_create import CreateTaskRequest
from ...models.data_validation.task_filter import TaskFilter
from ...models.data_validation.task_response import (
    TaskListResponse,
    TaskResponse,
)
from ...models.data_validation.task_update import UpdateTaskRequest
from ...operations.managers.task import TaskManager

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"],
)


Session = Annotated[
    AsyncSession,
    Depends(get_session),
]

Current = Annotated[
    CurrentUser,
    Depends(get_current_user),
]


Manager = Annotated[
    TaskManager,
    Depends(get_task_manager),
]


@router.post(
    "",
    response_model=TaskResponse,
    status_code=201,
)
async def create_task(
    request: CreateTaskRequest,
    session: Session,
    current_user: Current,
    manager: Manager,
) -> TaskResponse:
    """Create task."""

    return await manager.create_task(
        session=session,
        current_user=current_user,
        request=request,
    )


@router.get(
    "",
    response_model=TaskListResponse,
)
async def get_tasks(
    filters: Annotated[TaskFilter, Depends()],
    session: Session,
    current_user: Current,
    manager: Manager,
) -> TaskListResponse:
    """Return tasks."""

    return await manager.get_tasks(
        session=session,
        current_user=current_user,
        filters=filters,
    )


@router.get(
    "/{task_id}",
    response_model=TaskResponse,
)
async def get_task(
    task_id: UUID,
    session: Session,
    current_user: Current,
    manager: Manager,
) -> TaskResponse:
    """Return task."""

    return await manager.get_task(
        session=session,
        current_user=current_user,
        task_id=task_id,
    )


@router.patch(
    "/{task_id}",
    response_model=TaskResponse,
)
async def update_task(
    task_id: UUID,
    request: UpdateTaskRequest,
    session: Session,
    current_user: Current,
    manager: Manager,
) -> TaskResponse:
    """Update task."""

    return await manager.update_task(
        session=session,
        current_user=current_user,
        task_id=task_id,
        request=request,
    )


@router.delete(
    "/{task_id}",
    status_code=204,
)
async def delete_task(
    task_id: UUID,
    session: Session,
    current_user: Current,
    manager: Manager,
) -> None:
    """Delete task."""

    await manager.delete_task(
        session=session,
        current_user=current_user,
        task_id=task_id,
    )
