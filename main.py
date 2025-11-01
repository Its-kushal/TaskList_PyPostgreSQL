from flask import Flask, render_template, request, redirect, url_for
from db import getTaskList, addTask

tasklist = getTaskList()

app = Flask(__name__)



@app.route('/')
def home():
    # tasklist = [["Walk Dog", False], ["Wash Dishes", True], ["Take out trash", True]]
    tasklist = getTaskList()
    return render_template("./tasklist.html", tasklist = tasklist)

@app.post('/add')
def add():
    n: str = request.form['taskName']
    d: str = request.form['dueDate']
    addTask(name=n, date=d)
    return redirect(url_for('home'))




app.run()