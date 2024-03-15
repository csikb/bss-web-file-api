FROM python:3.12-slim as builder
WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
COPY requirements.txt ./

RUN apt-get install --no-install-recommends -y build-essential
RUN pip wheel --no-cache-dir --no-deps --wheel-dir ./wheels -r requirements.txt

FROM python:3.12-alpine

COPY --from=builder /app/wheels /wheels
COPY --from=builder /app/requirements.txt .

RUN pip install --no-cache /wheels/*

COPY ./src ./src

EXPOSE 80
CMD ["uvicorn", "src.bss_web_file_server.main:app", "--host", "0.0.0.0", "--port", "80"]
