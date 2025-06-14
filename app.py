from flask import Flask, render_template, request, redirect, url_for
import uuid

app = Flask(__name__)
tasks = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        task_text = request.form.get("task")
        if task_text:
            tasks.append({"id": str(uuid.uuid4()), "text": task_text})
        return redirect(url_for("index"))
    return render_template("index.html", tasks=tasks)

@app.route("/delete/<task_id>", methods=["POST"])
def delete(task_id):
    global tasks
    tasks = [task for task in tasks if task["id"] != task_id]
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
