async def test_get_payment(client, payment_payload):

    create = await client.post("/payments", json=payment_payload)

    payment_id = create.json()["id"]

    response = await client.get(f"/payments/{payment_id}")

    assert response.status_code == 200
    assert response.json()["id"] == payment_id
