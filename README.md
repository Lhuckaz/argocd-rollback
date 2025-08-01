# argocd-rollback

A minimal ArgoCD + Helm demo that uses `$ARGOCD_APP_REVISION` to ensure safe and accurate rollbacks.

## How it works

- Docker images are tagged with the Git commit SHA.
- Helm chart uses the SHA as the image tag.
- ArgoCD uses `$ARGOCD_APP_REVISION` to keep track of the correct version for rollback.

## Deployment

1. Add your DockerHub credentials to GitHub Actions secrets:
   - `DOCKERHUB_USERNAME`
   - `DOCKERHUB_TOKEN`

2. Push to main. GitHub Actions will:
   - Build the Docker image
   - Tag with SHA
   - Push to Docker Hub

3. ArgoCD deploys it automatically using the SHA tag.
