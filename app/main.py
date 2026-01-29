from fastapi import FastAPI
from app.api.routes import router
from app.api.errors import register_exception_handlers


app = FastAPI(title="Payment Service")

app.include_router(router)
register_exception_handlers(app)
