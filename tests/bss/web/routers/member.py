from uuid import UUID

from fastapi.testclient import TestClient

from bss.web.routers.member import router

client = TestClient(router)


def test_create_member_folder(mocker):
    video = {
        "id": "01234567-0123-0123-0123-0123456789ab",
        "url": "url"
    }
    response = client.post("/api/v1/member", json=video)
    assert response.json() == video
