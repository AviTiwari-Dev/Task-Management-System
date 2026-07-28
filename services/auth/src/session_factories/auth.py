"""Session factory."""

from collections.abc import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from ..engines.auth import engine as auth_engine

session_factory = async_sessionmaker(
    bind=auth_engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autoflush=True,
)
