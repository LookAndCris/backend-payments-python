from app.infrastructure.repository_in_memory import InMemoryPaymentRepository
from app.infrastructure.db.repository import PostgresPaymentRepository
from app.application.use_cases import CreatePayment, GetPayment

repository = PostgresPaymentRepository()
# repository = InMemoryPaymentRepository()

def get_create_payment_use_case() -> CreatePayment:
    return CreatePayment(repository)


def get_get_payment_use_case() -> GetPayment:
    return GetPayment(repository)







