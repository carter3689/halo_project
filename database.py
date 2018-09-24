from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import settings

db = settings.db

#Database Models
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(80))

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), unique=True)
    body = db.Column(db.String(300),unique=True)
    author = db.Column(db.String(50), db.ForeignKey(User.username))

db.create_all()