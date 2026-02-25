from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import declarative_base

DATABASE_URL = (
    "postgresql+asyncpg://payments_user:payments_pass@localhost:5432/payments"
)

engine = create_async_engine(
    DATABASE_URL,
    echo=True,  #TODO: Cambiar a False en producción
)

AsyncSessionLocal = async_sessionmaker(
    engine,
    expire_on_commit=False,
)

Base = declarative_base()