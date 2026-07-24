"""Authentication request models."""

from pydantic import BaseModel, ConfigDict, Field, field_validator


class RegisterRequest(BaseModel):
    """Register request."""

    model_config = ConfigDict(
        str_strip_whitespace=True,
    )

    first_name: str = Field(
        min_length=1,
        max_length=50,
    )

    middle_name: str | None = Field(
        default=None,
        max_length=50,
    )

    last_name: str = Field(
        min_length=1,
        max_length=50,
    )

    username: str = Field(
        min_length=3,
        max_length=100,
    )

    password: str = Field(
        min_length=8,
        max_length=128,
    )

    @field_validator(
        "first_name",
        "middle_name",
        "last_name",
    )
    @classmethod
    def validate_name(cls, value: str | None) -> str | None:
        """Validate name fields."""
        if value is None:
            return value

        if not value.replace(" ", "").isalpha():
            raise ValueError("Only alphabets are allowed.")

        return value


class LoginRequest(BaseModel):
    """Login request."""

    model_config = ConfigDict(
        str_strip_whitespace=True,
    )

    username: str = Field(
        min_length=3,
        max_length=100,
    )

    password: str = Field(
        min_length=8,
        max_length=128,
    )
