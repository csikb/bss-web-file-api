from uuid import UUID

from src.models.member import Member


def test_should_create_member():
    url = "url"
    uid = UUID("{12345678-1234-5678-1234-567812345678}")
    member = Member(id=uid, url=url)
    assert member.id is uid
    assert member.url is url
