from app.domain.repositories import PaymentRepository
from app.domain.models import Payment
from app.application.dto import CreatePaymentCommand
from app.domain.exceptions import PaymentNotFound, DuplicatePayment
from typing import Optional 

class CreatePayment:
    def __init__(self, repository: PaymentRepository):
        self.repository = repository

    async def execute(self, command: CreatePaymentCommand) -> Payment:

        existing = await self.repository.get_by_idempotency_key(
            command.idempotency_key
            )

        if existing:
            return existing 
    
        payment = Payment.create(
        amount=command.amount,
        currency=command.currency,
        description=command.description,
        idempotency_key=command.idempotency_key,
    )

        await self.repository.save(payment)
        return payment  

class GetPayment:
    def __init__(self, repository: PaymentRepository):
        self.repository = repository

    async def execute(self, payment_id: str) -> Payment:
        payment = await self.repository.get_by_id(payment_id)

        if not payment:
            raise PaymentNotFound(f"Payment {payment_id} not found")

        return payment
