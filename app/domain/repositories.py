from abc import ABC, abstractmethod
from typing import Optional
from .models import Payment


class PaymentRepository(ABC):

    @abstractmethod
    def save(self, payment: Payment) -> None:
        pass

    @abstractmethod
    def get_by_id(self, payment_id: str) -> Optional[Payment]:
        pass

    @abstractmethod
    def get_by_idempotency_key(self, key: str) -> Optional[Payment]:
        pass
