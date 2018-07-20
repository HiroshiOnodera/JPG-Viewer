'''
start
'''
# -*- encoding utf-8 -*-
from flask import redirect, url_for
from flask_login import LoginManager
from app import create_app
from controller import login_user_property

APP = create_app()

LOGIN_MANAGER = LoginManager()
LOGIN_MANAGER.init_app(APP)

@LOGIN_MANAGER.user_loader
def user_loader(email):
    '''
    flask-login
    user loader
    '''
    user = login_user_property.User(email)
    return user

@LOGIN_MANAGER.unauthorized_handler
def unauthorized():
    ''' When Users not logged in , redirect to login page
    '''
    return redirect(url_for("login_controller.login"))
