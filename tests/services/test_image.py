from pathlib import Path

from bss_web_file_server.services.image import ImgFormat, create_images


def test_create_images(tmp_path):
    img_file = Path(__file__).parent.joinpath("mountains.jpg").read_bytes()
    image_sizes = [
        ImgFormat(300, 300, "large"),
        ImgFormat(200, 200, "medium"),
        ImgFormat(100, 100, "small"),
    ]

    create_images(img_file, tmp_path, image_sizes)

    assert Path(tmp_path, "large.avif").exists()
    assert Path(tmp_path, "large.webp").exists()
    assert Path(tmp_path, "large.jpeg").exists()
    assert Path(tmp_path, "medium.avif").exists()
    assert Path(tmp_path, "medium.webp").exists()
    assert Path(tmp_path, "medium.jpeg").exists()
    assert Path(tmp_path, "small.avif").exists()
    assert Path(tmp_path, "small.webp").exists()
    assert Path(tmp_path, "small.jpeg").exists()
