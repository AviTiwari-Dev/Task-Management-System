"""User manager."""

from uuid import UUID

from ...models.data_validation.user import UserResponse
from ...operations.repositories.user import UserRepository


class UserManager:
    """User manager."""

    def __init__(
        self,
        user_repository: UserRepository,
    ) -> None:
        self._user_repository = user_repository

    async def get_by_user_id(
        self,
        user_id: UUID,
    ) -> UserResponse:
        """
        Get a user by id.
        """

        user = await self._user_repository.get_by_user_id(
            user_id,
        )

        if user is None:
            raise ValueError("User not found.")

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
