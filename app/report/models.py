from flask_sqlalchemy import SQLAlchemy
from app import db


class GradeEntry(db.Model):
    __tablename__ = 'grade_entry'
    assignments = db.Column(db.Float)
    labs = db.Column(db.Float)
    mids = db.Column(db.Float)
    end_sem = db.Column(db.Float)
    student_rollno = db.Column(db.String(8), db.ForeignKey("student.rollno"))
    course_code = db.Column(db.String(10), db.ForeignKey("course.code"))
    id = db.Column(db.Integer, primary_key=True)


    def __init__(self, student, course):
        self.assignments = 0.0
        self.labs = 0.0
        self.mids = 0.0
        self.end_sem = 0.0
        self.student_rollno = student
        self.course_code = course

    def set(self, **kwargs):
        if "assignments" in kwargs:
            self.assignments = kwargs["assignments"]

        if "labs" in kwargs:
            self.labs = kwargs["labs"]

        if "mids" in kwargs:
            self.mids = kwargs["mids"]

        if "end_sem" in kwargs:
            self.end_sem = kwargs["end_sem"]



