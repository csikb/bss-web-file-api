# BSS Web File Server

This project aims to help the video upload process.
It will create folders for each member and video
based on their uuid.

## Run server

```shell
uvicorn src.bss_web_file_server.main:app
```

## Development

```shell
uvicorn src.bss_web_file_server.main:app --reload
```

## Lint

```shell
poetry run isort . --check
poetry run black . --check
poetry run mypy -p src.bss_web_file_server
```

Apply lint

```shell
poetry run isort .
poetry run black .
```

## Test

```shell
poetry run pytest
```

## Build docker image
```shell
docker build -t bss_web_file_server .
```

## Run docker compose
```shell
docker-compose up
```