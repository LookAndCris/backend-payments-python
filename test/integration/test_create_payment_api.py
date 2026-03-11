async def test_create_payment(client, payment_payload):

    response = await client.post("/payments", json=payment_payload)

    assert response.status_code == 201

    data = response.json()

    assert data["amount"] == 1000
    assert data["currency"] == "COP"
