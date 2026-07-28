"""JWT utilities."""

from datetime import UTC, datetime, timedelta
from uuid import UUID

import jwt
from jwt import ExpiredSignatureError, InvalidTokenError

from ..configurations.utilities import utility_configuration_variables


def generate_access_token(
    user_id: UUID,
    username: str,
    role: str,
) -> str:
    """Generate a JWT access token."""

    now = datetime.now(UTC)

    payload = {
        "sub": str(user_id),
        "username": username,
        "role": role,
        "iss": utility_configuration_variables.JWT_ISSUER,
        "aud": utility_configuration_variables.JWT_AUDIENCE,
        "iat": now,
        "exp": now
        + timedelta(
            minutes=utility_configuration_variables.JWT_ACCESS_TOKEN_EXPIRE_MINUTES,
        ),
    }

    return jwt.encode(
        payload,
        utility_configuration_variables.JWT_SECRET_KEY,
        algorithm=utility_configuration_variables.JWT_ALGORITHM,
    )


def decode_token(token: str) -> dict:
    """Decode a JWT without handling exceptions."""

    return jwt.decode(
        token,
        utility_configuration_variables.JWT_SECRET_KEY,
        algorithms=[utility_configuration_variables.JWT_ALGORITHM],
        issuer=utility_configuration_variables.JWT_ISSUER,
        audience=utility_configuration_variables.JWT_AUDIENCE,
    )


def verify_token(token: str) -> dict | None:
    """Verify a JWT."""

    try:
        return decode_token(token)
    except (ExpiredSignatureError, InvalidTokenError):
        return None
