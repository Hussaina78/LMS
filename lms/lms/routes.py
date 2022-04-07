from flask import render_template, url_for, flash, redirect, request ,send_from_directory,make_response,jsonify
from lms import app,db,bcrypt
from .forms import Registration,Login
from .models import User
from flask_login import login_user, current_user, logout_user, login_required
from werkzeug.utils import secure_filename
import array, os, json


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    if current_user.is_authenticated:
        return render_template('dashboard/index.html')
    else:
        return redirect(url_for('login'))

@app.route('/logininstructor')
def logininstructor():
    return render_template('logininstructor.html')


@app.route('/register', methods=['GET' ,'POST'])
def register():
    register = Registration()
    if request.method == "POST":
        form = request.form
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        password1 = request.form['confirmpassword']
        email_pref = request.form['email_preference']
        if User.query.filter_by(email=email).first() == email:
            flash('Email Address already Exists', 'danger')
        else:
            hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
            user = User(name=name.lower(),email=email.lower(),password=hashed_password, email_preference= email_pref)
            db.session.add(user)
            db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html',form = register)
    

@app.route('/login', methods=['GET' ,'POST'])
def login():
    form = Login()
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    if request.method == "POST":
        form = request.form
        email = request.form['email']
        password = request.form['password']
        remember = request.form['rememberme']
        user = User.query.filter_by(email=email).first()
        if user and bcrypt.check_password_hash(user.password, password):
            login_user(user, remember= remember)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('dashboard'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html',form = form)




@app.route('/registerinstructor')
def registerinstructor():
    return render_template('registerinstructor.html')


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('login'))
