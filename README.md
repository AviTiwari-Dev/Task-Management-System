# Task Management System

A containerized microservices-based Task Management System built with **FastAPI**, **PostgreSQL**, **Docker Compose**, and **JWT Authentication**.

## Architecture

```
task_management_system/
│
├── docker-compose.yml
│
├── services/
│   ├── auth/
│   │   ├── Dockerfile
│   │   ├── requirements/
│   │   └── src/
│   │
│   └── task/
│       ├── Dockerfile
│       ├── requirements/
│       └── src/
│
└── shared/
    └── auth/
```

The project consists of two independent services.

| Service | Port | Description |
|----------|------|-------------|
| Auth Service | 8001 | User authentication and JWT generation |
| Task Service | 8000 | Task CRUD operations |

Each service has its own PostgreSQL database.

---

# Features

- FastAPI
- SQLAlchemy 2.0 (Async)
- PostgreSQL
- Docker Compose
- JWT Authentication
- Role Based Authorization
- Pagination
- Filtering
- Pydantic v2
- Clean Architecture
- Async Database Access

---

# Prerequisites

Install the following before starting the project.

- Docker Desktop
- Docker Compose (included with Docker Desktop)
- Git

Verify installation

```bash
docker --version
docker compose version
git --version
```

---

# Project Structure

```
task_management_system/

docker-compose.yml

services/
│
├── auth/
│   ├── Dockerfile
│   ├── .env
│   └── src/
│
├── task/
│   ├── Dockerfile
│   ├── .env
│   └── src/
│
shared/
```

---

# Environment Configuration

Each service maintains its own environment variables.

## Auth Service

Create

```
services/auth/.env
```

Example

```env
APP_NAME=Auth Service

DATABASE_URL=postgresql+asyncpg://postgres:postgres@auth-postgres:5432/auth_db

SECRET_KEY=change_me

ACCESS_TOKEN_EXPIRE_MINUTES=30

REFRESH_TOKEN_EXPIRE_DAYS=7
```

---

## Task Service

Create

```
services/task/.env
```

Example

```env
APP_NAME=Task Service

DATABASE_URL=postgresql+asyncpg://postgres:postgres@task-postgres:5432/task_db

AUTH_SERVICE_URL=http://auth-service:8001
```

---

# Docker Containers

The application starts four containers.

| Container | Description | Port |
|------------|-------------|------|
| auth-service | Authentication API | 8001 |
| task-service | Task API | 8000 |
| auth-postgres | Authentication Database | 5433 (host) → 5432 (container) |
| task-postgres | Task Database | 5432 (host) → 5432 (container) |

---

# Starting the Project

## Build containers

```bash
docker compose build
```

---

## Start services

```bash
docker compose up
```

Run in detached mode

```bash
docker compose up -d
```

---

## Rebuild after code changes

```bash
docker compose up --build
```

---

## Stop containers

```bash
docker compose down
```

---

## Remove containers and volumes

This removes all PostgreSQL data.

```bash
docker compose down -v
```

---

## View logs

All services

```bash
docker compose logs
```

Task Service

```bash
docker compose logs task-service
```

Auth Service

```bash
docker compose logs auth-service
```

Follow logs

```bash
docker compose logs -f
```

---

# API Documentation

After the containers are running:

Task Service

```
http://localhost:8000/docs
```

Authentication Service

```
http://localhost:8001/documentation/Swagger
```

---

# Database

Each service owns its own PostgreSQL database.

| Service | Database |
|----------|----------|
| Auth | auth_db |
| Task | task_db |

No database tables are shared between services.

---

# Common Docker Commands

Restart services

```bash
docker compose restart
```

Restart a single service

```bash
docker compose restart task-service
```

View running containers

```bash
docker ps
```

Open a shell inside Task Service

```bash
docker exec -it task-service bash
```

Open PostgreSQL

```bash
docker exec -it task-postgres psql -U postgres
```

---

# Running Tests

Inside a service container

```bash
pytest
```

or

```bash
docker exec -it task-service pytest
```

---

# Troubleshooting

## Container won't start

Rebuild images

```bash
docker compose down

docker compose up --build
```

---

## Database schema changed

Remove existing volumes

```bash
docker compose down -v
docker compose up --build
```

---

## Port already in use

Check running processes

```bash
docker ps
```

or stop the conflicting container.

---

## View logs

```bash
docker compose logs -f
```

---

# Technology Stack

- Python 3.14
- FastAPI
- SQLAlchemy 2.0
- PostgreSQL
- Pydantic v2
- Docker
- Docker Compose
- Alembic
- Uvicorn

---

# Development Workflow

```text
Clone Repository
        │
        ▼
Create .env Files
        │
        ▼
docker compose build
        │
        ▼
docker compose up
        │
        ▼
Run Alembic Migrations
        │
        ▼
Open Swagger UI
        │
        ▼
Begin Development
```

---

# Service URLs

| Service | URL |
|----------|-----|
| Task API | http://localhost:8000 |
| Task Swagger | http://localhost:8000/docs |
| Auth API | http://localhost:8001 |
| Auth Swagger | http://localhost:8001/documentation/Swagger |

---

# License

This project is provided for assessment and educational purposes.