# Task Management System

A production-ready **Task Management System** built using **Python**, **FastAPI**, **SQLAlchemy 2.0 (Async)**, and **PostgreSQL** following **Clean Architecture** and **Microservices** principles.

The project consists of independent microservices communicating through JWT authentication with a shared authentication library.

---

## Features

### Authentication Service

- User Registration
- User Login
- JWT Access Token Generation
- Current User Endpoint
- Password Hashing (Argon2)
- Role-Based Access Control (RBAC)

### Task Service

- Create Tasks
- List Tasks
- Get Task by ID
- Update Tasks
- Delete Tasks
- User-specific Task Access
- JWT Authentication

### Shared Authentication Library

- JWT Verification
- Current User Model
- Reusable Authentication Utilities

---

# Architecture

```
task_management_system/
│
├── services/
│   ├── auth/
│   └── task/
│
└── shared/
    └── auth/
```

---

# Technology Stack

- Python 3.14
- FastAPI
- SQLAlchemy 2.0 Async ORM
- PostgreSQL
- AsyncPG
- Pydantic v2
- JWT Authentication
- Argon2 Password Hashing
- Uvicorn

---

# Project Structure

```
task_management_system/

├── services/
│
│   ├── auth/
│   │
│   └── task/
│
└── shared/
    └── auth/
```

---

# Auth Service Structure

```
services/auth/src/

├── bases/
├── configurations/
├── dependencies/
├── endpoints/
├── engines/
├── enums/
├── exceptions/
├── models/
│   ├── data_storage/
│   └── data_validation/
├── operations/
│   ├── repositories/
│   └── managers/
├── routers/
├── session_factories/
├── utilities/
└── main.py
```

---

# Task Service Structure

```
services/task/src/

├── background_tasks/
├── bases/
├── configurations/
├── dependencies/
├── endpoints/
├── engines/
├── enums/
├── exceptions/
├── models/
│   ├── data_storage/
│   └── data_validation/
├── operations/
│   ├── repositories/
│   └── managers/
├── routers/
├── session_factories/
├── utilities/
└── main.py
```

---

# Shared Authentication Library

```
shared/auth/src/

├── models/
│   └── current_user.py
│
└── utilities/
    └── jwt.py
```

---

# Authentication Flow

```
User
 │
 │ Login
 ▼
Auth Service
 │
 │ Verify Credentials
 │
 ▼
Generate JWT
 │
 ▼
Client
 │
 │ Authorization: Bearer <token>
 ▼
Task Service
 │
 ▼
Verify JWT
 │
 ▼
Extract Current User
 │
 ▼
Perform CRUD Operations
```

---

# Database Schema

## Authentication Database

### users

| Column | Type |
|---------|------|
| user_id | UUID |
| username | VARCHAR |
| password | VARCHAR |
| role_id | UUID |
| is_active | BOOLEAN |
| created_at | TIMESTAMP |
| updated_at | TIMESTAMP |

---

### roles

| Column | Type |
|---------|------|
| role_id | UUID |
| role_name | ENUM |

---

### permissions

| Column | Type |
|---------|------|
| permission_id | UUID |
| permission_name | ENUM |

---

### role_permissions

| Column | Type |
|---------|------|
| role_id | UUID |
| permission_id | UUID |

---

## Task Database

### tasks

| Column | Type |
|---------|------|
| task_id | UUID |
| title | VARCHAR |
| description | TEXT |
| status | ENUM |
| priority | ENUM |
| due_date | DATE |
| user_id | UUID |
| created_at | TIMESTAMP |
| updated_at | TIMESTAMP |

---

# Role-Based Access Control

## Roles

- ADMIN
- USER

---

## Permissions

- task.create
- task.read
- task.update
- task.delete
- task.read.all
- user.read

---

# REST APIs

## Authentication

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | `/api/v1/auth/register` | Register User |
| POST | `/api/v1/auth/login` | Login User |
| GET | `/api/v1/auth/me` | Current User |

---

## Tasks

| Method | Endpoint |
|---------|----------|
| POST | `/api/v1/tasks` |
| GET | `/api/v1/tasks` |
| GET | `/api/v1/tasks/{task_id}` |
| PATCH | `/api/v1/tasks/{task_id}` |
| DELETE | `/api/v1/tasks/{task_id}` |

---

# JWT Payload

```json
{
  "sub": "user_id",
  "username": "john",
  "role": "ADMIN",
  "iss": "auth-service",
  "aud": "my-api",
  "iat": 1234567890,
  "exp": 1234569999
}
```

---

# Environment Variables

## Auth Service

```
URL=
PASSWORD_PEPPER=

JWT_SECRET_KEY=
JWT_ALGORITHM=HS256
JWT_ISSUER=
JWT_AUDIENCE=

ACCESS_TOKEN_EXPIRE_MINUTES=
```

---

## Task Service

```
URL=

JWT_SECRET_KEY=
JWT_ALGORITHM=HS256
JWT_ISSUER=
JWT_AUDIENCE=
```

---

# Running the Project

## Clone Repository

```bash
git clone https://github.com/AviTiwari-Dev/Task-Management-System

cd task_management_system
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Start Authentication Service

```bash
uvicorn task_management_system.services.auth.src.main:auth_api --reload --port 8001
```

---

## Start Task Service

```bash
uvicorn task_management_system.services.task.src.main:app --reload --port 8002
```

---

# API Documentation

Auth Service

```
http://localhost:8001/documentaion/Swagger
```

Task Service

```
http://localhost:8002/docs
```

---

# Clean Architecture

The project follows the Repository–Manager pattern.

```
API
 │
 ▼
Manager
 │
 ▼
Repository
 │
 ▼
Database
```

### Responsibilities

- **Endpoints** – Handle HTTP requests and responses.
- **Managers** – Implement business logic.
- **Repositories** – Perform database operations.
- **Models** – Define database schema and validation models.
- **Utilities** – Provide reusable helper functions.
- **Dependencies** – Manage authentication and dependency injection.

---

# Security

- JWT Bearer Authentication
- Argon2 Password Hashing
- Role-Based Authorization
- User-specific Resource Access
- Async Database Sessions
- Pydantic Input Validation

---

# Future Enhancements

- Refresh Tokens
- Logout
- Logout from All Devices
- Refresh Token Rotation
- Redis Session Management
- Alembic Database Migrations
- CI/CD Pipeline
- Unit Tests
- Integration Tests
- API Gateway
- Complete Role Based and Permission Based System
- Distributed Logging
- Monitoring and Metrics

---