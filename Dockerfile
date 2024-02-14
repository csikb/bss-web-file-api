FROM golang:1.22.0-alpine3.19 as builder
WORKDIR /project

COPY go.mod go.sum ./
RUN go mod download

COPY ./ ./
RUN go build -o ./app ./cmd/fileapi

FROM scratch
WORKDIR /project

COPY --from=builder /project/app ./app
CMD ["./app"]

LABEL org.opencontainers.image.source="https://github.com/BSStudio/bss-web-file-api"
LABEL org.opencontainers.image.description="BSS Web File API"
LABEL org.opencontainers.image.licenses="GPL-3.0"

