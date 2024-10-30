import os
from sqlalchemy import text
from flask import Flask, render_template_string, url_for
from flask import request
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
path = os.path.abspath(os.path.dirname(__file__))


app = Flask(__name__, template_folder='./templates', static_folder='./static')
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + os.path.join(path, 'database.sqlite3')
db = SQLAlchemy(app)
app.app_context().push()

class Student(db.Model):
    __tablename__ = 'student'
    student_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    roll_number = db.Column(db.String, unique=True, nullable=False)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String)

class Course(db.Model):
    __tablename__ = 'course'
    course_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    course_code = db.Column(db.String, unique=True, nullable=False)
    course_name = db.Column(db.String, nullable=False)
    course_description = db.Column(db.String)

class Enrollments(db.Model):
    __tablename__ = 'enrollments'
    enrollment_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    estudent_id = db.Column(db.Integer, db.ForeignKey('student.student_id'), nullable=False)
    ecourse_id = db.Column(db.Integer, db.ForeignKey('course.course_id'), nullable=False)

def check_roll_no_exists(roll_no: str) -> bool:
    result = Student.query.where(Student.roll_number == roll_no).one_or_none()
    if result is None:
        return False
    else:
        return True

@app.route('/')
def index():
    students = Student.query.all()
    if len(students) == 0:
        return render_template("empty_index.html")
    else:
        return render_template("index.html", students=students)

@app.route('/student/create', methods=['GET', 'POST'])
def add_student():
    if request.method == 'GET':
        return render_template("add_student.html")
    elif request.method == 'POST':
        """Extracting Form Data"""
        roll_number = request.form['roll']
        first_name = request.form['f_name']
        last_name = request.form['l_name']
        checkbox = request.form.getlist("courses")
        if check_roll_no_exists(roll_number):
            return render_template("student_exist.html")
        else:
            course_dict = {
                "course_1": "CSE01",
                "course_2": "CSE02",
                "course_3": "CSE03",
                "course_4": "BST13",
            }

            student_id = db.session.execute(text("SELECT seq FROM sqlite_sequence where name='student'")).scalar()
            enrollment_id = db.session.execute(text("SELECT seq FROM sqlite_sequence where name='enrollments'")).scalar()

            if student_id is None:
                student_id = 1
            else:
                student_id = int(student_id) + 1

            if enrollment_id is None:
                enrollment_id = 1
            else:
                enrollment_id = int(enrollment_id) + 1

            student = Student(student_id=student_id,
                              roll_number=roll_number,
                              first_name=first_name,
                              last_name=last_name)
            db.session.add(student)

            for i in checkbox:
                enroll = Enrollments(enrollment_id=enrollment_id,
                                     estudent_id=student_id,
                                     ecourse_id=course_dict[i])
                db.session.add(enroll)
                enrollment_id += 1

            db.session.commit()
            return url_for("index")

@app.route("/student/<int:student_id>/update")
def update_student(student_id):
    return render_template("update.html")

@app.route("/student/<int:student_id>/delete")
def delete_student(student_id):
    return render_template_string("delete_student page")

@app.route('/student/<int:student_id>', methods=['GET'])
def show_student(student_id):
    if request.method == 'GET':
        student = Student.query.filter_by(student_id=student_id).first()
        student_enrollment = Enrollments.query.filter_by(estudent_id=student.student_id).all()
        student_courses = []
        for i in student_enrollment:
            course_code = i.ecourse_id
            student_courses.append(Course.query.filter_by(course_code=course_code).first())
        return render_template("student_page.html", student=student, courses=student_courses)

if __name__=='__main__':
    app.run(debug=True)