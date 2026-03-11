async def test_api_key_required(anon_client, payment_payload):

    response = await anon_client.post(
        "/payments",
        json=payment_payload,
    )

    assert response.status_code == 401
