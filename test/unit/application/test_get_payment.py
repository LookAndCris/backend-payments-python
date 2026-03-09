from unittest.mock import AsyncMock

import pytest

from app.application.use_cases import GetPayment


@pytest.mark.asyncio
async def test_get_payment_cache_hit(mocker):

    repository = AsyncMock()

    cache = AsyncMock()

    payment = mocker.Mock()

    cache.get.return_value = payment

    use_case = GetPayment(repository, cache)

    result = await use_case.execute("payment-id")

    assert result == payment

    repository.get_by_id.assert_not_called()


@pytest.mark.asyncio
async def test_get_payment_cache_miss(mocker):

    repository = AsyncMock()

    cache = AsyncMock()

    payment = mocker.Mock()

    cache.get.return_value = None

    repository.get_by_id.return_value = payment

    use_case = GetPayment(repository, cache)

    result = await use_case.execute("payment-id")

    assert result == payment

    repository.get_by_id.assert_called_once()


from app.domain.exceptions import PaymentNotFound


@pytest.mark.asyncio
async def test_get_payment_not_found(mocker):

    repository = AsyncMock()

    cache = AsyncMock()

    cache.get.return_value = None

    repository.get_by_id.return_value = None

    use_case = GetPayment(repository, cache)

    with pytest.raises(PaymentNotFound):
        await use_case.execute("missing")
