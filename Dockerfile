FROM python:3.11-slim
WORKDIR /app
COPY app /app
RUN pip install flask
ENV FLASK_APP=main.py
CMD ["flask", "run", "--host=0.0.0.0", "--port=8080"]