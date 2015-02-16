from flask import Flask,render_template,request,redirect,make_response
import sqlite3
from DataB import app
import CheckDb
package = "DataB"
name = str.split(CheckDb.SchemaPath,".")[0]
imported = getattr(__import__(package, fromlist=[name]), name)
def DBGetCompanys():
	global CheckDb
	conn = sqlite3.connect(CheckDb.DataPath)
	c= conn.cursor()
	c.execute('''SELECT * FROM Company''')
	RawResults = c.fetchall()
	Results={}
	for x in RawResults:
		Results[x[0]]=x[1]
	return RawResults
@app.route('/',methods=['GET','POST'])
def Pagehome():
	global CheckDb
	print(CheckDb.DataPath)
	return render_template("home.html")

@app.route('/AddCompany',methods=['GET','POST'])
def PageAddCompany():	
	Companys = DBGetCompanys()
	return render_template("AddCompany.html",Companys)
