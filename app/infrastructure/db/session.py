from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import declarative_base
from sqlalchemy.pool import NullPool

ENV = "test"  # Cambia a "production" en producción

DATABASE_URL = (
    "postgresql+asyncpg://payments_user:payments_pass@localhost:5432/payments"
)

if ENV == "test":
    engine = create_async_engine(
        DATABASE_URL,
        echo=True,  # TODO: Cambiar a False en producción
        poolclass=NullPool,
    )
else:
    engine = create_async_engine(
        DATABASE_URL,
        echo=False,
    )

AsyncSessionLocal = async_sessionmaker(
    engine,
    expire_on_commit=False,
)

Base = declarative_base()
