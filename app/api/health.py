from fastapi import APIRouter
from sqlalchemy import text

from app.infrastructure.db.session import engine
from app.infrastructure.cache.redis_client import redis_client

router = APIRouter()


@router.get("/health")
async def health_check():

    db_status = "up"
    redis_status = "up"

    # check database

    try:
        async with engine.connect() as conn:
            await conn.execute(text("SELECT 1"))
    except Exception:
        db_status = "down"

    # check redis

    if redis_client is not None:
        try:
            await redis_client.ping()
        except Exception:
            redis_status = "down"
    else:
        redis_status = "disabled"

    # overall status

    status = "ok"

    if db_status != "up" or redis_status not in ("up", "disabled"):
        status = "degraded"

    return {
        "status": status,
        "services": {
            "database": db_status,
            "redis": redis_status,
        },
    }
