# BSS Web - File API

![CircleCI](https://img.shields.io/circleci/build/github/BSStudio/bss-web-file-api/main?label=build)
![GitHub branch checks state](https://img.shields.io/github/checks-status/BSStudio/bss-web-file-api/main)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/BSStudio/bss-web-file-api)
![GitHub](https://img.shields.io/github/license/BSStudio/bss-web-file-api)
[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=BSStudio_bss-web-file-api&metric=bugs)](https://sonarcloud.io/dashboard?id=BSStudio_bss-web-file-api)
[![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=BSStudio_bss-web-file-api&metric=code_smells)](https://sonarcloud.io/dashboard?id=BSStudio_bss-web-file-api)
[![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=BSStudio_bss-web-file-api&metric=duplicated_lines_density)](https://sonarcloud.io/dashboard?id=BSStudio_bss-web-file-api)
[![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=BSStudio_bss-web-file-api&metric=ncloc)](https://sonarcloud.io/dashboard?id=BSStudio_bss-web-file-api)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=BSStudio_bss-web-file-api&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=BSStudio_bss-web-file-api)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=BSStudio_bss-web-file-api&metric=alert_status)](https://sonarcloud.io/dashboard?id=BSStudio_bss-web-file-api)
[![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=BSStudio_bss-web-file-api&metric=reliability_rating)](https://sonarcloud.io/dashboard?id=BSStudio_bss-web-file-api)
[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=BSStudio_bss-web-file-api&metric=security_rating)](https://sonarcloud.io/dashboard?id=BSStudio_bss-web-file-api)
[![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=BSStudio_bss-web-file-api&metric=sqale_index)](https://sonarcloud.io/dashboard?id=BSStudio_bss-web-file-api)
[![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=BSStudio_bss-web-file-api&metric=vulnerabilities)](https://sonarcloud.io/dashboard?id=BSStudio_bss-web-file-api)

This server will create a file structure for newly created users and videos.
Any time someone creates a new video or user, the API will create a folder and a symbolic link to the file.
Later the symbolic link will help to access the same file from different locations.

For example each user has a uuid and a unique url that they can change.
The uuid can not be changed.

The file structure will look like this:
```
📁
├─ 📁 m/
│  ├─ 📁 <uuid>/
│  │  ├─ 🖼️ profilePicture.jpg
│  │  ├─ 🖼️ profilePicture.png
│  │  ├─ 🖼️ profilePicture.webp
│  │  ├─ 🖼️ profilePicture.avif
├─ 📁 member/
│  ├─ 📁 <url>/ --> /m/<uuid>
├─ 📁 v/
│  ├─ 📁 <uuid>/
│  │  ├─ 📄️ prog_index.m3u8
│  │  ├─ 📁️ thumbnail/
│  │  │  ├─ 🖼️ thumbnail.jpg
│  │  │  ├─ 🖼️ thumbnail.png
│  │  │  ├─ 🖼️ thumbnail.webp
│  │  │  ├─ 🖼️ thumbnail.avif
│  │  ├─ 📁️ v1/
│  │  │  ├─ 📄️ prog_index.m3u8
│  │  │  ├─ 🎞️ fileSequence0.ts
│  │  │  ├─ [...]
│  │  ├─ 📁️ a1/
│  │  │  ├─ 📄️ prog_index.m3u8
│  │  │  ├─ 🎵️ fileSequence0.aac
│  │  │  ├─ [...]
├─ 📁 video/
│  ├─ 📁 <url>/ --> /v/<uuid>
├─ 📁 e/
│  │  ├─ 🖼️ thumbnail.jpg
│  │  ├─ 🖼️ thumbnail.png
│  │  ├─ 🖼️ thumbnail.webp
│  │  ├─ 🖼️ thumbnail.avif
├─ 📁 event/
│  ├─ 📁 <url>/ --> /e/<uuid>
```
The videos are hosted from the video studio's on premise server.
To make the workflow easier, the video editors need a convenient way to upload the videos to the server.

This will help the video editors to find the folder where their videos should be stored.

## Development

### Prerequisites

1. Install Go: https://golang.org/doc/install
1. Install golangci-lint: https://golangci-lint.run/usage/install/
1. (recomennded) Install Docker: https://docs.docker.com/get-docker/
1. (optional) Install goreleaser: https://goreleaser.com/install/

### Install dependencies

```bash
go mod download
```

### Run the application

```bash
go run ./cmd/fileapi
```

### Run tests

```bash
go test
```

### Lint

```bash
golangci-lint run
```

### Build

```bash
go build -o fileapi ./cmd/fileapi
```

Running the applications differs based on the environment.

### Build and run Docker image

The `BASE_PATH` environment variable is set to`/data` by default in the image.

```bash
docker build -t bsstudio/bss-web-file-api .
docker run -p 8080:8080 -v /your/local/folder:/data bsstudio/bss-web-file-api
```

## Environment variables

| Name      | Description                           | Default       |
|-----------|---------------------------------------|---------------|
| BASE_PATH | The base path for the file operations | $HOME/fileapi |

