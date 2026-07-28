"""Token response models."""

from pydantic import BaseModel, ConfigDict


class TokenResponse(BaseModel):
    """JWT token response."""

    model_config = ConfigDict(
        from_attributes=True,
    )

    access_token: str
    token_type: str = "Bearer"
