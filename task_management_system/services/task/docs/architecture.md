# **Task Microservice**

## **Database Structure**

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
            ├── updated_at

## **Models**

    data_validation/
    ├── task.py
    ├── task_create.py
    ├── task_update.py
    ├── task_response.py
    └── task_filter.py

## **Endpoints**

    POST   /tasks        → create task
    GET    /tasks        → list tasks (filter + pagination)
    GET    /tasks/{id}   → get single task
    PUT    /tasks/{id}   → update
    DELETE /tasks/{id}   → delete

