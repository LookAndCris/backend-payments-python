import pytest

from app.domain.models import Payment
from app.domain.exceptions import InvalidAmount


def test_create_payment_success():

    payment = Payment.create(
        amount=1000,
        currency="COP",
        description="Test payment",
        idempotency_key="key-123",
    )

    assert payment.amount == 1000
    assert payment.currency == "COP"
    assert payment.status.value == "pending"
    assert payment.id is not None


def test_create_payment_invalid_amount():

    with pytest.raises(InvalidAmount):

        Payment.create(
            amount=0,
            currency="COP",
            description="Invalid payment",
            idempotency_key="key-123",
        )
