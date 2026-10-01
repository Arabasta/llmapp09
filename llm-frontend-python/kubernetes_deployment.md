# Frontend deployment on Minikube

The manifest creates the `llm-frontend` namespace, Deployment, ClusterIP
Service, and a ConfigMap pointing at the backend Service in its separate
namespace.

```sh
kubectl --context minikube apply -f llm-frontend-python/k8s/deployment.yaml
kubectl --context minikube -n llm-frontend rollout status deployment/llm-frontend-app
kubectl --context minikube -n llm-frontend port-forward service/llm-frontend-service 5000:5000
```
