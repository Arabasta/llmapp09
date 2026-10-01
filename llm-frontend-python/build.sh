#!/usr/bin/env bash
set -euo pipefail

: "${DOCKERHUB_USERNAME:?Set DOCKERHUB_USERNAME before running this script}"
IMAGE_TAG="${IMAGE_TAG:-1.0.0}"

docker buildx build \
  --platform linux/amd64,linux/arm64 \
  --tag "${DOCKERHUB_USERNAME}/llm-frontend-python:${IMAGE_TAG}" \
  --push \
  .
