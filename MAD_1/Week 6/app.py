# from flask import Flask
# from flask_restful import Api
# from flask_restful import fields
# from flask_restful import Resource
# from flask_restful import marshal_with
# from flask_sqlalchemy import SQLAlchemy
#
# student_resource_fields = {
#     "student_id": fields.Integer,
#     "roll_number": fields.String,
#     "first_name": fields.String,
#     "last_name": fields.String
# }
# app = Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///../api_database.sqlite3"
# db = SQLAlchemy()
# db.init_app(app)
# api = Api(app)
# app.app_context().push()
#
# class Student(db.Model):
#     __tablename__ = 'student'
#     student_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     roll_number = db.Column(db.String, unique=True, nullable=False)
#     first_name = db.Column(db.String, nullable=False)
#     last_name = db.Column(db.String)
#
#
# class Course(db.Model):
#     __tablename__ = 'course'
#     course_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     course_code = db.Column(db.String, unique=True, nullable=False)
#     course_name = db.Column(db.String, nullable=False)
#
#
# class Enrollment(db.Model):
#     __tablename__ = 'enrollment'
#     enrollment_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     course_id = db.Column(db.Integer, db.ForeignKey('course.course_id'), nullable=False)
#     student_id = db.Column(db.Integer, db.ForeignKey('student.student_id'), nullable=False)
#
# class STUDENT_API(Resource):
#     @marshal_with(student_resource_fields)
#     def get(self, student_id):
#         student = Student.query.filter(Student.student_id == student_id).first()
#         if student:
#             return student
#         else:
#             return {'message': 'Student not found'}, 404
#
# api.add_resource(STUDENT_API, "/api/student", "/api/student/<int:student_id>")
#
#
# if __name__ == "__main__":
#     app.run(debug=True)