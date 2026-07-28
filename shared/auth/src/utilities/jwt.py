"""JWT utility functions."""

from uuid import UUID

import jwt
from pydantic import BaseModel


class TokenPayload(BaseModel):
    """JWT payload."""

    sub: UUID
    username: str
    role: str
    iss: str
    aud: str
    iat: int
    exp: int


def verify_token(
    *,
    token: str,
    secret_key: str,
    issuer: str,
    audience: str,
) -> TokenPayload:
    """
    Verify JWT token.
    """

    payload = jwt.decode(
        token,
        secret_key,
        algorithms=["HS256"],
        issuer=issuer,
        audience=audience,
    )

    return TokenPayload.model_validate(payload)
