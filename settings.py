import os
from flask import Flask, render_template,redirect, url_for,flash
from flask_bootstrap import Bootstrap

from flask_login import LoginManager

from flask_sqlalchemy import SQLAlchemy





app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://cwkqdony:XBBKHlMjl572S8kkNtMHArOi_9qltXH5@tantor.db.elephantsql.com:5432/cwkqdony'
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'