import redis.asyncio as redis

import os
import redis.asyncio as redis

ENV = "test"  # Cambia a "production" en producción
# ENV = os.getenv("ENV", "dev")

if ENV == "test":
    redis_client = None
else:
    redis_client = redis.Redis(
        host="localhost",
        port=6379,
        decode_responses=True,
    )
