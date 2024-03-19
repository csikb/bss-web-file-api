from fastapi import FastAPI
from fastapi.testclient import TestClient

from bss_web_file_server.routers import health

app = FastAPI()
app.include_router(health.router)
client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.text == "UP"


def test_ping():
    response = client.get("/ping")
    assert response.status_code == 200
    assert response.text == "PONG"
