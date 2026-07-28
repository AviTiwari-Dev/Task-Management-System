""" """

from argon2 import PasswordHasher, Type
from argon2.exceptions import VerificationError, VerifyMismatchError

from ..configurations.utilities import utility_configuration_variables

_password_hasher = PasswordHasher(
    time_cost=3,
    memory_cost=65536,  # 64 MiB
    parallelism=4,
    hash_len=32,  # 32 bytes (256 bits)
    salt_len=16,  # 16 bytes (128 bits)
    type=Type.ID,
)


def hash_password(value: str) -> str:
    """
    Hash a value using Argon2id and a server-side pepper.
    """
    return _password_hasher.hash(
        value + utility_configuration_variables.PASSWORD_PEPPER,
    )


def verify_password(value: str, hashed_value: str) -> bool:
    """
    Verify a value against its Argon2 hash.
    """
    try:
        return _password_hasher.verify(
            hashed_value,
            value + utility_configuration_variables.PASSWORD_PEPPER,
        )
    except (VerifyMismatchError, VerificationError):
        return False


def needs_rehash(hashed_value: str) -> bool:
    """Return True if the stored hash should be upgraded."""
    return _password_hasher.check_needs_rehash(hashed_value)


print(hash_password("stringstA@1"))
