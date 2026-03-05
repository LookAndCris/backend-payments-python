from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import declarative_base
from sqlalchemy.pool import NullPool

from app.core.config import settings

Base = declarative_base()

if settings.TESTING:
    engine = create_async_engine(
        settings.DATABASE_URL,
        echo=True,
        poolclass=NullPool,
    )

elif settings.PRODUCTION:

    engine = create_async_engine(
        settings.DATABASE_URL,
        pool_size=10,
        max_overflow=20,
        echo=False,
    )

else:  # development

    engine = create_async_engine(
        settings.DATABASE_URL,
        echo=True,
    )


AsyncSessionLocal = async_sessionmaker(
    engine,
    expire_on_commit=False,
)
