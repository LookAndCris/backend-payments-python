import time
import logging
from starlette.types import ASGIApp, Receive, Scope, Send

logger = logging.getLogger(__name__)


class TimingMiddleware:

    def __init__(self, app: ASGIApp):
        self.app = app

    async def __call__(self, scope: Scope, receive: Receive, send: Send):

        if scope["type"] != "http":
            await self.app(scope, receive, send)
            return

        start = time.perf_counter()

        async def send_wrapper(message):

            if message["type"] == "http.response.start":

                duration = (time.perf_counter() - start) * 1000

                path = scope["path"]
                method = scope["method"]

                logger.info(
                    f"request_completed path={path} "
                    f"method={method} duration_ms={round(duration, 2)}"
                )

            await send(message)

        await self.app(scope, receive, send_wrapper)
