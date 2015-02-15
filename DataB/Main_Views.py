from flask import Flask,render_template,request,redirect,make_response
import sqlite3
from DataB import app
from DataB import DataPath


@app.route('/',methods=['GET','POST'])
def home():
	global DataPath
	print(DataPath)
	return render_template("home.html")
