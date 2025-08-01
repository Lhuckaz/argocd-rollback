from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from GitOps App! Argo CD Rollback - 1.0.1"