# -*- coding: utf-8 -*-
'''
Created on Oct 1, 2016

@author: guxiwen
'''
from flask_wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Required, Length, Email


class loginForm(Form):
    username = StringField('username',validators=[Required(),Length(1,12)])
    password = PasswordField('password',validators=[Required()])
    submit = SubmitField('Log In')