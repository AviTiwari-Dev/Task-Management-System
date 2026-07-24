"""Current authenticated user model."""

from uuid import UUID

from pydantic import BaseModel, ConfigDict

from ..enums.role import Role


class CurrentUser(BaseModel):
    """Authenticated user."""

    user_id: UUID
    username: str
    role: Role

    model_config = ConfigDict(
        frozen=True,
        extra="forbid",
    )
