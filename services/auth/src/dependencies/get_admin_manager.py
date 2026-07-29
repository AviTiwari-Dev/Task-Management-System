"""Admin manager dependency."""

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from ..dependencies.get_session import get_session
from ..operations.managers.admin import AdminManager
from ..operations.repositories.role import RoleRepository
from ..operations.repositories.user import UserRepository


def get_admin_manager(
    session: AsyncSession = Depends(get_session),
) -> AdminManager:
    """Return an admin manager."""

    return AdminManager(
        user_repository=UserRepository(session),
        role_repository=RoleRepository(session),
    )
