from flask import Flask
import sqlite3
from DataB import app
DataBase = "FoodDb.db"
@app.route('/',methods=['GET','POST'])
def home():
	return "test"
