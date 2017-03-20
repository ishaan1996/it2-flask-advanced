from flask_sqlalchemy import SQLAlchemy
import flask
import os
from random import randrange, uniform

app = flask.Flask(__name__)
app.config['DEBUG'] = True
base_dir = os.path.abspath(os.path.dirname(__file__))  
sqlalchemy_database_uri = 'sqlite:///' + os.path.join(base_dir, 'app.db')
app.config['SQLALCHEMY_DATABASE_URI'] = sqlalchemy_database_uri
db = SQLAlchemy(app)

class Student(db.Model):
    __tablename__ = 'student'
    rollno = db.Column(db.String(8), primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    def __init__(self, roll, name):
        self.rollno = roll
        self.name = name

    def __repr__(self):
        return "Student { name: %r, rollno: %r }"%(self.rollno, self.name)


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




def seed_courses():
    cf = open("seed/Courses.txt")
    entries = list(map(lambda x: x.strip().split(','), cf))
    cos = list(map(lambda x: Course(*x), entries))
    for co in cos:
        db.session.add(co)
    return cos

def seed_students():
    sf = open("seed/Students.txt")
    entries = list(map(lambda x: x.strip().split(','), sf))
    sos = list(map(lambda x: Student(*x), entries))
    for so in sos:
        db.session.add(so)
    return sos

def seed_grade_entries(cos, sos):
    for student in sos:
        for course in cos:
            skeleton = {
                "assignments": 15,
                "labs": 15,
                "mids": 30,
                "end_sem": 40
            }
            obj = GradeEntry(student.rollno, course.code)
            params = {}
            for key in skeleton:
                params[key] = round(uniform(0, skeleton[key]), 2)
            obj.set(**params)
            db.session.add(obj)
    

if __name__ == '__main__':
    os.remove(os.path.join(base_dir, "app.db"))
    db.create_all()
    students = seed_students()
    courses = seed_courses()
    seed_grade_entries(courses, students)
    db.session.commit()
