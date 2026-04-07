from slowapi import Limiter
from slowapi.util import get_remote_address
from app.core.config import settings
from app.infrastructure.rate_limit.key_funcs import get_api_key


def get_storage_uri():
    # usamos Redis en producción
    if settings.TESTING:
        return "memory://"
    return settings.REDIS_URL


limiter = Limiter(
    key_func=get_api_key,
    storage_uri=get_storage_uri(),
)
