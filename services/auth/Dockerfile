FROM python:3.14-slim-bookworm AS builder

WORKDIR /app

RUN apt-get update && \
    apt-get install -y build-essential

COPY services/auth/requirements ./requirements

RUN pip install --prefix=/install \
    -r requirements/base.txt \
    -r requirements/prod.txt

FROM python:3.14-slim-bookworm

WORKDIR /app

ENV PYTHONPATH=/app

COPY --from=builder /install /usr/local

COPY services/auth ./services/auth
COPY shared/ ./shared
COPY infrastructure ./infrastructure

CMD ["uvicorn", "services.auth.src.main:auth_api", "--host", "0.0.0.0", "--port", "8001"]
