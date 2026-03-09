import pytest
from unittest.mock import AsyncMock

from app.application.use_cases import CreatePayment
from app.application.dto import CreatePaymentCommand
from app.domain.models import Payment


@pytest.mark.asyncio
async def test_create_payment_success(mocker):

    repository = AsyncMock()

    repository.get_by_idempotency_key.return_value = None

    use_case = CreatePayment(repository)

    command = CreatePaymentCommand(
        amount=1000,
        currency="COP",
        description="Test payment",
        idempotency_key="test-key",
    )

    payment = await use_case.execute(command)

    assert payment.amount == 1000
    assert payment.currency == "COP"

    repository.save.assert_called_once()


@pytest.mark.asyncio
async def test_create_payment_idempotent(mocker):

    repository = AsyncMock()

    existing_payment = mocker.Mock()

    repository.get_by_idempotency_key.return_value = existing_payment

    use_case = CreatePayment(repository)

    command = CreatePaymentCommand(
        amount=1000,
        currency="COP",
        description="Test payment",
        idempotency_key="same-key",
    )

    payment = await use_case.execute(command)

    assert payment == existing_payment

    repository.save.assert_not_called()
