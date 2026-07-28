"""Authentication manager."""

from shared.auth.src.enums.role import Role as RoleEnum

from ...models.data_storage.user import User
from ...models.data_validation.auth import LoginRequest, RegisterRequest
from ...models.data_validation.token import TokenResponse
from ...models.data_validation.user import UserResponse
from ...operations.repositories.role import RoleRepository
from ...operations.repositories.user import UserRepository
from ...utilities.hash import hash_password, verify_password
from ...utilities.jwt import generate_access_token


class AuthManager:
    """Authentication manager."""

    def __init__(
        self,
        user_repository: UserRepository,
        role_repository: RoleRepository,
    ) -> None:
        self._user_repository = user_repository
        self._role_repository = role_repository

    async def register(
        self,
        request: RegisterRequest,
    ) -> UserResponse:
        """
        Register a new user.
        """

        existing_user = await self._user_repository.get_by_username(
            request.username,
        )

        if existing_user is not None:
            raise ValueError("Username already exists.")

        role = await self._role_repository.get_by_role_name(
            RoleEnum.USER,
        )

        if role is None:
            raise ValueError("Default role not found.")

        user = User(
            first_name=request.first_name,
            middle_name=request.middle_name,
            last_name=request.last_name,
            username=request.username,
            password_hash=hash_password(request.password),
            role_id=role.role_id,
        )

        user = await self._user_repository.create(user)

        return UserResponse(
            user_id=user.user_id,
            first_name=user.first_name,
            middle_name=user.middle_name,
            last_name=user.last_name,
            username=user.username,
            role=role.role_name,
            is_active=user.is_active,
            created_at=user.created_at,
            updated_at=user.updated_at,
        )

    async def login(
        self,
        request: LoginRequest,
    ) -> TokenResponse:
        """
        Authenticate a user.
        """

        user = await self._user_repository.get_by_username(
            request.username,
        )

        if user is None:
            raise ValueError("Invalid username or password.")

        if not verify_password(
            request.password,
            user.password_hash,
        ):
            raise ValueError("Invalid username or password.")

        if not user.is_active:
            raise ValueError("User account is inactive.")

        token = generate_access_token(
            user_id=user.user_id,
            username=user.username,
            role=user.role.role_name.value,
        )

        return TokenResponse(
            access_token=token,
        )
