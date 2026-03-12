from fastapi import FastAPI
from app.api.routes import router
from app.api.health import router as health_router
from app.api.errors import register_exception_handlers
from app.infrastructure.logging.logger import setup_logging
from app.infrastructure.middleware.timing import TimingMiddleware
from app.api.auth.auth_routes import router as auth_router

setup_logging()

app = FastAPI(title="Payment Service")

app.add_middleware(TimingMiddleware)

app.include_router(router)
app.include_router(auth_router)
app.include_router(health_router)

register_exception_handlers(app)
