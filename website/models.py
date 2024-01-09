from website import db 
from datetime import datetime
from flask_login import UserMixin 

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(200), unique=True, nullable=False)
    name = db.Column(db.String(300), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=False)
    credit = db.Column(db.String(200), nullable=False)

class Rating(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(200), default="User", nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False) ##
    course = db.relationship('Course', backref=db.backref('ratings', lazy=True))
    stars = db.Column(db.Integer, nullable=False)
    grade = db.Column(db.String(200), nullable=False)
    difficulty = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.now(), nullable=False)
    anonymous = db.Column(db.Boolean, default=True, nullable=False)
    summary_word1 = db.Column(db.String(300), default="word1", nullable=False)
    summary_word2 = db.Column(db.String(300), default="word2", nullable=False)
    summary_word3 = db.Column(db.String(300), default="word3", nullable=False)

class User (db.Model, UserMixin):
    id = db.Column(db.Integer,primary_key=True)
    username= db.Column(db.String(150),unique=True )
    email = db.Column(db.String(150),unique=True)
    password = db.Column(db.String(50))
    
   