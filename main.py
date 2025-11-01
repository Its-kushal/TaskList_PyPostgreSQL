from flask import Flask, render_template
from db import getTaskList

tasklist = getTaskList()

app = Flask(__name__)

# tasklist = [["Walk Dog", False], ["Wash Dishes", True], ["Take out trash", True]]
tasklist = getTaskList()

@app.route('/')
def home():
    return render_template("./tasklist.html", tasklist = tasklist)

app.run()