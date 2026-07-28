FROM python:3.14.5-slim-bookworm

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app

RUN apt-get update \
 && apt-get install -y build-essential \
 && rm -rf /var/lib/apt/lists/*

COPY . .

RUN pip install --no-cache-dir \
    -r services/auth/requirements/base.txt \
    -r services/auth/requirements/prod.txt

CMD [
    "uvicorn",
    "services.auth.src.main:auth_api",
    "--host",
    "0.0.0.0",
    "--port",
    "8001"
]