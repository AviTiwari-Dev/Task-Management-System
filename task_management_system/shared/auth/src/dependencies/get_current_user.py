"""Current user dependency."""

from collections.abc import Awaitable, Callable

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from jwt import ExpiredSignatureError, InvalidTokenError
from pydantic import BaseModel

from ..models.current_user import CurrentUser
from ..utilities.jwt import verify_token

bearer_scheme = HTTPBearer()


class JWTSettings(BaseModel):
    """JWT settings."""

    secret_key: str
    issuer: str
    audience: str


def get_current_user_dependency(
    settings: JWTSettings,
) -> Callable[[HTTPAuthorizationCredentials], Awaitable[CurrentUser]]:
    """Create a dependency for retrieving the authenticated user."""

    async def get_current_user(
        credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme),
    ) -> CurrentUser:
        """Return the authenticated user."""

        try:
            payload = verify_token(
                token=credentials.credentials,
                secret_key=settings.secret_key,
                issuer=settings.issuer,
                audience=settings.audience,
            )

        except ExpiredSignatureError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token has expired.",
            ) from None

        except InvalidTokenError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid authentication token.",
            ) from None

        return CurrentUser(
            user_id=payload.sub,
            username=payload.username,
            role=payload.role,
        )

    return get_current_user
