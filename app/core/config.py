import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings

ENV = os.getenv("ENV", "development")

if ENV == "test":
    load_dotenv(".env.test")
elif ENV == "production":
    load_dotenv(".env.production")
else:
    load_dotenv(".env")


class Settings(BaseSettings):

    ENV: str = "development"

    POSTGRES_HOST: str
    POSTGRES_PORT: int
    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str

    REDIS_HOST: str
    REDIS_PORT: int

    API_KEY: str

    @property
    def DATABASE_URL(self):

        return (
            f"postgresql+asyncpg://{self.POSTGRES_USER}:"
            f"{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:"
            f"{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
        )

    @property
    def REDIS_URL(self):
        return f"redis://{self.REDIS_HOST}:{self.REDIS_PORT}"

    @property
    def TESTING(self):
        return self.ENV == "test"

    @property
    def PRODUCTION(self):
        return self.ENV == "production"

    @property
    def DEVELOPMENT(self):
        return self.ENV == "development"


settings = Settings()
