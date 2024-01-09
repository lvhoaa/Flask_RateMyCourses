from flask import Blueprint, render_template, request, flash, redirect
import json
from .models import Course, Rating, User
from .chatgpt import chatgpt_summarize
from .forms import CreateNewRating
from . import db 
from .profanity_check import profanity_check
from flask_login import current_user,login_required

views = Blueprint('views',__name__)

@views.route('/',methods=['GET'])
def home():
    courses = Course.query.all()
    return render_template('home.html', courses=courses)

@views.route('/course/<courseCode>', methods=['GET', 'POST'])
def courseHome(courseCode):
    current_course = Course.query.filter_by(code=courseCode).first()

    if current_course is None:
        return 'Course not found', 404

    ratings = Rating.query.filter_by(course_id=current_course.id).all()

    avg_stars = 0
    avg_grade = 0
    avg_difficulty = 0
    num_rating = 0

    for rating in ratings:
        avg_stars += rating.stars
        avg_grade += {"A": 4.0, "A-": 3.7, "B+": 3.3, "B": 3, "B-": 2.7, "C+": 2.3, "C": 2, "C-": 1.7, "D+": 1.3, "D": 1}.get(rating.grade, 0)
        avg_difficulty += rating.difficulty
        num_rating += 1

    if num_rating > 0:
        avg_stars = round(avg_stars / num_rating, 1)
        avg_grade = round(avg_grade / num_rating, 1)
        avg_difficulty = round(avg_difficulty / num_rating, 1)
    else:
        avg_stars = "N/A"
        avg_grade = "N/A"
        avg_difficulty = "N/A"

    if request.method == 'POST':

        form = CreateNewRating(request.form)
        if form.validate():
            stars = form.stars.data
            grade = form.grade.data
            difficulty = form.difficulty.data
            comment = form.comment.data
            anonymous = form.anonymous.data
            if profanity_check(comment):
                user_to_delete = User.query.filter_by(username=current_user.username).first()
                if user_to_delete:
                    db.session.delete(user_to_delete)
                    db.session.commit()
                    return redirect('/ban/'+current_user.username) 
            else:
            
                summary = chatgpt_summarize(comment)
                print(summary)
                summary_word1 = summary.split('.')[0].split(",")[0].upper()
                summary_word2 = summary.split('.')[0].split(",")[1].upper()
                summary_word3 = summary.split('.')[0].split(",")[2].upper()

                newRating = Rating(
                    author=request.user.username,
                    stars=stars,
                    grade=grade,
                    difficulty=difficulty,
                    comment=comment,
                    anonymous=anonymous,
                    summary_word1=summary_word1,
                    summary_word2=summary_word2,
                    summary_word3=summary_word3,
                    course_id=current_course.id
                )

                db.session.add(newRating)
                db.session.commit()

            return redirect('/course/' + courseCode)

    form = CreateNewRating()

    return render_template('course.html', course=current_course, ratings=ratings, form=form, range=range(1, 6),avg_stars=avg_stars, avg_grade=avg_grade, avg_difficulty=avg_difficulty)

@views.route('/ban/<username>')
@login_required
def banBadWords():
    return render_template('ban.html',username=current_user.username)


# CODE TO ADD COURSES DATA INTO DATABASE
# @views.route('/insert-data')
# def insert_data():
#     new_course = Course(code="SAMPLE - CLICK HERE",name="SAMPLE COURSE DISPLAY",description="SAMPLE: An introduction to data analysis in the open-source R language, with an emphasis on practical data work. Topics will include data wrangling, summary statistics, modeling, and visualization. Will also cover fundamental programming concepts including data types, functions, flow of control, and good programming practices. Intended for a broad range of students outside of computer science. Some familiarity with statistics is expected.",credit="4")
#     db.session.add(new_course)
    
#     with open('website\data\courses.json') as json_data:
#         courses =json.load(json_data)
#     for course in courses:
#         newCourse = Course(code=course['code'],name=course['name'],description=course['description'],credit=course['credit'])
#         db.session.add(newCourse)
    
#     db.session.commit()
#     return "Insert data successfully"

# @views.route('/delete-all-courses')
# def delete_all_courses():
#     db.session.query(Course).delete()
#     db.session.commit()

#     return 'Delete all courses successfully!'