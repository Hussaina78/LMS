from unicodedata import category
from matplotlib import image
from lms import db,login_manager,app
from datetime import datetime
from flask_login import UserMixin



@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    address = db.Column(db.String(120), unique=False, nullable=True)
    role = db.Column(db.String(120), unique=False, nullable=True, default='user')
    password = db.Column(db.String(250),unique=False, nullable=False)
    email_preference = db.Column(db.String(120), unique=False, nullable=False)
    
    def __repr__(self):
        return f"User('{self.id}','{self.name}','{self.role}','{self.email}')"


class Courses(db.Model):
    __tablename__ = 'courses'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), unique=False, nullable=False)
    description = db.Column(db.String(120), unique=False, nullable=False)
    category = db.Column(db.String(120), unique=False, nullable=False)
    duration = db.Column(db.String(120), unique=False, nullable=False)
    instructor = db.Column(db.String(120), unique=False, nullable=False)
    image = db.Column(db.String(120), unique=False, nullable=True)
    def __repr__(self):
        return f"Courses('{self.id}','{self.title}','{self.description}','{self.image}')"