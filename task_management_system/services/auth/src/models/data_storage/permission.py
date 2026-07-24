"""Permission model."""

from datetime import datetime
from typing import TYPE_CHECKING
from uuid import UUID, uuid4

from sqlalchemy import DateTime, Enum, String, func
from sqlalchemy.dialects.postgresql import UUID as PGUUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ...bases.auth import AuthBase
from ...enums.permission import Permission as PermissionEnum

if TYPE_CHECKING:
    from .role_permission import RolePermission


class Permission(AuthBase):
    """Permission model."""

    __tablename__ = "permissions"
    __table_args__ = {"schema": "auth_sch"}

    permission_id: Mapped[UUID] = mapped_column(
        PGUUID(as_uuid=True),
        primary_key=True,
        default=uuid4,
    )

    permission_name: Mapped[PermissionEnum] = mapped_column(
        Enum(
            PermissionEnum,
            name="permission_enum",
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

    roles: Mapped[list["RolePermission"]] = relationship(
        back_populates="permission",
        cascade="all, delete-orphan",
    )
