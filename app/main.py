from fastapi import FastAPI
from app.api.routes import router
from app.api.errors import register_exception_handlers
from app.infrastructure.logging.logger import setup_logging
from app.infrastructure.middleware.timing import TimingMiddleware

setup_logging()

app = FastAPI(title="Payment Service")

app.add_middleware(TimingMiddleware)

app.include_router(router)

register_exception_handlers(app)
