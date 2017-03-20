from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for
from app import db
from app.students.models import Student

mod_students = Blueprint('students', __name__, url_prefix='/students')

@mod_students.route('/', methods=['GET'])
def get_all_students():
    students = Student.query.all()
    return render_template('students/index.html', students=students)

@mod_students.route('/<rollno>', methods=['GET'])
def get_student(rollno):
    student = Student.query.filter(Student.rollno == rollno).all()
    return render_template('students/index.html', students=student)
