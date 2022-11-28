from pydantic import BaseSettings


class Settings(BaseSettings):
    server_base_path: str = "./assets/"


settings = Settings()
