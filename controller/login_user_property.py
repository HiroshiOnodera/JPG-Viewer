
'''
login user info

'''
# -*- coding: utf-8 -*-
from flask_login import UserMixin

class User(UserMixin):
    ''' login user info
    '''
    def __init__(self, email):
        self.id = email
