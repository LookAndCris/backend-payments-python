import pytest


async def test_get_payment(client):

    payload = {
        "amount": 9000,
        "currency": "COP",
        "description": "Fetch payment",
        "idempotency_key": "fetch-test",
    }

    create = await client.post("/payments", json=payload)

    payment_id = create.json()["id"]

    response = await client.get(f"/payments/{payment_id}")

    assert response.status_code == 200
    assert response.json()["id"] == payment_id
