from flask import render_template, url_for, flash, redirect, request ,send_from_directory,make_response,jsonify
from lms import app,db,bcrypt
from .forms import Logininstructor, Registration,Login,Registerinstructor
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

@app.route('/admindashboard')
def admindashboard():
    if current_user.is_authenticated:
        return render_template('admindashboard.html')
    else:
        return redirect(url_for('login'))


@app.route('/instructordashboard')
@login_required
def instructordashboard():
    if current_user.is_authenticated:
        return render_template('instructordashboard.html')
    else:
        return redirect(url_for('instructorlogin'))



@app.route('/register', methods=['GET' ,'POST'])
def register():
    register = Registration()
    if request.method == "POST":
        form = request.form
      
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        password1 = request.form['confirmpassword']
        print(User.query.filter_by(email=email).first().email)
        if User.query.filter_by(email=email).first().email == email:
            flash('Email Address already Exists', 'danger')
        else:
            hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
            user = User(name=name.lower(),email=email.lower(),password=hashed_password)
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
        if request.form['rememberme']:
            remember = request.form['rememberme']
        else:
            remember = 'no'
        user = User.query.filter_by(email=email).first()
        if user and bcrypt.check_password_hash(user.password, password):
            login_user(user, remember= remember)
            if current_user.role== "user":
              #  next_page = request.args.get('next')#requests current url and redirects to next page otherwise it returns to the dashboard
                return redirect(url_for('dashboard'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html',form = form)


@app.route('/logininstructor')
def logininstructor():
    form = Logininstructor()
    if current_user.is_authenticated:
        return redirect(url_for('instructordashboard'))
    if request.method == "POST":
        form = request.form
        email = request.form['email']
        password = request.form['password']
        if request.form['rememberme']:
            remember = request.form['rememberme']
        else:
            remember = 'no'
            user = User.query.filter_by(email=email).first()
            if user and bcrypt.check_password_hash(user.password, password):
                login_user(user, remember=remember)
                if current_user.role== "user":
                    return redirect(url_for(instructordashboard))
            else:
                flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('logininstructor.html',form = form)


#@app.route('/registerinstructor')
#def registerinstructor():
    #return render_template('registerinstructor.html')


@app.route('/registerinstructor', methods=['GET','POST'])
def registerinstructor():
    register = Registerinstructor()#am getting an error here
    #if request.method =='GET':
    #   return "Register via the Registration Page"
    if request.method == "POST":
        form = request.form #is this right
        email = request.form['email']
        password = request.form['password']
        confirmpassword = request.form['confirmpassword']
        username = request.form['username']
        coursecode = request.form['coursecode']
        rememberme = rememberme.form['rememberme']
        role = 'instructor'

        print(User.query.filter_by(email=email).first().email)
        if User.query.filter_by(email=email).first().email == email:
            flash('Email Address already Exists', 'danger')
        else:
            hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
            user = User(name=username.lower(),email=email.lower(),password=hashed_password)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('instructordashboard'))
    return render_template('registerinstructor.html',form = Registerinstructor())# alternatively you can use form = register
    
#@app.route("/logout")
#def logout():
  #  logout_user()
  #  return redirect(url_for('login'))

@app.route("/logout", methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    flash("You Have Logged Out Successfully! Remember to keep track of your progress")
    return redirect(url_for('login'))
