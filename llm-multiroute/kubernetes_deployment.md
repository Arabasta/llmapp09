# Backend deployment on Minikube

The manifest creates the `llm-multiroute-backend` namespace, Deployment,
ClusterIP Service, and non-secret model configuration. Create the API key
Secret separately so credentials never enter source control.

```sh
kubectl --context minikube create namespace llm-multiroute-backend --dry-run=client -o yaml | kubectl --context minikube apply -f -
kubectl --context minikube -n llm-multiroute-backend create secret generic llm-multiroute-secret --from-literal=OLLAMA_API_KEY="$OLLAMA_API_KEY" --dry-run=client -o yaml | kubectl --context minikube apply -f -
kubectl --context minikube apply -f llm-multiroute/k8s/deployment.yaml
kubectl --context minikube -n llm-multiroute-backend rollout status deployment/llm-multiroute-app
```
