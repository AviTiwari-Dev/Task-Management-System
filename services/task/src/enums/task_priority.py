"""
Task priority enum
"""

from enum import StrEnum


class TaskPriority(StrEnum):
    """
    Represents the priority of task
    """

    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"
