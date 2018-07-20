
'''
create Flask-application

'''
# -*- coding: utf-8 -*-
import logging
from logging.handlers import RotatingFileHandler
from flask import Flask
from controller import img_controller

def create_app():
    ''' initialize flaks app
    '''
    app = Flask(__name__)
    app.register_blueprint(img_controller.APP)

    #setup logging
    handler = RotatingFileHandler('./logs/app.log', maxBytes=100000, backupCount=10)
    handler.setFormatter(logging.Formatter('%(asctime)s %(message)s'))
    app.logger.addHandler(handler)
    app.logger.setLevel(logging.DEBUG)

    return app
