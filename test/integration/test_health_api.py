async def test_health_endpoint(client):

    response = await client.get("/health")

    assert response.status_code == 200

    data = response.json()

    assert "status" in data
    assert "services" in data
