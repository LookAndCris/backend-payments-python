import os

os.environ["ENV"] = "test"

import pytest
from httpx import AsyncClient, ASGITransport

from app.main import app
from app.core.config import settings
from app.infrastructure.db.session import engine


@pytest.fixture
async def client():

    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url="http://test",
        headers={"X-API-Key": settings.API_KEY},
    ) as client:
        yield client


@pytest.fixture
async def anon_client():

    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url="http://test",
    ) as client:
        yield client


@pytest.fixture
def payment_payload():
    return {
        "amount": 1000,
        "currency": "COP",
        "description": "test",
        "idempotency_key": "test-key",
    }


@pytest.fixture(scope="session", autouse=True)
async def shutdown_engine():

    yield
    await engine.dispose()
