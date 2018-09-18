from flask import render_template, url_for, flash, redirect, request, abort
from . import auth
from ..models import User
from .forms import RegistrationForm, LoginForm
from .. import db
from flask_login import login_user, current_user, logout_user

@auth.route('/register',methods = ["GET","POST"])
def register():
    form = RegistrationForm()

    # if current_user.is_authenticated:
    #     return redirect(url_for('main.index'))
    if form.validate_on_submit():
        user = User(email = form.email.data, username = form.username.data, password = form.password.data)
        # user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('You are now signed up!')

        return redirect(url_for('auth.login'))
        # title = 'Create an account'
    return render_template('auth/register.html', form = form)

@auth.route('/login',methods = ["GET","POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user,form.remember.data)
            next_page = request.args.get('next')
            return redirect(url_for('main.index'))
        else:
            flash('Login unsuccessful.Invalid username or password.')
    title = "Login"
    return render_template('auth/login.html',form = form ,title = title)

@auth.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('main.index'))