from flask import Blueprint, render_template,request,flash, redirect,url_for
from .models import User 
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user
 
auth = Blueprint('auth',__name__)

@auth.route('/login',methods=['POST','GET'])
def login():
    if request.method =='POST':
        data = request.form 
        email = data.get('email')
        password = data.get('password')
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password,password):
                flash('Loggined in successfully',category='success')
                login_user(user,remember=True) # Log user in: remember the fact user is logged in 
                return redirect(url_for('views.home'))
            else:
                flash('Invalid password',category='error')
        else:
            flash('Email does not exist',category='success')        
    return render_template('login.html',user=current_user)

@auth.route('/logout/')
@login_required # cannot access LOGOUT if not LOGGED IN 
def logout():
    logout_user()     
    return redirect(url_for('auth.login'))  # url_for: point the url to the FUNCTION
    
    
@auth.route('/sign-up/',methods=['POST','GET'])
def sign_up():
    if request.method =='POST':
        # access the form attribute of the request --> access data 
        data =request.form 
        email = data.get('email')
        username = data.get('username')
        password1=data.get('password1')
        password2=data.get('password2')
        
        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists',category='error')
            
        # Message flashing: flash something on the screen
        elif len(email)<4:
            flash('Email must be greater than 4 characters',category='error')
        elif len(username)<2:
            flash('First name must be greater than 2 characters',category='error')
        elif password1!=password2:
            flash('Passwords do not match',category='error')
        elif len(password1)<7:
            flash('Password is too short',category='error')
        else:
            new_user=User(email=email,password=generate_password_hash(password1,method='sha256'),username=username)
            db.session.add(new_user)
            db.session.commit()
            flash('Account created',category='success')
            # must log in back after sign up
            return redirect(url_for('auth.login')) 
            

    return render_template("sign_up.html",user=current_user)