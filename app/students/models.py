from flask_sqlalchemy import SQLAlchemy
from app import db

class Student(db.Model):
    __tablename__ = 'student'
    rollno = db.Column(db.String(8), primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    def __init__(self, roll, name):
        self.rollno = roll
        self.name = name

    def __repr__(self):
        return "Student { name: %r, rollno: %r }"%(self.rollno, self.name)


