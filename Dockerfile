FROM python:3.12 as builder

WORKDIR /app

    # python
ENV PYTHONUNBUFFERED=1 \
    # prevents python creating .pyc files
    PYTHONDONTWRITEBYTECODE=1 \
    \
    # pip
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on

COPY ./requirements.txt ./

RUN pip wheel --no-cache-dir --no-deps --wheel-dir ./wheels -r requirements.txt

FROM python:3.12-slim AS app

# use non-root user
RUN adduser --system --group --home /home/abc abc
USER abc:abc
WORKDIR /home/abc

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

EXPOSE 80
CMD ["uvicorn", "src.bss_web_file_server.main:app", "--host", "0.0.0.0", "--port", "80"]
