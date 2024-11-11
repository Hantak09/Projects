from app import db
from app import app
from app import Course
from app import Student
from app import Enrollment

with app.app_context():
    db.create_all()

