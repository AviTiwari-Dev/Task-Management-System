FROM python:3.14.5-slim-bookworm AS base

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update \
    && apt-get install -y build-essential \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY ./src ./src

COPY ./requirements/base.txt ./requirements/base.txt
RUN pip install --no-cache-dir -r ./requirements/base.txt

# Test image
FROM base AS test

COPY ./tests ./tests

COPY ./requirements/test.txt ./requirements/test.txt
RUN pip install --no-cache-dir ./requirements/test.txt

# Production image
FROM base AS prod

COPY ./requirements/prod.txt ./requirements./prod.txt
RUN pip install --no-cache-dir -r ./requirements/prod.txt

RUN useradd -m appuser \
    && chown -R appuser:appuser /app
USER appuser

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8080"]
