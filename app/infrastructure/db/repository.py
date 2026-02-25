from typing import Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.models import Payment, PaymentStatus
from app.domain.repositories import PaymentRepository

from .models import PaymentORM
from .session import AsyncSessionLocal


class PostgresPaymentRepository(PaymentRepository):
    def __init__(self, session_factory=AsyncSessionLocal):
        self._session_factory = session_factory

    async def save(self, payment: Payment) -> None:
        async with self._session_factory() as session:
            orm_obj = PaymentORM(
                id=payment.id,
                amount=payment.amount,
                currency=payment.currency,
                description=payment.description,
                status=payment.status.value,
                idempotency_key=payment.idempotency_key,
            )

            session.add(orm_obj)
            await session.commit()

    async def get_by_id(self, payment_id: str) -> Optional[Payment]:
        async with self._session_factory() as session:
            stmt = select(PaymentORM).where(PaymentORM.id == payment_id)
            result = await session.execute(stmt)
            orm_obj = result.scalar_one_or_none()

            if not orm_obj:
                return None

            return self._to_domain(orm_obj)

    async def get_by_idempotency_key(self, key: str) -> Optional[Payment]:
        async with self._session_factory() as session:
            stmt = select(PaymentORM).where(
                PaymentORM.idempotency_key == key
            )
            result = await session.execute(stmt)
            orm_obj = result.scalar_one_or_none()

            if not orm_obj:
                return None

            return self._to_domain(orm_obj)

    def _to_domain(self, orm: PaymentORM) -> Payment:
        return Payment(
            id=orm.id,
            amount=orm.amount,
            currency=orm.currency,
            description=orm.description,
            status=PaymentStatus(orm.status),
            idempotency_key=orm.idempotency_key,
        )