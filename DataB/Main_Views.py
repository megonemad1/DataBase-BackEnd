from flask import Flask,render_template,request,redirect,make_response
import sqlite3
from DataB import app
from DataB import Schema


@app.route('/',methods=['GET','POST'])
def Pagehome():
	global DataPath
	print(Schema.DataPath)
	return render_template("home.html")
def Validation(Text,Type):
	if Type=="text":
		return (Text != "")
	if Type=="id":
		try:
			i= int(Text)
		except Exception as e:
			print(e)
			return False
		return (i >=0)
			
		

@app.route('/AddCompany',methods=['GET','POST'])
def PageAddCompany():
	if request.method=="POST":
		print (request.form)
		if ( 'TxtAddCompany' in request.form):
			val = request.form['TxtAddCompany']
			if Validation(val,"text"):
				NewCompany = Schema.Company.CreateNode()
				NewCompany.CompanyName=val			
		if ( 'BtnRemoveEntry' in request.form):
			print("enter Remove")
			val = request.form['BtnRemoveEntry']
			if Validation(val,"id"):
				CompanyToRemove=Schema.Company(int(val))
				print(CompanyToRemove)
				CompanyToRemove.Removed=1
				print(CompanyToRemove)
		return redirect('/AddCompany')
	t=[]
	for n in Schema.Company.GetAllLiveKeys():
		t.append(Schema.Company(n).TableJson())
	print ("live keys: {0} Dead Keys: {1}".format(len(Schema.Company.GetAllLiveKeys()),len(Schema.Company.GetAllRawKeys())))
	return render_template("AddCompany.html",Companys=t)
