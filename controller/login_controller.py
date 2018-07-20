'''
User authentication

'''
# -*- coding: utf-8 -*-
from flask import Blueprint, redirect, url_for, render_template, current_app
from flask_login import logout_user, login_required, login_user
from form.login_form import LoginForm
from controller import login_user_property

LOGIN_APP = Blueprint("login_controller", __name__)

@LOGIN_APP.route("/login", methods=["GET"])
def login():
    ''' login page
    '''
    login_form = LoginForm()
    return render_template("login.html", form=login_form)

@LOGIN_APP.route("/login", methods=["POST"])
def authenticate():
    ''' user authentication
    '''
    login_form = LoginForm()
    if not login_form.validate_on_submit():
        return redirect(url_for('login_controller.login'))

    email = login_form.email.data
    password = login_form.password.data
    if not email == current_app.config['EMAIL'] \
        or not password == current_app.config['PASSWORD']:

        current_app.logger.info(' fail login %s %s ' %(email, password))
        return redirect(url_for('login_controller.login'))

    login_user(login_user_property.User(email))
    current_app.logger.info('success login %s' %email)
    return redirect(url_for('img_controller.root'))

@LOGIN_APP.route("/logout", methods=["POST"])
@login_required
def logout():
    ''' logout
    '''
    logout_user()
    return redirect(url_for('login_controller.login'))
