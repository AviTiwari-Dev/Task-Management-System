"""
Task status enum
"""

from enum import StrEnum


class TaskStatus(StrEnum):
    """
    Represents the lifecycle stages of a system or user task.
    """

    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    CANCELLED = "cancelled"
