"""Settings for the web file server."""

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Class for reading settings from environment variables."""

    server_base_path: str = "./assets/"
    username: str = "admin"
    password: str = "password"


settings = Settings()
