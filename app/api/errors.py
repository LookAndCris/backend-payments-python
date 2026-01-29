from fastapi import FastAPI, HTTPException
from app.domain.exceptions import InvalidAmount, DuplicatePayment


def register_exception_handlers(app: FastAPI):

    @app.exception_handler(InvalidAmount)
    async def invalid_amount_handler(_, exc: InvalidAmount):
        raise HTTPException(status_code=400, detail=str(exc))

    @app.exception_handler(DuplicatePayment)
    async def duplicate_payment_handler(_, exc: DuplicatePayment):
        raise HTTPException(status_code=409, detail=str(exc))
