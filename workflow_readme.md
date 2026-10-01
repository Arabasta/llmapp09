# GitHub Actions workflows

- `llm-multiroute-ci.yml`: Ruff, backend unit tests, Docker build, Trivy scan,
  and multi-architecture publish.
- `llm-frontend-python-ci.yml`: Ruff, Docker build, Trivy scan, and
  multi-architecture publish.
- `promptfoo-tests-ci.yml`: starts the backend and runs all Promptfoo suites.
- `deepeval-tests-ci.yml`: starts the backend and runs all model-graded
  DeepEval suites.

Required repository variable: `DOCKERHUB_USERNAME`.

Required repository secrets: `DOCKERHUB_TOKEN`, `OLLAMA_API_KEY`,
`OLLAMA_BASE_URL`, and `OPENAI_API_KEY`.

High and Critical Trivy findings fail image publication. The repository does
not include blanket vulnerability suppressions.
