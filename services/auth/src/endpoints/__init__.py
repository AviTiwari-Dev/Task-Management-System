from .rest.admin import make_admin, make_user
from .rest.auth import get_current_authenticated_user, login, register

__all__ = [
    "get_current_authenticated_user",
    "login",
    "register",
    "make_admin",
    "make_user",
]
