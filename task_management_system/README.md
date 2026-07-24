# **Task Management System**

## **Microservices**

### **Auth Microservice**

#### **Database Structure**

    auth_db
    └── auth_sch
        ├── users
        │   ├── user_id (UUID, PK)
        │   ├── first_name
        │   ├── middle_name
        │   ├── last_name
        │   ├── username (Unique)
        │   ├── password_hash
        │   ├── role_id (FK -> roles.role_id)
        │   ├── is_active
        │   ├── created_at
        │   └── updated_at
        │
        ├── roles
        │   ├── role_id (UUID, PK)
        │   ├── role_name (Unique)
        │   ├── description
        │   ├── created_at
        │   └── updated_at
        │
        ├── permissions
        │   ├── permission_id (UUID, PK)
        │   ├── permission_name (Unique)
        │   ├── description
        │   ├── created_at
        │   └── updated_at
        │
        └── role_permissions
            ├── role_id (FK -> roles.role_id)
            └── permission_id (FK -> permissions.permission_id)

#### **Models**

    data_validation/
    ├── auth.py
    ├── token.py
    └── user.py

#### **Endpoints**

    POST   /register        → register user
    POST   /login           → login user
    GET    /me              → get logedin user details


### **Task Microservice**

#### **Database Structure**

    task_db
    └── task_sch
        └── tasks
            ├── task_id (UUID, PK)
            ├── title
            ├── description
            ├── status
            ├── priority
            ├── due_date
            ├── user_id (UUID)
            ├── created_at
            └── updated_at

#### **Models**

    data_validation/
    ├── task.py
    ├── task_create.py
    ├── task_update.py
    ├── task_response.py
    └── task_filter.py

#### **Endpoints**

    POST   /tasks        → create task
    GET    /tasks        → list tasks (filter + pagination)
    GET    /tasks/{id}   → get single task
    PUT    /tasks/{id}   → update
    DELETE /tasks/{id}   → delete
