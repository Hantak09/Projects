from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
db = SQLAlchemy()
