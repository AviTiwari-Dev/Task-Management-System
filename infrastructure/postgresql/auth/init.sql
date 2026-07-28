CREATE SCHEMA IF NOT EXISTS auth_sch;

CREATE EXTENSION IF NOT EXISTS pgcrypto;

-- ==========================================================
-- ENUMS
-- ==========================================================

CREATE TYPE auth_sch.role_enum AS ENUM
(
    'ADMIN',
    'USER'
);

-- ==========================================================
-- ROLES
-- ==========================================================

CREATE TABLE auth_sch.roles
(
    role_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),

    role_name auth_sch.role_enum NOT NULL UNIQUE,

    description VARCHAR(255),

    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),

    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

INSERT INTO auth_sch.roles
(
    role_name,
    description
)
VALUES
(
    'ADMIN',
    'System Administrator'
),
(
    'USER',
    'Regular User'
);

-- ==========================================================
-- USERS
-- ==========================================================

CREATE TABLE auth_sch.users
(
    user_id UUID PRIMARY KEY,

    first_name VARCHAR(50) NOT NULL,

    middle_name VARCHAR(50),

    last_name VARCHAR(50) NOT NULL,

    username VARCHAR(100) NOT NULL UNIQUE,

    password_hash VARCHAR(255) NOT NULL,

    is_active BOOLEAN NOT NULL DEFAULT TRUE,

    role_id UUID NOT NULL
        REFERENCES auth_sch.roles(role_id),

    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),

    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

INSERT INTO auth_sch.users
(
    user_id,
    first_name,
    middle_name,
    last_name,
    username,
    password_hash,
    is_active,
    role_id
)
VALUES
(
    '11111111-1111-1111-1111-111111111111',
    'System',
    NULL,
    'Administrator',
    'admin',
    '$argon2id$v=19$m=65536,t=3,p=4$3YskP/FY6y8DkDx5QlcVsg$X5CIUnV0dJ82w3eHpwBzReNZ4gJNDDH9Joc2Acm7+cM',
    TRUE,
    (
        SELECT role_id
        FROM auth_sch.roles
        WHERE role_name = 'ADMIN'
    )
),
(
    '22222222-2222-2222-2222-222222222222',
    'John',
    NULL,
    'Doe',
    'john',
    '$argon2id$v=19$m=65536,t=3,p=4$3YskP/FY6y8DkDx5QlcVsg$X5CIUnV0dJ82w3eHpwBzReNZ4gJNDDH9Joc2Acm7+cM',
    TRUE,
    (
        SELECT role_id
        FROM auth_sch.roles
        WHERE role_name = 'USER'
    )
);