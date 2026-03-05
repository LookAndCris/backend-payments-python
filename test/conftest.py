import pytest
from httpx import AsyncClient, ASGITransport

from app.main import app
from app.infrastructure.db.session import engine


@pytest.fixture
async def client():
    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://test"
    ) as client:
        yield client


@pytest.fixture(scope="session", autouse=True)
async def shutdown_engine():
    # se ejecuta después de todos los tests
    yield
    await engine.dispose()
