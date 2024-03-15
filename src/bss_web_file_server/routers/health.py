"""Health check endpoints."""

from fastapi import APIRouter

router = APIRouter(tags=["Health"])


@router.get("/health", response_model=str)
async def health():
    return "UP"


@router.get("/ping", response_model=str)
async def ping():
    return "PONG"
