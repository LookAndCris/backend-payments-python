from dataclasses import dataclass

@dataclass(frozen=True)
class CreatePaymentCommand:
    amount: int
    currency: str
    description: str
    idempotency_key: str