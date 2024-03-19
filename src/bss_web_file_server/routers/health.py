"""Health check endpoints."""

from fastapi import APIRouter
from fastapi.responses import PlainTextResponse

router = APIRouter(tags=["Health"])


@router.get("/health", response_class=PlainTextResponse)
async def health():
    """Health check endpoint."""
    return "UP"


@router.get("/ping", response_class=PlainTextResponse)
async def ping():
    """Ping check endpoint."""
    return "PONG"
