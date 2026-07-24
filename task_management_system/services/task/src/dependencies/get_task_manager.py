from ..operations.managers.task import TaskManager
from ..operations.repositories.task import TaskRepository

_task_repository = TaskRepository()
_task_manager = TaskManager(_task_repository)


def get_task_manager() -> TaskManager:
    """Return TaskManager."""

    return _task_manager
