import logging

from pydantic_settings import BaseSettings

logging.basicConfig(level=logging.INFO)


class Settings(BaseSettings):
    """App settings."""

    PROJECT_NAME: str = "API STECHS Challenge"
    DEBUG: bool = True
    DATABASE_URL: str


settings = Settings()
