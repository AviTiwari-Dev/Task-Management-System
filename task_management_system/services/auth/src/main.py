""" """

from contextlib import asynccontextmanager

from fastapi import FastAPI

from . import endpoints  # noqa: F401
from .bases.auth import AuthBase
from .configurations.auth_api import auth_api_configuration_variables
from .engines.auth import engine as auth_engine
from .routers.auth import router as auth_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with auth_engine.begin() as connection:
        await connection.run_sync(AuthBase.metadata.create_all)
    yield


auth_api = FastAPI(
    title="Auth API's",
    version=auth_api_configuration_variables.APP_VERSION,
    debug=auth_api_configuration_variables.ENVIRONMENT != "production",
    deprecated=False,
    include_in_schema=True,
    description="Auth api's microservice.",
    summary="Auth api's microservice.",
    lifespan=lifespan,
    docs_url="/documentation/Swagger",
    redoc_url="/documentation/ReDoc",
    openapi_url="/documentation/openapi.json",
    license_info={
        "name": "MIT License",
        "identifier": "MIT",
    },
    contact={
        "name": "Avi Tiwari",
        "email": "email@example.com",
    },
)

auth_api.include_router(
    auth_router,
    prefix=f"/api/v{auth_api_configuration_variables.API_VERSION}",
)
