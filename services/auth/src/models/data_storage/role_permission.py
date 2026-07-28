"""Role Permission model."""

from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ...bases.auth import AuthBase

if TYPE_CHECKING:
    from .permission import Permission
    from .role import Role


class RolePermission(AuthBase):
    """Role Permission model."""

    __tablename__ = "role_permissions"
    __table_args__ = {"schema": "auth_sch"}

    role_id: Mapped[UUID] = mapped_column(
        ForeignKey(
            "auth_sch.roles.role_id",
            ondelete="CASCADE",
        ),
        primary_key=True,
    )

    permission_id: Mapped[UUID] = mapped_column(
        ForeignKey(
            "auth_sch.permissions.permission_id",
            ondelete="CASCADE",
        ),
        primary_key=True,
    )

    role: Mapped["Role"] = relationship(
        back_populates="permissions",
    )

    permission: Mapped["Permission"] = relationship(
        back_populates="roles",
    )
