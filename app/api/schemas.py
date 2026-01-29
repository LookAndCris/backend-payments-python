from pydantic import BaseModel, Field


class CreatePaymentRequest(BaseModel):
    amount: int = Field(gt=0)
    currency: str
    description: str
    idempotency_key: str

class PaymentResponse(BaseModel):
    id: str
    amount: int
    currency: str
    description: str
    status: str
