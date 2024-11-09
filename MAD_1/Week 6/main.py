from flask import Flask
from flask_restful import Api
from source.database import db


def create_app():
    server = Flask(__name__)
    server.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///api_database.sqlite3'
    api = Api(server)
    db.init_app(server)
    server.app_context().push()
    return server, api

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)