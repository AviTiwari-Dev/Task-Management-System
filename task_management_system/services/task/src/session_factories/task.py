"""
Session Factory
"""

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from ..engines.task import engine as auth_engine

session_factory = async_sessionmaker(
    bind=auth_engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autoflush=True,
)
