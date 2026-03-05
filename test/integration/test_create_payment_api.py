import pytest


async def test_create_payment(client):

    payload = {
        "amount": 10000,
        "currency": "COP",
        "description": "Integration payment",
        "idempotency_key": "create-test",
    }

    response = await client.post("/payments", json=payload)

    assert response.status_code == 201

    data = response.json()

    assert data["amount"] == 10000
    assert data["currency"] == "COP"
