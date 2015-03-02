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
			
def tableJson(Tablecls=None):
	if Tablecls==None:
		return None
	t=[]
	for n in Tablecls.GetAllKeys():
		t.append(Tablecls(n).TableJson())
	return t

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
				CompanyToRemove.Remove()
		if ( 'BtnEditEntry' in request.form):			
			val = request.form['BtnEditEntry']
			print(val)
			if Validation(val,"id"):
				#print('/EditCompany/'+str(val))
				return redirect('/EditCompany/'+str(val))
		return redirect('/AddCompany')
	t=tableJson(Schema.Company)
	
	print ("keys: {0} ".format(len(Schema.Company.GetAllKeys())))
	return render_template("AddCompany.html",FullTable=t,TableKeys=Schema.Company.expectedkeys())


@app.route('/AddTutor',methods=['GET','POST'])
def PageAddTutor():
	if request.method=="POST":
			#formstuff
		return redirect('/AddTutor')
	t=tableJson(Schema.Tutor)
	print ("keys: {0} ".format(len(Schema.Company.GetAllKeys())))
	return render_template("AddCompany.html",Tutor=t,TableKeys=Schema.Tutor.expectedkeys())