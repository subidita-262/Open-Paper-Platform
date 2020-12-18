from flask import Flask, render_template, request, redirect, session, url_for
import boto3
#import key_config as keys
import os
import random, string
from dotenv import load_dotenv
from Process import User_info, Check_info

load_dotenv(".env")

app = Flask(__name__)
app.secret_key = 'BXDjbdasd1234GRPSJK456'
# Get the service resource.


@app.route("/")
def login():
	return render_template("login.html")

@app.route('/check',methods = ['post'])
def check():
    if request.method =='POST':
        session.pop('user_id', None)
        email = request.form['email']
        password = request.form['password']
        user = Check_info(email, password)
        user.check_user()
        ret_values = user.get_list()
        #print(ret_values)
        name = ret_values[1]
        user_id = ret_values[2]
        if ret_values[0] == True:
            session['user_id'] = user_id
            return render_template("home.html",name = name, user_id = user_id)
        else:
        	warning = "Wrong credentials!"
    return render_template("login.html", msg = warning)

@app.route("/registration")
def register():
	return render_template("Registration.html")

@app.route("/signup", methods =['post'])
def signup():
    if request.method == 'POST':
    	name = request.form['name']
    	email = request.form['email']
    	password = request.form['password']
    	newuser = User_info(name, email, password)
    	newuser.insert_item()

    	msg = "Registration Complete. Please Login to your account !"
    	return render_template('login.html',msg = msg)
    return render_template("Registration.html")

@app.route("/home")
def home():
	return render_template("home.html")

if __name__ == '__main__':
	app.run(debug = True)