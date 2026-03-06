from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import declarative_base
from sqlalchemy.pool import NullPool

from app.core.config import settings

Base = declarative_base()


# ---------- ENGINE ----------

if settings.TESTING:

    engine = create_async_engine(
        settings.DATABASE_URL,
        echo=False,
        poolclass=NullPool,
    )

elif settings.PRODUCTION:

    engine = create_async_engine(
        settings.DATABASE_URL,
        echo=False,
        pool_size=10,
        max_overflow=20,
        pool_pre_ping=True,
    )

else:  # development

    engine = create_async_engine(
        settings.DATABASE_URL,
        echo=True,
        pool_pre_ping=True,
    )


# ---------- SESSION ----------

AsyncSessionLocal = async_sessionmaker(
    engine,
    expire_on_commit=False,
)
