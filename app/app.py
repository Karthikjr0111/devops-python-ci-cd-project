from flask import Flask, jsonify

app = Flask(__name__)

tasks = [
    {"id": 1, "task": "Learn DevOps"},
    {"id": 2, "task": "Build CI/CD Pipeline"}
]

@app.route("/")
def home():
    return "DevOps Python App Running"

@app.route("/tasks")
def get_tasks():
    return jsonify(tasks)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)