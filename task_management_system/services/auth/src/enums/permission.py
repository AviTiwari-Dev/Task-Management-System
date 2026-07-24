"""Permission enum."""

from enum import StrEnum


class Permission(StrEnum):
    """System permissions."""

    USER_READ = "user.read"

    TASK_CREATE = "task.create"
    TASK_READ = "task.read"
    TASK_UPDATE = "task.update"
    TASK_DELETE = "task.delete"

    TASK_READ_ALL = "task.read.all"
