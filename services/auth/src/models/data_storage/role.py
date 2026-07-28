"""Role model."""

from datetime import datetime
from typing import TYPE_CHECKING
from uuid import UUID, uuid4

from shared.auth.src.enums.role import Role as RoleEnum
from sqlalchemy import DateTime, Enum, String, func
from sqlalchemy.dialects.postgresql import UUID as PGUUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ...bases.auth import AuthBase

if TYPE_CHECKING:
    from .role_permission import RolePermission
    from .user import User


class Role(AuthBase):
    """Role model."""

    __tablename__ = "roles"
    __table_args__ = {"schema": "auth_sch"}

    role_id: Mapped[UUID] = mapped_column(
        PGUUID(as_uuid=True),
        primary_key=True,
        default=uuid4,
    )

    role_name: Mapped[RoleEnum] = mapped_column(
        Enum(
            RoleEnum,
            name="role_enum",
            schema="auth_sch",
        ),
        unique=True,
        nullable=False,
    )

    description: Mapped[str | None] = mapped_column(
        String(255),
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )

    users: Mapped[list["User"]] = relationship(
        back_populates="role",
    )

    permissions: Mapped[list["RolePermission"]] = relationship(
        back_populates="role",
        cascade="all, delete-orphan",
    )
