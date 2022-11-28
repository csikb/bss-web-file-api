from uuid import UUID

from bss_web_file_server.models.member import Member


def test_should_create_member():
    url = "url"
    id = UUID("{12345678-1234-5678-1234-567812345678}")
    member = Member(id=id, url=url)
    assert member.id is id
    assert member.url is url
