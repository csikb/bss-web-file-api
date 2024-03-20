FROM python:3.12 AS builder-base

WORKDIR /app
    # python
ENV PYTHONUNBUFFERED=1 \
    # prevents python creating .pyc files
    PYTHONDONTWRITEBYTECODE=1 \
    \
    # pip
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on

FROM builder-base AS lock

RUN pip install --no-cache-dir poetry==1.8.2
COPY ./pyproject.toml ./poetry.lock ./
RUN poetry export  --output requirements.txt

FROM builder-base AS builder

COPY --from=lock /app/requirements.txt ./
RUN pip wheel --no-cache-dir --no-deps --wheel-dir ./wheels -r requirements.txt

FROM python:3.12-slim AS app

RUN adduser --system --group --home /home/nonroot nonroot
ENV PATH="/home/nonroot/.local/bin:${PATH}"
USER nonroot:nonroot
WORKDIR /home/nonroot/app

    # python
ENV PYTHONUNBUFFERED=1 \
    # prevents python creating .pyc files
    PYTHONDONTWRITEBYTECODE=1 \
    \
    # pip
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on

COPY --from=builder /app/wheels ./wheels
COPY --from=builder /app/requirements.txt ./

RUN pip install --no-cache-dir ./wheels/*

COPY ./src ./src

CMD ["uvicorn", "src.bss_web_file_server.main:app", "--host", "0.0.0.0", "--port", "80"]
EXPOSE 80
LABEL org.opencontainers.image.source="https://github.com/BSStudio/bss-web-file-api"
LABEL org.opencontainers.image.description="BSS Web file API"
LABEL org.opencontainers.image.licenses="GPL-3.0"
