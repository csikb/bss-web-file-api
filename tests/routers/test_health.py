import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient

from bss_web_file_server.routers import health


@pytest.fixture
def client():
    app = FastAPI()
    app.include_router(health.router)
    return TestClient(app=app)


def test_health(client: TestClient):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.text == "UP"


def test_ping(client: TestClient):
    response = client.get("/ping")
    assert response.status_code == 200
    assert response.text == "PONG"
