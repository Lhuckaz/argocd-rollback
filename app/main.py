from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from GitOps App! Argo CD Rollback - 1.0.5"

@app.route("/actuator/health")
def health():
    return { "status": "UP" }