from .....shared.auth.src.dependencies.get_current_user import (
    JWTSettings,
    get_current_user_dependency,
)
from ..configurations.settings import settings

jwt_settings = JWTSettings(
    secret_key=settings.JWT_SECRET_KEY,
    issuer=settings.JWT_ISSUER,
    audience=settings.JWT_AUDIENCE,
)

get_current_user = get_current_user_dependency(jwt_settings)
