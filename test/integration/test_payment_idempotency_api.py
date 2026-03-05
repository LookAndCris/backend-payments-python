import pytest


async def test_payment_idempotency(client):

    payload = {
        "amount": 5000,
        "currency": "COP",
        "description": "Idempotent payment",
        "idempotency_key": "idem-test",
    }

    r1 = await client.post("/payments", json=payload)
    r2 = await client.post("/payments", json=payload)

    assert r1.status_code == 201
    assert r2.status_code == 201

    assert r1.json()["id"] == r2.json()["id"]
