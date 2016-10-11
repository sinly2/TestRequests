# -*- coding: utf-8 -*-
'''
Created on Sep 30, 2016

@author: guxiwen
'''
from flask import *
from app.auth import auth
from app.models import *
from forms import loginForm
from flask_login import login_user, logout_user,login_required
from controllers import authControllers
@auth.route('/test')
def test():
    cu = authControllers.verify_password('xixi', '112233')
    if cu is True:
        return 'ok'
    return 'no ok'

@auth.route('/login',methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    user = authControllers.verify_password(username, password)
    if user:
        #print load_user(user_id).user_name
        login_user(user,remember=False)
        return redirect(url_for('main.index'))
    else:
        flash('Invalid username or password')
    return 'login failed!'

@auth.route('/login',methods=['GET'])
def login_form():
    form = loginForm()
    return render_template('login.html',form=form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out...')
    return redirect(url_for('main.index'))
