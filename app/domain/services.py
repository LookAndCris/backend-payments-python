

class PaymentService:

    def __init__(self, repository: PaymentRepository):
        self.repository = repository

    def create_payment(self, payment: Payment) -> Payment:
        existing = self.repository.get_by_idempotency_key(payment.idempotency_key)
        if existing:
            raise DuplicatePayment("Payment already exists")

        self.repository.save(payment)
        return payment
