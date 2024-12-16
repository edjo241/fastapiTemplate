import os
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    DATABASE_URL: str = os.getenv("DATABASE_URL")
    UPLOAD_DIRECTORY: str = os.getenv("UPLOAD_DIRECTORY")

    class Config:
        case_sensitive = True

settings = Settings()