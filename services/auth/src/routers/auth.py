""" """

from fastapi import APIRouter

router = APIRouter(
    prefix="/auth",
    deprecated=False,
    include_in_schema=True,
    tags=["Auth"],
)
