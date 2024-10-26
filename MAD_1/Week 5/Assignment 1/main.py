import os
from flask import Flask
from flask import request
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
path = os.path.abspath(os.path.dirname(__file__))


app = Flask(__name__, template_folder='./templates')
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + os.path.join(path, 'database.sqlite3')
db = SQLAlchemy(app)
# db.init_app(app)
app.app_context().push()

class Student(db.Model):
    __tablename__ = 'student'
    student_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    roll_number = db.Column(db.String, unique=True, nullable=False)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String)

class Course(db.Model):
    # __tablename__ = 'course'
    course_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    course_code = db.Column(db.String, unique=True, nullable=False)
    course_name = db.Column(db.String, nullable=False)
    course_description = db.Column(db.String)

class Enrollments(db.Model):
    # __tablename__ = 'enrollments'
    enrollment_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    estudent_id = db.Column(db.Integer, db.ForeignKey('student.student_id'), nullable=False)
    ecourse = db.Column(db.Integer, db.ForeignKey('course.course_id'), nullable=False)

@app.route('/')
def index():
    students = Student.query.all()
    if len(students) == 0:
        return render_template("empty_index.html")

@app.route('/student/create', methods=['GET', 'POST'])
def add_student():
    return render_template("add_student.html")


if __name__=='__main__':
    app.run(debug=True)