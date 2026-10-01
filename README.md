# llmapp09 - End-to-End LLMOps CI/CD

This repository is the cleaned workshop solution derived from
`darryl1975/DOAIS/llmapp09` at commit
`0565982e6ffc53a52837281074dd7f5b7a597689`.

## Components

- `llm-multiroute`: deployed FastAPI backend with model routing, guardrails, and metrics
- `llm-frontend-python`: Flask frontend and backend proxy
- `promptfoo-tests`: HTTP contract and behavior evaluations
- `deepeval-tests`: model-graded quality evaluations
- `llm-python`: earlier workshop backend retained as reference; it is not deployed by this lab

## Local Docker run

1. Copy `.env.example` to `.env` and set `OLLAMA_API_KEY`.
2. Run `docker compose up --build -d`.
3. Open the frontend at <http://localhost:5000> and the API docs at
   <http://localhost:8080/swagger-ui.html>.
4. Stop the stack with `docker compose down`.

If either host port is occupied, override it without changing the container
network, for example `FRONTEND_HOST_PORT=5001 docker compose up -d`.

## CI/CD

GitHub Actions lint and test the code, run Promptfoo and DeepEval, scan both
container images with Trivy, and publish multi-architecture images to Docker
Hub. Configure these repository settings before the first push:

- Variable: `DOCKERHUB_USERNAME`
- Secrets: `DOCKERHUB_TOKEN`, `OLLAMA_API_KEY`, `OLLAMA_BASE_URL`, `OPENAI_API_KEY`

Published image tags include `main`, `latest`, and `sha-<commit>` for both
`llm-multiroute` and `llm-frontend-python`.

## Minikube

The Kubernetes manifests use the public `keiyam/*:main` images. Create the
backend secret locally before applying the backend manifest:

```sh
kubectl --context minikube create namespace llm-multiroute-backend --dry-run=client -o yaml | kubectl --context minikube apply -f -
kubectl --context minikube -n llm-multiroute-backend create secret generic llm-multiroute-secret --from-literal=OLLAMA_API_KEY="$OLLAMA_API_KEY" --dry-run=client -o yaml | kubectl --context minikube apply -f -
kubectl --context minikube apply -f llm-multiroute/k8s/deployment.yaml
kubectl --context minikube apply -f llm-frontend-python/k8s/deployment.yaml
```

Every command names the `minikube` context explicitly so another configured
cluster cannot be modified accidentally.
