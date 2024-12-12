from typing import List

import attr

@attr.s
class Task:
    action: str = attr.ib()
    params: List[str] = attr.ib(default=[])

    
TASKS = []

NO_TASK = Task(action='None')



def get_tasks() -> List[Task]:
    return TASKS


def pop_next_task() -> Task:
    if TASKS:
        task = TASKS.pop(0)
        return task
    else:
        return NO_TASK


def add_task(task: Task) -> None:
    TASKS.append(task)
