from uuid import UUID

from bss_web_file_server.models.video import Video


def test_should_create_video():
    url = "url"
    id = UUID("{12345678-1234-5678-1234-567812345678}")
    video = Video(id=id, url=url)
    assert video.id is id
    assert video.url is url
