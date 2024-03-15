from uuid import UUID

from bss_web_file_server.models.video import Video


def test_should_create_video():
    urls = ["url1", "url2"]
    uid = UUID("{12345678-1234-5678-1234-567812345678}")
    video = Video(id=uid, urls=urls)
    assert video.id is uid
    for i in range(len(urls)):
        assert video.urls[i] is urls[i]
