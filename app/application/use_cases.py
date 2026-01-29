from app.domain.repositories import PaymentRepository
from app.domain.models import Payment
from app.application.commands import CreatePaymentCommand
from app.domain.exceptions import PaymentNotFoundError, DuplicatePaymentError
from typing import Optional 

class CreatePayment:
    def __init__(self, repository: PaymentRepository):
        self.repository = repository

    def execute(self, command: CreatePaymentCommand) -> Payment:
        ...

class GetPayment:
    def __init__(self, repository: PaymentRepository):
        self.repository = repository

    def execute(self, payment_id: str) -> Payment:
        ...
