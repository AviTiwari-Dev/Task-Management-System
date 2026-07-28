"""Session dependency."""

from collections.abc import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession

from ..session_factories.task import session_factory


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    """Provide a database session."""

    async with session_factory() as session:
        yield session
