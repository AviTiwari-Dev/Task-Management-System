"""Role enum."""

from enum import StrEnum


class Role(StrEnum):
    """System roles."""

    ADMIN = "admin"
    USER = "user"
