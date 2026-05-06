from pydantic_settings import BaseSettings
from functools import lru_cache
from pathlib import Path

class Settings(BaseSettings):
    MONGODB_URL: str
    DATABASE_NAME: str = "user_db"

    SMTP_USERNAME: str
    SMTP_PASSWORD: str
    SMTP_HOST: str = "smtp.mailgun.org"
    SMTP_PORT: int = 587

    CHECKIN_SECRET: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


@lru_cache()
def get_settings() -> Settings:
    return Settings()  # type: ignore