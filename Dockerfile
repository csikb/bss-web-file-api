FROM golang:1.22.0-alpine3.19 as builder

WORKDIR /project

COPY go.mod go.sum ./

RUN go mod download

COPY ./ ./

RUN go build -o ./app main.go

FROM scratch

WORKDIR /project

COPY --from=builder /project/app ./app

CMD ["./app"]
