import redis.asyncio as redis
from app.core.config import settings

redis_client = None

if not settings.TESTING:
    redis_client = redis.from_url(settings.REDIS_URL)
