from typing import List

import attr

@attr.s
class Task:
    id: int = attr.ib()
    request: str = attr.ib(default='')
    response: str = attr.ib(default='')

    
TASKS: List[Task] = []

NO_TASK = Task(id=-1)



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