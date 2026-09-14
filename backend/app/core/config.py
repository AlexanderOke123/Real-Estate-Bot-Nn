from pydantic_settings import BaseSettings
from typing import List


class Settings(BaseSettings):
    APP_NAME: str = "PrimeHomes Lead Bot"
    APP_ENV: str = "development"
    DEBUG: bool = True

    API_V1_PREFIX: str = "/api/v1"

    # MySQL (local development)
    # Format: mysql+pymysql://USER:PASSWORD@HOST:PORT/DATABASE
    DATABASE_URL: str = "mysql+pymysql://root:password@localhost:3306/real_estate_leads"

    # Auth (for later sales dashboard)
    JWT_SECRET: str = "change-me-to-a-long-random-string-in-production"
    JWT_ALGORITHM: str = "HS256"
    JWT_ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    # CORS
    CORS_ORIGINS: List[str] = [
        "http://localhost:3000",
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "http://127.0.0.1:3000",
    ]

    # n8n integration
    N8N_WEBHOOK_URL: str = "http://localhost:5678/webhook/lead-process-message"
    N8N_WEBHOOK_SECRET: str = "change-me-n8n-secret"

    class Config:
        env_file = ".env"
        case_sensitive = True
        extra = "ignore"


settings = Settings()
