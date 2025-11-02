from flask import Flask, render_template, request, redirect, url_for
from db import getTaskList, addTask, updateTask, deleteTask, completeTask

tasklist = getTaskList()

app = Flask(__name__)

@app.route('/')
def home():
    tasklist = getTaskList()
    return render_template("./tasklist.html", tasklist = tasklist)

@app.post('/add')
def add():
    n: str = request.form['taskName']
    d: str = request.form['dueDate']
    addTask(name=n, date=d)
    return redirect(url_for('home'))

@app.post('/update')
def update():
    id: int = request.form['id']
    n: str = request.form['updateTask']
    d: str = request.form['updateDate']
    b = request.form['saveOrDeleteOrComplete']
    if b == "X":
        deleteTask(id=id)
    elif b == "update":
        updateTask(id=id, updateTask=n, updateDate=d)
    elif b == "complete":
        completeTask(id=id)
    return redirect(url_for('home'))

app.run(debug=True)