FROM python:3.11.0-alpine3.16 as builder
WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
COPY requirements.txt ./
RUN pip wheel --no-cache-dir --no-deps --wheel-dir ./wheels -r requirements.txt

FROM python:3.11.0-alpine3.16

COPY --from=builder /app/wheels /wheels
COPY --from=builder /app/requirements.txt .

RUN pip install --no-cache /wheels/*

COPY ./src ./src

RUN mkdir -p /usr/share/bss        \
             /usr/share/bss/m      \
             /usr/share/bss/member \
             /usr/share/bss/v      \
             /usr/share/bss/video
ENV SERVER_BASE_PATH="/usr/share/bss"

CMD ["uvicorn", "src.bss_web_file_server.main:app", "--host", "0.0.0.0", "--port", "80"]
