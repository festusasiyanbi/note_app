from flask import Blueprint, render_template, request, flash, redirect, url_for
from . import db
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, current_user, logout_user, login_required


auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])

def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist', category='error')
    
    return render_template('login.html', user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/sign-up', methods=['GET', 'POST'])

def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        full_name = request.form.get('fullName')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')

        user = User.query.filter_by(email=email).first()

        if user:
            flash('Email already exists', category='error')
        else:
            if len(email) < 4:
                flash('Email must be greater than 3 characters', category='error')
            elif len(full_name) < 2:
                flash('Full name must be greater than 1 character', category='error')
            elif len(password) < 7:
                flash('Password must be at least 7 characters', category='error')
            elif password != confirm_password:
                flash('Passwords don\'t match', category='error')
            else:
                new_user = User(email=email, full_name=full_name, password=generate_password_hash(password=password, method='sha256'))
                db.session.add(new_user)
                db.session.commit()
                login_user(new_user, remember=True)
                flash('Account successfully created', category='success')
                return redirect(url_for('auth.login'))

    return render_template('sign_up.html', user=current_user)
