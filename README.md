# argocd-rollback

A minimal ArgoCD + Helm demo that uses `$ARGOCD_APP_REVISION` to ensure safe and accurate rollbacks. Lets go.

## How it works

- Docker images are tagged with the Git commit SHA.
- Helm chart uses the SHA as the image tag.
- ArgoCD uses `$ARGOCD_APP_REVISION` to keep track of the correct version for rollback.

## 📦 Prerequisites

- Kubernetes cluster (e.g., minikube, k3d, KinD)
- `kubectl` and `argocd` CLI installed
- Docker Hub account
- Add your DockerHub credentials to GitHub Actions secrets
   - `DOCKERHUB_USERNAME`
   - `DOCKERHUB_TOKEN`
- Your repo structure:
  ```
  .
  ├── apps/
  │   └── argocd-rollback.yaml     # ArgoCD Application
  └── charts/
      └── argocd-rollback/         # Helm Chart
          └── envs/
              └── prod/
                  └── values.yaml  # Environment-specific values
  ```

---

## 🧱 Step 1: Install ArgoCD

```bash
kubectl create namespace argocd

kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
```

🔒 Port-forward to access the ArgoCD UI:

```bash
kubectl port-forward svc/argocd-server -n argocd 8080:443
```

---

## 🔐 Step 2: Log in to ArgoCD CLI

Get the admin password:

```bash
kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d; echo
```

Then log in:

```bash
argocd login localhost:8080 --username admin --password <copied-password> --insecure
```

---

## 🚀 Step 3: Add ArgoCD Application

Apply it:

```bash
kubectl apply -f apps/argocd-rollback.yaml
```

---

## 🔁 Done! You can now deploy and safely roll back versions with ArgoCD using Helm and GitOps.