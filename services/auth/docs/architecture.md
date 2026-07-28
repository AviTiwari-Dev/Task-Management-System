


## **Database Structure**

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
