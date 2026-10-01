# Docker deployment

The root `docker-compose.yml` builds the FastAPI backend and Flask frontend,
waits for backend readiness, and connects both services through `llm-network`.
Backend metrics persist in the `llm-metrics` named volume.

```sh
cp .env.example .env
# Set OLLAMA_API_KEY in .env.
docker compose up --build -d
docker compose ps
docker compose down
```

The GitHub workflows publish multi-architecture images as
`keiyam/llm-multiroute` and `keiyam/llm-frontend-python`. The manual
`build.sh` scripts use `DOCKERHUB_USERNAME` and optional `IMAGE_TAG`
environment variables instead of a hard-coded account.
