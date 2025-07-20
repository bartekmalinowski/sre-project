from flask import Flask, jsonify, request
from . import logic

app = Flask(__name__)


@app.route("/")
def home():
    return "Welcome to TaskMaster API!"


@app.route("/tasks", methods=["GET"])
def get_tasks():
    all_tasks = logic.get_all_tasks()
    return jsonify(all_tasks)


@app.route("/tasks", methods=["POST"])
def add_task():
    if not request.json or "title" not in request.json:
        return jsonify({"error": "Missing title"}), 400

    title = request.json["title"]
    new_task = logic.add_new_task(title)
    return jsonify(new_task), 201
