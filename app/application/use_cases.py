from typing import Optional

from app.domain.repositories import PaymentRepository
from app.domain.models import Payment
from app.domain.exceptions import PaymentNotFound, DuplicatePayment

from app.application.dto import CreatePaymentCommand

from app.infrastructure.cache.payment_cache import PaymentCache 

import logging

logger = logging.getLogger(__name__)

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
    def __init__(self, repository: PaymentRepository, cache: PaymentCache):
        self.repository = repository
        self.cache = cache
        
    async def execute(self, payment_id: str) -> Payment:
        # intentar cache
        cached = await self.cache.get(payment_id)
        if cached:
            logger.info("payment_cache_hit", extra={"payment_id": payment_id})
            return cached

        logger.info("payment_cache_miss", extra={"payment_id": payment_id})
        # ir a DB
        payment = await self.repository.get_by_id(payment_id)

        if not payment:
            raise PaymentNotFound(f"Payment {payment_id} not found")

        # guardar en cache
        await self.cache.set(payment)

        return payment
