import pytest
from fastapi import Depends, FastAPI
from fastapi.security import HTTPBasicCredentials
from fastapi.testclient import TestClient

from src.security import authorize


@pytest.fixture
def client():
    app = FastAPI()

    @app.get("/secure-endpoint", dependencies=[Depends(authorize)])
    def secure_endpoint():
        return {"message": "You are authorized"}

    return TestClient(app)


def test_authorize_correct_credentials(mocker, client):
    credentials = HTTPBasicCredentials(username="admin", password="password")
    mocker.patch("src.security.security", return_value=credentials)

    response = client.get(
        "/secure-endpoint", auth=(credentials.username, credentials.password)
    )

    assert response.status_code == 200
    assert response.json() == {"message": "You are authorized"}


def test_authorize_incorrect_credentials(mocker, client):
    credentials = HTTPBasicCredentials(username="admin", password="password")
    mocker.patch("src.security.security", return_value=credentials)

    response = client.get("/secure-endpoint", auth=("wrong", "wrong"))

    assert response.status_code == 401
    assert response.json() == {"detail": "Incorrect username or password"}
