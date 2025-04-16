from flask import Flask, render_template,redirect, url_for, request

app = Flask(__name__)
# initializing the empty to do list.
TODO_LIST = []  
@app.route("/")
def home():
    return render_template("index.html", todo_list=TODO_LIST) 

@app.route("/add", methods=["POST"])
def add_task():
    task = request.form.get("task")
    if task:
        TODO_LIST.append(task)
    return redirect(url_for("home"))    



#Deleting the task

@app.route("/delete/<int:task_id>")
def delete_task(task_id):
   if 0 <= task_id < len(TODO_LIST):
       TODO_LIST.pop(task_id)
   return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)  # Set debug=True for development purposes only.