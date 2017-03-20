from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for
from app import db
from app.report.models import GradeEntry

mod_report = Blueprint('report', __name__, url_prefix='/report')

@mod_report.route('/student/<rollno>', methods=['GET'])
def get_student_grades(rollno):
#write your code here

@mod_report.route('/course/<code>', methods=['GET'])
def get_course(code):
#write your code here
