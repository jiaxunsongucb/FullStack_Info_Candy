"""
need to update
"""
from flask import Flask, render_template, redirect, request, session, escape, url_for
from app import app, models
# from .forms import UserForm, TripForm
# Access the models file to use SQL functions
from .models import *

# index page
@app.route('/')
@app.route('/index')
def index():
    if 'username' in session:
        username = escape(session['username'])
        return redirect('/trips')
    else:
        return render_template('login.html')

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method=='POST':
        session['username'] = request.form['username']
        session['password'] = request.form['password']
        return redirect(url_for('index'))
    if request.method=='GET':
        return redirect(url_for('signup'))

@app.route('/signup', methods = ['GET', 'POST'])
def signup():
    if request.method=='POST':
        username = request.form['username']
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        password = request.form['password']
        insert_user(username, password, first_name, last_name)
        session['username'] = username
        session['first_name'] = first_name
        session['last_name'] = last_name
        session['password'] = password
        return redirect(url_for('index'))
    return render_template('signup.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('password', None)
    return redirect(url_for('index'))

@app.route('/choose')
def choose():
    return render_template('choose.html',user="test", cart="cart")

# @app.route('/create_user', methods=['GET', 'POST'])
# def create_user():

# @app.route('/order')
# def display_order():

# @app.route('/create-order', methods=['GET', 'POST'])
# def create_order():

# @app.route('/remove-order/<value>')
# def remove_order(value):

# # 404 errohandler
# @app.errorhandler(404)
def page_not_found(error):
	return render_template('page_not_found.html'), 404
