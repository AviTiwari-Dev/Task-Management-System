"""Admin endpoints."""

from uuid import UUID

from fastapi import Depends, status
from shared.auth.src.models.current_user import CurrentUser

from ...dependencies.auth import get_current_user
from ...dependencies.get_admin_manager import get_admin_manager
from ...models.data_validation.user import UserResponse
from ...operations.managers.admin import AdminManager
from ...routers.auth import router


@router.patch(
    "/users/{user_id}/make-admin",
    response_model=UserResponse,
    status_code=status.HTTP_200_OK,
    summary="Promote a user to admin",
)
async def make_admin(
    user_id: UUID,
    current_user: CurrentUser = Depends(get_current_user),
    manager: AdminManager = Depends(get_admin_manager),
) -> UserResponse:
    """Promote a user to admin."""

    # TODO: Replace with get_current_admin_user dependency.
    if current_user.role.lower() != "admin":
        raise PermissionError("Only admins can perform this action.")

    return await manager.make_admin(
        user_id=user_id,
    )


@router.patch(
    "/users/{user_id}/make-user",
    response_model=UserResponse,
    status_code=status.HTTP_200_OK,
    summary="Demote an admin to user",
)
async def make_user(
    user_id: UUID,
    current_user: CurrentUser = Depends(get_current_user),
    manager: AdminManager = Depends(get_admin_manager),
) -> UserResponse:
    """Demote an admin to a normal user."""

    # TODO: Replace with get_current_admin_user dependency.
    if current_user.role.lower() != "admin":
        raise PermissionError("Only admins can perform this action.")

    return await manager.make_user(
        user_id=user_id,
    )
