from flask import Flask
from flask_restful import Api
from flask_restful import Resource

from source.database import db

def create_app():
    server = Flask(__name__)
    server.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../api_database.sqlite3'
    db.init_app(server)
    interface = Api(server)
    server.app_context().push()
    db.create_all()
    return server, interface

app, api = create_app()

from source.api import STUDENT_API

api.add_resource(STUDENT_API, '/api/student', '/api/student/<int:student_id>')

if __name__ == '__main__':
    app.run(debug=True)