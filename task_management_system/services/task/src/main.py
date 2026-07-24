"""Task Service."""

from contextlib import asynccontextmanager

from fastapi import FastAPI

from .bases.task import TaskBase
from .engines.task import engine as task_engine
from .routers.task import router


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan."""

    async with task_engine.begin() as connection:
        await connection.run_sync(TaskBase.metadata.create_all)
    yield
    # Shutdown


app = FastAPI(
    title="Task Service",
    description="Task Management Microservice",
    version="1.0.0",
    lifespan=lifespan,
)

app.include_router(router)


@app.get(
    "/health",
    tags=["Health"],
)
async def health() -> dict[str, str]:
    """Health check."""

    return {
        "status": "healthy",
    }
