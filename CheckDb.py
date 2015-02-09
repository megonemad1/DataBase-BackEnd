import sqlite3
DataPath = "database.db"
def Check():
	global DataPath
	conn = sqlite3.connect(DataPath)
	c= conn.cursor()
	print("1")
	c.execute('''CREATE TABLE IF NOT EXISTS Company (ID integer PRIMARY KEY AUTOINCREMENT, CompanyName text);''')
	print("2")
	c.execute('''CREATE TABLE IF NOT EXISTS Tutor (ID INTEGER PRIMARY KEY AUTOINCREMENT,TutorCompany int, TutorGroup int, TutorTeacher text, FOREIGN KEY (TutorCompany) REFERENCES Company(ID));''')
	c.close()
	conn.commit()
def addData():
	global DataPath
	conn = sqlite3.connect(DataPath)
	c= conn.cursor()
	for x in range(20):
		print("3")
		c.execute('''INSERT INTO Company(CompanyName) VALUES (?);''',("test"+str(x),))
		print("4")
		c.execute('''INSERT INTO Tutor(TutorCompany,TutorGroup,TutorTeacher) VALUES (?,?,?);''',(int(x/2),x,"dave"+str(x)))
	c.close()
	conn.commit()
def getTableDB():
	global DataPath
	conn = sqlite3.connect(DataPath)
	c= conn.cursor()
	c.execute('''SELECT CompanyName,TutorGroup,TutorTeacher FROM Company INNER JOIN Tutor on Tutor.TutorCompany= Company.ID WHERE Company.ID==1;''')
	vals = c.fetchall()
	c.close()
	return vals
Check()
addData()
print(getTableDB())
print ("checked")