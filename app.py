
'''
create Flask-application

'''
# -*- coding: utf-8 -*-
import logging
from logging.handlers import RotatingFileHandler
from flask import Flask
from flask_login import LoginManager
from controller import img_controller, login_controller

def create_app():
    ''' initialize flaks app
    '''
    app = Flask(__name__)
    app.config.from_object('config.config.DevelopmentConfig')
    app.register_blueprint(img_controller.APP)
    app.register_blueprint(login_controller.LOGIN_APP)

    login_manager = LoginManager()
    login_manager.init_app(app)

    #setup logging
    handler = RotatingFileHandler('./logs/app.log', maxBytes=100000, backupCount=10)
    handler.setFormatter(logging.Formatter('%(asctime)s %(message)s'))
    app.logger.addHandler(handler)
    app.logger.setLevel(logging.DEBUG)

    return app
