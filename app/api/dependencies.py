from app.infrastructure.repository import InMemoryPaymentRepository
from app.application.use_cases import CreatePayment, GetPayment


repository = InMemoryPaymentRepository()

def get_create_payment_use_case() -> CreatePayment:
    return CreatePayment(repository)


def get_get_payment_use_case() -> GetPayment:
    return GetPayment(repository)
