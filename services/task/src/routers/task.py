from fastapi import APIRouter

from ..endpoints.rest.task import router as task_router

router = APIRouter()

router.include_router(task_router)
