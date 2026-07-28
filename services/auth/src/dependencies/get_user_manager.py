from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from ..dependencies.get_session import get_session
from ..operations.managers.user import UserManager
from ..operations.repositories.user import UserRepository


async def get_user_manager(
    session: AsyncSession = Depends(get_session),
) -> UserManager:
    return UserManager(
        user_repository=UserRepository(session),
    )
