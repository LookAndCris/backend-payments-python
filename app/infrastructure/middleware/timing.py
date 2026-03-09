import time
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request

from app.infrastructure.logging.log import logger


class TimingMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, request: Request, call_next):

        start = time.perf_counter()

        response = await call_next(request)

        duration = (time.perf_counter() - start) * 1000

        logger.info(
            "request_completed",
            path=request.url.path,
            method=request.method,
            duration_ms=round(duration, 2),
            status_code=response.status_code,
        )

        return response
