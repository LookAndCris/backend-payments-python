import pytest


async def test_payment_not_found(client):

    response = await client.get("/payments/does-not-exist")

    assert response.status_code == 404
