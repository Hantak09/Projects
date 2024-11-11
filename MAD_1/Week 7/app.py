from flask import Flask, render_template_string
from flask import request
from flask import url_for
from flask import redirect
from flask import render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///week7_database.sqlite3"
db = SQLAlchemy(app)

"""Models"""
class Student(db.Model):
    __tablename__ = "student"
    student_id = db.Column(db.Integer,autoincrement=True, primary_key=True)
    roll_number = db.Column(db.String, unique=True, nullable=False)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String)

class Course(db.Model):
    __tablename__ = "course"
    course_id = db.Column(db.Integer,autoincrement=True, primary_key=True)
    course_code = db.Column(db.String, unique=True, nullable=False)
    course_name = db.Column(db.String, nullable=False)
    course_description = db.Column(db.String)

class Enrollment(db.Model):
    __tablename__ = "enrollment"
    enrollment_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    ecourse_id = db.Column(db.Integer, db.ForeignKey("course.course_id"), nullable=False)
    estudent_id = db.Column(db.Integer, db.ForeignKey("student.student_id"), nullable=False)

@app.route('/')
def index():
    students = Student.query.all()
    if len(students) == 0:
        return render_template("index-empty.html")
    return render_template("index.html", students=students)

@app.route('/student/create', methods=['GET', 'POST'])
def student_add():
    if request.method == "GET":
        return render_template("student-add.html")
    if request.method == "POST":
        roll_number = request.form["roll"]
        first_name = request.form["f_name"]
        last_name = request.form["l_name"]

        student = Student.query.filter(Student.roll_number == roll_number).first()
        if student:
            return render_template("student-exist.html")
        else:
            student = Student(roll_number=roll_number, first_name=first_name, last_name=last_name)
            db.session.add(student)
            db.session.commit()
            return redirect(url_for("index"))

@app.route("/student/<int:student_id>/update", methods=["GET", "POST"])
def student_update(student_id):
    return render_template_string("Student Update Page")

@app.route('/student/<int:student_id>/delete', methods=["GET", "POST"])
def student_delete(student_id):
    return render_template_string("Student Delete Page")

@app.route("/student/<int:student_id>")
def student_show(student_id):
    return render_template_string("Student Show Page")




if __name__ == '__main__':
    app.run(debug=True)