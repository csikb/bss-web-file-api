from bss_web_file_server.settings import Settings


def test_settings_default_values():
    settings = Settings()
    assert settings.server_base_path == "./assets/"
    assert settings.username == "admin"
    assert settings.password == "password"
