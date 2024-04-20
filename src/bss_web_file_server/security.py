"""Security module for the FastAPI application."""

import secrets
from typing import Annotated

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials

from .settings import settings

security = HTTPBasic()


def authorize(credentials: Annotated[HTTPBasicCredentials, Depends(security)]):
    """
    Authorize the request with the correct username and password.
    The correct username and password are stored in the settings.
    :param credentials: the credentials from the request
    :return:
    """
    current_username_bytes = credentials.username.encode("utf8")
    correct_username_bytes = settings.username.encode("utf8")
    is_correct_username = secrets.compare_digest(
        current_username_bytes, correct_username_bytes
    )
    current_password_bytes = credentials.password.encode("utf8")
    correct_password_bytes = settings.password.encode("utf8")
    is_correct_password = secrets.compare_digest(
        current_password_bytes, correct_password_bytes
    )
    if not (is_correct_username and is_correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Basic"},
        )
