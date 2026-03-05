import os


class Settings:

    ENV: str = os.getenv("ENV", "development")

    DATABASE_URL: str = os.getenv(
        "DATABASE_URL",
        "postgresql+asyncpg://payments_user:payments_pass@localhost:5432/payments",
    )

    REDIS_URL: str = os.getenv(
        "REDIS_URL",
        "redis://localhost:6379",
    )

    DEBUG: bool = ENV == "development"

    TESTING: bool = ENV == "test"

    PRODUCTION: bool = ENV == "production"


settings = Settings()
