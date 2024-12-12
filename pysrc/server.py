from flask import Flask, jsonify

import attr

import task_manager

app = Flask(__name__)

@app.route("/")
def homepage():
  return "Task Server"


@app.route("/get_tasks")
def get_tasks():
    tasks = task_manager.get_tasks()
    return jsonify([attr.asdict(t) for t in tasks])


@app.route("/pop_next_task")
def pop_next_task():
    t = task_manager.pop_next_task()
    return jsonify(attr.asdict(t))


if __name__ == "__main__":
    task_manager.add_task(task_manager.Task(action="test1"))
    task_manager.add_task(task_manager.Task(action="test2", params=["a","b"]))
    app.run()