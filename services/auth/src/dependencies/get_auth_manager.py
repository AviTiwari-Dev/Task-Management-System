from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from ..dependencies.get_session import get_session
from ..operations.managers.auth import AuthManager
from ..operations.repositories.role import RoleRepository
from ..operations.repositories.user import UserRepository


async def get_auth_manager(
    session: AsyncSession = Depends(get_session),
) -> AuthManager:
    return AuthManager(
        user_repository=UserRepository(session),
        role_repository=RoleRepository(session),
    )
