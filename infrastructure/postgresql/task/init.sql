CREATE SCHEMA IF NOT EXISTS task_sch;

CREATE EXTENSION IF NOT EXISTS pgcrypto;

CREATE TYPE task_sch.task_status_enum AS ENUM
(
    'PENDING',
    'IN_PROGRESS',
    'COMPLETED',
    'CANCELLED'
);

CREATE TYPE task_sch.task_priority_enum AS ENUM
(
    'LOW',
    'MEDIUM',
    'HIGH'
);

CREATE TABLE task_sch.tasks
(
    task_id UUID PRIMARY KEY,

    title VARCHAR(200) NOT NULL,

    description TEXT,

    status task_sch.task_status_enum NOT NULL,

    priority task_sch.task_priority_enum NOT NULL,

    due_date TIMESTAMPTZ NOT NULL,

    user_id UUID NOT NULL,

    created_at TIMESTAMPTZ DEFAULT now(),

    updated_at TIMESTAMPTZ DEFAULT now()
);

INSERT INTO task_sch.tasks
VALUES
(
    gen_random_uuid(),
    'Prepare project report',
    'Monthly report',
    'PENDING',
    'LOW',
    now() + interval '7 day',
    '22222222-2222-2222-2222-222222222222',
    now(),
    now()
),

(
    gen_random_uuid(),
    'Fix login bug',
    'Critical production issue',
    'IN_PROGRESS',
    'HIGH',
    now() + interval '2 day',
    '22222222-2222-2222-2222-222222222222',
    now(),
    now()
),

(
    gen_random_uuid(),
    'Deploy release',
    'Deploy version 1.0',
    'COMPLETED',
    'MEDIUM',
    now(),
    '11111111-1111-1111-1111-111111111111',
    now(),
    now()
),

(
    gen_random_uuid(),
    'Database backup',
    'Nightly backup verification',
    'PENDING',
    'HIGH',
    now() + interval '1 day',
    '11111111-1111-1111-1111-111111111111',
    now(),
    now()
),

(
    gen_random_uuid(),
    'Refactor API',
    'Improve service architecture',
    'IN_PROGRESS',
    'MEDIUM',
    now() + interval '5 day',
    '22222222-2222-2222-2222-222222222222',
    now(),
    now()
);