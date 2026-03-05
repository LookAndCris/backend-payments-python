import time
import logging
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request

logger = logging.getLogger(__name__)


class TimingMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, request: Request, call_next):
        start = time.perf_counter()

        response = await call_next(request)

        duration = (time.perf_counter() - start) * 1000

        logger.info(
            f"request_completed path={request.url.path} "
            f"method={request.method} duration_ms={round(duration, 2)}"
        )

        # logger.info(
        #     "request_completed",
        #     extra={
        #         "path": request.url.path,
        #         "method": request.method,
        #         "duration_ms": round(duration, 2),
        #     },
        # )

        return response