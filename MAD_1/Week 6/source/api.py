from flask_restful import fields
from flask_restful import Resource
from flask_restful import marshal_with

from source.database import db
from source.models import Student

student_resource_fields = {
    "student_id": fields.Integer,
    "roll_number": fields.String,
    "first_name": fields.String,
    "last_name": fields.String
}

class STUDENT_API(Resource):
    @marshal_with(student_resource_fields)
    def get(self, student_id):
        student = Student.query.filter(Student.student_id ==student_id).first()
        return student