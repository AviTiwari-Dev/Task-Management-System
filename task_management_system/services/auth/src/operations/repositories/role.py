"""Role repository."""

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from ......shared.auth.src.enums.role import Role as RoleEnum
from ...models.data_storage.role import Role


class RoleRepository:
    """Repository for role database operations."""

    def __init__(
        self,
        session: AsyncSession,
    ) -> None:
        self._session = session

    async def get_by_role_name(
        self,
        role_name: RoleEnum,
    ) -> Role | None:
        """Get a role by name."""

        result = await self._session.execute(
            select(Role).where(
                Role.role_name == role_name,
            ),
        )

        return result.scalar_one_or_none()
