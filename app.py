from flask import Flask, render_template, redirect, url_for, request
from flask_scss import Scss
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app = Flask(__name__)
Scss(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


class MyTask(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    complete = db.Column(db.Boolean, default=False) 
    created = db.Column(db.DateTime, default=datetime.utcnow)



    def __repr__(self) -> str:
        return f"<Task {self.id}>"

with app.app_context():
    db.create_all()


@app.route("/",methods=["GET","POST"])
def index():

    if request.method == "POST":
        task_content = request.form["content"]
        new_task = MyTask(content=task_content)

        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect("/")
        except:
            return "There was an issue adding your task"

    else:
        tasks = MyTask.query.order_by(MyTask.created).all()
        return render_template("index.html", tasks=tasks)


@app.route("/delete/<int:id>")
def delete(id:int):

    delete_task = MyTask.query.get_or_404(id)
    try:
        db.session.delete(delete_task)
        db.session.commit()
        return redirect("/")
    except:
        return "There was a problem deleting that task"




    return render_template("index.html")



 
@app.route("/update/<int:id>", methods=["GET","POST"])
def update(id:int):
    task = MyTask.query.get_or_404(id)

    if request.method == "POST":
        task.content = request.form["content"]
        try:
            db.session.commit()
            return redirect("/")
        except:
            return "There was an issue updating your task"
    else:
        return render_template("update.html", task=task)

 

if __name__ == "__main__":
    
    app.run(debug=True)

#if __name__ in "__main__":
    #with app.app_context():
     #   db.create_all()
    #app.run(debug=True)