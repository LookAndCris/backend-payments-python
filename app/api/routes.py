from fastapi import APIRouter, Depends, status, HTTPException
from app.api.schemas import CreatePaymentRequest, PaymentResponse
from app.application.dto import CreatePaymentCommand
from app.application.use_cases import CreatePayment, GetPayment
from app.api.dependencies import (
    get_create_payment_use_case,
    get_get_payment_use_case,
)
from app.domain.exceptions import PaymentNotFound
from app.api.security.api_key import verify_api_key
from app.api.security.jwt_auth import verify_jwt

router = APIRouter(dependencies=[Depends(verify_api_key), Depends(verify_jwt)])


@router.post(
    "/payments",
    response_model=PaymentResponse,
    status_code=status.HTTP_201_CREATED,
)
async def create_payment(
    request: CreatePaymentRequest,
    use_case: CreatePayment = Depends(get_create_payment_use_case),
):
    command = CreatePaymentCommand(
        amount=request.amount,
        currency=request.currency,
        description=request.description,
        idempotency_key=request.idempotency_key,
    )

    payment = await use_case.execute(command)

    return PaymentResponse(
        id=payment.id,
        amount=payment.amount,
        currency=payment.currency,
        description=payment.description,
        status=payment.status.value,
    )


@router.get(
    "/payments/{payment_id}",
    response_model=PaymentResponse,
)
async def get_payment(
    payment_id: str, use_case: GetPayment = Depends(get_get_payment_use_case)
):
    try:
        payment = await use_case.execute(payment_id)
    except PaymentNotFound:
        raise HTTPException(status_code=404, detail="Payment not found")

    return PaymentResponse(
        id=payment.id,
        amount=payment.amount,
        currency=payment.currency,
        description=payment.description,
        status=payment.status.value,
    )
