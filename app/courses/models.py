from flask_sqlalchemy import SQLAlchemy
from app import db

class Course(db.Model):
    __tablename__= 'course'
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500))
    code = db.Column(db.String(10), primary_key=True)

    def __init__(self, code, name, description):
        self.code = code
        self.name = name
        self.description = description

    def __repr__(self):
        return "Course { code: %r, name: %r, description: %r}"%(self.code, 
                self.name, self.description)
