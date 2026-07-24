"""Admin dependency."""

from fastapi import Depends, HTTPException, status

from ..models.current_user import CurrentUser
from .get_current_user import get_current_user


async def get_current_admin(
    current_user: CurrentUser = Depends(get_current_user),
) -> CurrentUser:
    """Ensure current user is an admin."""

    if current_user.role.lower() != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Administrator access required.",
        )

    return current_user
