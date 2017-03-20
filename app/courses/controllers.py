from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for
from app import db
from app.courses.models import Course

mod_courses = Blueprint('courses', __name__, url_prefix='/courses')

@mod_courses.route('/', methods=['GET'])
def get_all_courses():
#write your code here

@mod_courses.route('/search', methods=['GET'])
def search_courses():
#write your code here

@mod_courses.route('/<code>', methods=['GET'])
def get_course(code):
#write your code here

