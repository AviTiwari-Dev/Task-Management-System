"""User repository."""

from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from ...models.data_storage.user import User


class UserRepository:
    """Repository for user database operations."""

    def __init__(
        self,
        session: AsyncSession,
    ) -> None:
        self._session = session

    async def create(
        self,
        user: User,
    ) -> User:
        """Create a user."""

        self._session.add(user)

        await self._session.commit()
        await self._session.refresh(user)

        return user

    async def get_by_user_id(
        self,
        user_id: UUID,
    ) -> User | None:
        """Return a user by user ID."""

        result = await self._session.execute(
            select(User)
            .options(selectinload(User.role))
            .where(User.user_id == user_id),
        )

        return result.scalar_one_or_none()

    async def get_by_username(
        self,
        username: str,
    ) -> User | None:
        """Return a user by username."""

        result = await self._session.execute(
            select(User)
            .options(selectinload(User.role))
            .where(User.username == username),
        )

        return result.scalar_one_or_none()

    async def update(
        self,
        user: User,
    ) -> User:
        """Persist changes to a user."""

        await self._session.commit()
        await self._session.refresh(user)

        return user

    async def delete(
        self,
        user: User,
    ) -> None:
        """Delete a user."""

        await self._session.delete(user)
        await self._session.commit()
