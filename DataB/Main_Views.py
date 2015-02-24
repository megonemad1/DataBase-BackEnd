from flask import Flask,render_template,request,redirect,make_response
import sqlite3
from DataB import app
from DataB import Schema


@app.route('/',methods=['GET','POST'])
def Pagehome():
	global DataPath
	print(Schema.DataPath)
	return render_template("home.html")

@app.route('/AddCompany',methods=['GET','POST'])
def PageAddCompany():
	t=[]
	item = Schema.Company.CreateNode()
	item.CompanyName="Test1"
	item = Schema.Company.CreateNode()
	item.CompanyName="Test2"
	for n in Schema.Company.GetAllKeys():
		print (n)
		t.append(Schema.Company(n).TableJson())
		print(t)
	return render_template("AddCompany.html",Companys=t)
