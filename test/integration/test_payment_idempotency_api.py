async def test_payment_idempotency(client, payment_payload):

    r1 = await client.post("/payments", json=payment_payload)
    r2 = await client.post("/payments", json=payment_payload)

    assert r1.status_code == 201
    assert r2.status_code == 201

    assert r1.json()["id"] == r2.json()["id"]
