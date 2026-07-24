"""
Engine
"""

from sqlalchemy.ext.asyncio import create_async_engine

from ..configurations.engine import engine_configuration_variables

engine = create_async_engine(
    url=engine_configuration_variables.URL,
    echo=engine_configuration_variables.ECHO,
    pool_size=engine_configuration_variables.POOL_SIZE,
    max_overflow=engine_configuration_variables.MAX_OVERFLOW,
    pool_timeout=engine_configuration_variables.POOL_TIMEOUT,
    pool_recycle=engine_configuration_variables.POOL_RECYCLE,
    future=engine_configuration_variables.FUTURE,
    connect_args={
        "server_settings": {
            "jit": "off",
        }
    },
)
