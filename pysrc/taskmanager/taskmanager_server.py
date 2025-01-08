from flask import Flask, jsonify
import json

import attr

import taskmanager

app = Flask(__name__)

@app.route("/")
def homepage():
  return "Task Server"


@app.route("/get_tasks")
def get_tasks():
    tasks = taskmanager.get_tasks()
    return jsonify([attr.asdict(t) for t in tasks])


@app.route("/pop_next_task")
def pop_next_task():
    t = taskmanager.pop_next_task()
    return jsonify(attr.asdict(t))


@app.route("/add_task")
def add_task(task_json):
    taskmanager.add_task(json.loads(task_json))



if __name__ == "__main__":
    taskmanager.add_task(taskmanager.Task({'action': "test1"}))
    taskmanager.add_task(taskmanager.Task({'action': "test2", 'params': ["a","b"]}))
    app.run()