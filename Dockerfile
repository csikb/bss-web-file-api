FROM golang:1.22.0-alpine3.19 AS builder
WORKDIR /project

COPY go.mod go.sum ./
RUN go mod download

COPY ./ ./
RUN go build -o ./app ./cmd/fileapi

FROM scratch as app
COPY --from=builder /project/app ./app

EXPOSE 8080
ENV BASE_PATH="/data"

CMD ["./app"]

LABEL org.opencontainers.image.source="https://github.com/BSStudio/bss-web-file-api"
LABEL org.opencontainers.image.description="BSS Web File API"
LABEL org.opencontainers.image.licenses="GPL-3.0"
