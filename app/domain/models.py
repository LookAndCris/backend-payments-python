from enum import Enum
from dataclasses import dataclass
from uuid import uuid4
from .exceptions import InvalidAmount

class PaymentStatus(str, Enum):
    PENDING = "pending"
    COMPLETED = "completed"
    FAILED = "failed"

@dataclass
class Payment:
    id: str
    amount: int
    currency: str
    description: str
    status: PaymentStatus
    idempotency_key: str

    @staticmethod
    def create(amount: int, currency: str, description: str, idempotency_key: str) -> "Payment":
        if amount <= 0:
            raise InvalidAmount("Amount must be greater than zero")

        return Payment(
            id=str(uuid4()),
            amount=amount,
            currency=currency,
            description=description,
            status=PaymentStatus.PENDING,
            idempotency_key=idempotency_key
        )
