from flask import Flask, render_template

app = Flask(__name__)

tasklist = [["Walk Dog", False], ["Wash Dishes", True], ["Take out trash", True]]

@app.route('/')
def home():
    return render_template("./tasklist.html", tasklist = tasklist)

app.run()