from flask import Flask, render_template, request
from tinydb import TinyDB, Query

db = TinyDB("./db.json")
app = Flask(__name__)


@app.route('/todo', methods=["GET","POST"])
def hello():
    todo = request.form.get('todo')
    print(todo)
    myData = db.all()
    if todo:
        db.insert({"Todo": todo})
    return render_template("index.html", todos = myData)
    
if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
