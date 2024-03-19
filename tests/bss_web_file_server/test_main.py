from fastapi import APIRouter
from fastapi.testclient import TestClient

from bss_web_file_server.main import app


def test_main_startup(mocker):
    mocker.patch("bss_web_file_server.routers.health").router = APIRouter()
    mocker.patch("bss_web_file_server.routers.member").router = APIRouter()
    mocker.patch("bss_web_file_server.routers.video").router = APIRouter()

    member_service_mock = mocker.patch("bss_web_file_server.main.MemberService")
    member_service_mock.create_base_path.return_value = None
    video_service_mock = mocker.patch("bss_web_file_server.main.VideoService")
    video_service_mock.create_base_path.return_value = None

    with TestClient(app) as client:
        response = client.get("/docs")
        assert response.status_code == 200
    assert member_service_mock.create_base_path.call_count == 1
    assert video_service_mock.create_base_path.call_count == 1
