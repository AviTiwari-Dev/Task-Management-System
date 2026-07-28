"""Authentication endpoints."""

from fastapi import Depends, status
from shared.auth.src.models.current_user import CurrentUser

from ...dependencies.auth import get_current_user
from ...dependencies.get_auth_manager import get_auth_manager
from ...dependencies.get_user_manager import get_user_manager
from ...models.data_validation.auth import LoginRequest, RegisterRequest
from ...models.data_validation.token import TokenResponse
from ...models.data_validation.user import UserResponse
from ...operations.managers.auth import AuthManager
from ...operations.managers.user import UserManager
from ...routers.auth import router


@router.post(
    "/register",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Register a new user",
)
async def register(
    request: RegisterRequest,
    manager: AuthManager = Depends(get_auth_manager),
) -> UserResponse:
    """Register a new user."""

    return await manager.register(request)


@router.post(
    "/login",
    response_model=TokenResponse,
    status_code=status.HTTP_200_OK,
    summary="Authenticate a user",
)
async def login(
    request: LoginRequest,
    manager: AuthManager = Depends(get_auth_manager),
) -> TokenResponse:
    """Authenticate a user."""

    return await manager.login(request)


@router.get(
    "/me",
    response_model=UserResponse,
    status_code=status.HTTP_200_OK,
    summary="Get current user",
)
async def get_current_authenticated_user(
    current_user: CurrentUser = Depends(get_current_user),
    manager: UserManager = Depends(get_user_manager),
) -> UserResponse:
    """Return the currently authenticated user."""

    return await manager.get_by_user_id(current_user.user_id)
