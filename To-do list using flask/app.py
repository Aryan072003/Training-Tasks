from flask import Flask, render_template, request, redirect, url_for
from json import dumps, loads

app = Flask(__name__)

@app.route('/')
def home():
    f_read = open("task.json", "r")
    tasks = loads(f_read.read())
    return render_template("index.html", todo=tasks)

@app.route('/add', methods=["POST"])
def add_task():
    f_read = open("task.json", "r")
    tasks = loads(f_read.read())
    task = request.form.get("task")
    if request.method == "POST":
        if task != "":
            tasks.append({"id": len(tasks) + 1, "task": task, "checked": False})
            with open("task.json", "w") as f_write:
                f_write.write(dumps(tasks, indent=4))
                f_write.close()
    return redirect(url_for("home"))

@app.route('/complete/<task_id>', methods=["POST"])
def check(task_id):
    f_read = open("task.json", "r")
    tasks = loads(f_read.read())
    if request.method == "POST":
        for todo in tasks:
            if todo.id == task_id:
                todo.checked = not todo.checked
                break
        with open("task.json", "w") as f_write:
            f_write.write(dumps(tasks, indent=4))
            f_write.close()
    return redirect(url_for("home"))

if __name__ == '__main__':
    app.run(debug=True)
