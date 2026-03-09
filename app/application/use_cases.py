from typing import Optional

from app.domain.repositories import PaymentRepository
from app.domain.models import Payment
from app.domain.exceptions import PaymentNotFound

from app.application.dto import CreatePaymentCommand
from app.infrastructure.cache.payment_cache import PaymentCache

from app.infrastructure.logging.log import logger


class CreatePayment:

    def __init__(self, repository: PaymentRepository):
        self.repository = repository

    async def execute(self, command: CreatePaymentCommand) -> Payment:

        existing = await self.repository.get_by_idempotency_key(command.idempotency_key)

        if existing:

            logger.info(
                "payment_idempotent_hit",
                payment_id=existing.id,
                idempotency_key=command.idempotency_key,
            )

            return existing

        payment = Payment.create(
            amount=command.amount,
            currency=command.currency,
            description=command.description,
            idempotency_key=command.idempotency_key,
        )

        await self.repository.save(payment)

        logger.info(
            "payment_created",
            payment_id=payment.id,
            amount=payment.amount,
            currency=payment.currency,
        )

        return payment


class GetPayment:

    def __init__(self, repository: PaymentRepository, cache: PaymentCache):
        self.repository = repository
        self.cache = cache

    async def execute(self, payment_id: str) -> Payment:

        # intentar cache
        cached = await self.cache.get(payment_id)

        if cached:

            logger.info("payment_cache_hit", payment_id=payment_id)

            return cached

        logger.info("payment_cache_miss", payment_id=payment_id)

        payment = await self.repository.get_by_id(payment_id)

        if not payment:

            logger.warning("payment_not_found", payment_id=payment_id)

            raise PaymentNotFound(f"Payment {payment_id} not found")

        await self.cache.set(payment)

        return payment
