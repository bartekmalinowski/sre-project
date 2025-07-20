tasks = {
    1: {"id": 1, "title": "Setup CI/CD Pipeline", "completed": True},
    2: {"id": 2, "title": "Write unit tests", "completed": True},
}
next_id = 3


def get_all_tasks():
    return list(tasks.values())


def add_new_task(title):
    global next_id
    new_task = {"id": next_id, "title": title, "completed": False}
    tasks[next_id] = new_task
    next_id += 1
    return new_task
