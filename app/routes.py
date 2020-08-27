from flask import render_template,redirect,url_for,flash,request
from app import app,db
from app.forms import LoginForm,RegistrationForm,EditProfileForm
from flask_login import current_user,login_user,logout_user,login_required
from app.models import User
from werkzeug.urls import url_parse
from datetime import datetime

#all the view functions will be defined here
@app.route('/')
@app.route('/index')
@login_required
def index():
    #below is just a dummy user and posts
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html',title="Varuns'",posts=posts)

#login view function
@app.route('/login',methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form=LoginForm()
    if form.validate_on_submit():
        user=User.query.filter(User.username == form.username.data).first()

        if user is None or not user.check_password(form.password.data):
            flash(message='Invalid Username or password')
            return redirect(url_for('login'))
        login_user(user,remember=form.remember_me.data)
        next_page = request.args.get('next')
        #below line is my own jugad if this blows up see carefully
        if not next_page or url_parse(next_page).netloc != '' or next_page=='/' or next_page==' ':
            next_page='index'
        return redirect(url_for(next_page))

    return render_template('login.html',title='Sign In',form=form)


#logout view function
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))


#register route function
@app.route('/register',methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        redirect(url_for('index'))
    form=RegistrationForm()
    if form.validate_on_submit and request.method=='POST':
        userobj=User(username=form.username.data,email=form.email.data)
        userobj.set_password(form.password.data)
        db.session.add(userobj)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html',form=form)

#user profile
@app.route('/user/<username>')
@login_required
def user(username):
    user= User.query.filter(User.username == username).first_or_404()
    posts = [
        {'author': user, 'body': 'Test post #1'},
        {'author': user, 'body': 'Test post #2'}
    ]
    return render_template('user.html',user=user,posts=posts)


#this route is for getting last seen
@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen=datetime.utcnow()
        db.session.commit()

#this route is for profile editing
@app.route('/edit_profile',methods=['GET','POST'])
@login_required
def edit_profile():
    form=EditProfileForm()
    if form.validate_on_submit() and request.method=='POST':
        user=current_user
        user.username=form.username.data
        user.about_me=form.about_me.data
        db.session.add(user)
        db.session.commit()
        flash('Your changes have been saved')
        return redirect(url_for('edit_profile'))
    form.username.data=current_user.username
    form.about_me.data=current_user.about_me
    return render_template('edit_profile.html',form=form) 