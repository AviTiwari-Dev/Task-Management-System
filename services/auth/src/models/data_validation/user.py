"""User response models."""

from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict
from shared.auth.src.enums.role import Role


class UserResponse(BaseModel):
    """User response."""

    model_config = ConfigDict(
        from_attributes=True,
    )

    user_id: UUID
    first_name: str
    middle_name: str | None
    last_name: str
    username: str
    role: Role
    is_active: bool
    created_at: datetime
    updated_at: datetime
