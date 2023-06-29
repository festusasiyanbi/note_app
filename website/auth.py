from flask import Blueprint

auths = Blueprint('auths', __name__)

@auths.route("/login")

def login():
    return "<p>Login Page</p>"

@auths.route("/logout")

def logout():
    return "<p>logout Page</p>"

@auths.route("/sign-up")

def sign_up():
    return "<p>sign up Page</p>"