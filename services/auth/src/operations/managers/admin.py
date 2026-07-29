"""Admin manager."""

from uuid import UUID

from shared.auth.src.enums.role import Role

from ...exceptions.role_not_found_error import RoleNotFoundError
from ...exceptions.user_not_found_error import UserNotFoundError
from ...models.data_validation.user import UserResponse
from ..repositories.role import RoleRepository
from ..repositories.user import UserRepository


class AdminManager:
    """Manager for administrative user operations."""

    def __init__(
        self,
        user_repository: UserRepository,
        role_repository: RoleRepository,
    ) -> None:
        self._user_repository = user_repository
        self._role_repository = role_repository

    async def make_admin(
        self,
        *,
        user_id: UUID,
    ) -> UserResponse:
        """Promote a user to admin."""

        user = await self._user_repository.get_by_user_id(user_id)

        if user is None:
            raise UserNotFoundError()

        admin_role = await self._role_repository.get_by_role_name(Role.ADMIN)

        if admin_role is None:
            raise RoleNotFoundError()

        user.role = admin_role

        user = await self._user_repository.update(user)

        return UserResponse(
            user_id=user.user_id,
            first_name=user.first_name,
            middle_name=user.middle_name,
            last_name=user.last_name,
            username=user.username,
            role=user.role.role_name,
            is_active=user.is_active,
            created_at=user.created_at,
            updated_at=user.updated_at,
        )

    async def make_user(
        self,
        *,
        user_id: UUID,
    ) -> UserResponse:
        """Demote an admin to a normal user."""

        user = await self._user_repository.get_by_user_id(
            user_id,
        )

        if user is None:
            raise UserNotFoundError()

        user_role = await self._role_repository.get_by_role_name(Role.USER)

        if user_role is None:
            raise RoleNotFoundError()

        user.role = user_role

        user = await self._user_repository.update(user)

        return UserResponse(
            user_id=user.user_id,
            first_name=user.first_name,
            middle_name=user.middle_name,
            last_name=user.last_name,
            username=user.username,
            role=user.role.role_name,
            is_active=user.is_active,
            created_at=user.created_at,
            updated_at=user.updated_at,
        )
