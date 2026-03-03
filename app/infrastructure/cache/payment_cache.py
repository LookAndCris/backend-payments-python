import json
from typing import Optional

from app.domain.models import Payment, PaymentStatus
from .redis_client import redis_client


class PaymentCache:
    PREFIX = "payment:"

    async def get(self, payment_id: str) -> Optional[Payment]:
        data = await redis_client.get(self.PREFIX + payment_id)
        if not data:
            return None

        obj = json.loads(data)

        return Payment(
            id=obj["id"],
            amount=obj["amount"],
            currency=obj["currency"],
            description=obj["description"],
            status=PaymentStatus(obj["status"]),
            idempotency_key=obj["idempotency_key"],
        )

    async def set(self, payment: Payment, ttl: int = 300) -> None:
        payload = json.dumps({
            "id": payment.id,
            "amount": payment.amount,
            "currency": payment.currency,
            "description": payment.description,
            "status": payment.status.value,
            "idempotency_key": payment.idempotency_key,
        })

        await redis_client.set(
            self.PREFIX + payment.id,
            payload,
            ex=ttl,
        )