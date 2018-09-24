from forms import *
from database import *
import settings


from flask_bootstrap import Bootstrap
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask import Flask, render_template,redirect, url_for,flash

from werkzeug.security import generate_password_hash, check_password_hash

app = settings.app
Bootstrap(app)
db = settings.db
login_manager = settings.login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


#Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user, remember=form.remember.data)
                return redirect(url_for('dashboard'))

        return '<h1>Invalid username or password</h1>'

    return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegisterForm()

    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        new_user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        return '<h1>New user has been created!</h1>'


    return render_template('signup.html', form=form)

@app.route('/dashboard', methods=['GET','POST'])
@login_required
def dashboard():
    form = PostForm()
    
    if form.validate_on_submit():
        new_post = Post(title = form.title.data, body = form.body.data, author = current_user.username)
        db.session.add(new_post)
        db.session.commit()
        return '<h1> New Post Created! </h1>'
    return render_template('dashboard.html', name=current_user.username,form=form)


@app.route('/posts/<username>',methods=['GET'])
@login_required
def displayPost(username):
    if current_user.username == username:
        posts = Post.query.filter_by(author = username).first()
        return render_template('/display_post.html',posts=posts)
    else:
        return '<h1> You do not have rights to this content </h1>'

if __name__ == '__main__':
    app.run(debug=True)