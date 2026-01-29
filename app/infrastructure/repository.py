from typing import Dict, Optional
from app.domain.repositories import PaymentRepository
from app.domain.models import Payment


class InMemoryPaymentRepository(PaymentRepository):
    def __init__(self):
        self._payments_by_id: Dict[str, Payment] = {}
        self._payments_by_idempotency: Dict[str, Payment] = {}

    def save(self, payment: Payment) -> None:
        self._payments_by_id[payment.id] = payment
        self._payments_by_idempotency[payment.idempotency_key] = payment

    def get_by_id(self, payment_id: str) -> Optional[Payment]:
        return self._payments_by_id.get(payment_id)

    def get_by_idempotency_key(self, key: str) -> Optional[Payment]:
        return self._payments_by_idempotency.get(key)
