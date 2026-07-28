"""Task Service."""

from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from .bases.task import TaskBase
from .engines.task import engine as task_engine
from .exceptions.task_not_found_error import TaskNotFoundError
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


@app.exception_handler(TaskNotFoundError)
async def task_not_found_handler(
    request: Request,
    exc: TaskNotFoundError,
):
    return JSONResponse(
        status_code=404,
        content={
            "detail": "Task not found.",
        },
    )


@app.get(
    "/health",
    tags=["Health"],
)
async def health() -> dict[str, str]:
    """Health check."""

    return {
        "status": "healthy",
    }
