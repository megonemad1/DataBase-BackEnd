import sqlite3
DataPath = "DataB/FoodDataBase.db"

class Refrence:
	def __init__(self,CTFK,FT,FTPK):
		self.TableForeignKey=CTFK
		self.ForeignTable=FT
		self.ForeignTablePrimaryKey=FTPK
	def __str__(self):
		return '''FOREIGN KEY ({0}) REFERENCES {1}({2})'''.format(self.TableForeignKey,self.ForeignTable,self.ForeignTablePrimaryKey)
	__repr__ = __str__
	

class Table:
	
	def __init__(self,tablename):
		self.TableName=tablename
		self.col={}
		self.ref=[]
	def AddCol(self, ColAsStr):
		c = str.split(ColAsStr," ")
		#print (c)
		if len(c)>=2:
			return self.AddColByParts(c[0],c[1])
		else:
			return None
	def AddColByParts(self,ColName, ColType):
		if self != None:
			self.col[ColName]=ColType
		return self
	def AddReff(self,TableForeignKey,ForeignTable):
		if self != None:
			self.ref.append(Refrence(TableForeignKey,ForeignTable,"ID"))
			#print(self)
			self.AddColByParts(TableForeignKey,"integer")
		return self
	def __str__(self):
		if self != None:
			c= []
			for clm in self.col.keys():
				c.append(clm +" "+self.col[clm])
			s= '''CREATE TABLE IF NOT EXISTS {0} (ID integer PRIMARY KEY AUTOINCREMENT, {1}'''.format(self.TableName,", ".join(c))
		#	print (c)
			for x in self.ref:
				s+=", "+str(x)
			s+=");"
			return s
		else:
			return "error"
	__repr__ = __str__



def Check():
	global DataPath
	print (DataPath)
	conn = sqlite3.connect(DataPath)
	c= conn.cursor()
	Company = Table("Company")
	Company.AddCol("CompanyName text")
	c.execute(str(Company))
	Tutor = Table("Tutor")
	Tutor.AddCol("TutorGroup integer").AddCol("TutorTeacher text").AddReff("Company",Company.TableName)
	c.execute(str(Tutor))
	Customer= Table("Customer")
	Customer.AddCol("CustomerName text").AddReff("Tutor",Tutor.TableName)
	c.execute(str(Customer))
	Transac = Table("Transac")
	Transac.AddCol("Time timestamp").AddReff("Customer",Customer.TableName)
	c.execute(str(Transac))
	FoodSupplyer= Table("FoodSupplyer")
	FoodSupplyer.AddCol("SupplyerName Text").AddCol("Address text").AddCol("Email text").AddCol("Tell text")
	c.execute(str(FoodSupplyer))
	FoodIngredent = Table("FoodIngredent")
	FoodIngredent.AddCol("Ingredent Name").AddCol("PricePerUnit integer").AddReff("Supplyer",FoodSupplyer.TableName)
	c.execute(str(FoodIngredent))
	FoodOrder = Table("FoodOrder")
	FoodOrder.AddReff("Transac",Transac.TableName)
	FoodOrder.AddReff("FoodIngredent",FoodIngredent.TableName)
	c.execute(str(FoodOrder))
	c.close()
	conn.commit()
	f = open("Shema.py","wb")
	s="#{0}\r\n#{1}\r\n#{2}\r\n#{3}\r\n#{4}\r\n#{5}\r\n#{6}\r\n".format(str(Company),str(Tutor),str(Customer),str(Transac),str(FoodSupplyer),str(FoodIngredent),str(FoodOrder))
	s+=LoadImports()
	s+=CreatePyClass(Company)
	s+=CreatePyClass(Tutor)
	s+=CreatePyClass(Customer)
	s+=CreatePyClass(Transac)
	s+=CreatePyClass(FoodSupplyer)
	s+=CreatePyClass(FoodIngredent)
	s+=CreatePyClass(FoodOrder)
	f.write(bytes(s, 'UTF-8'))
	f.close()
	print ("checked")
def LoadImports():
	return '''from DataB import DataPath\r\nimport sqlite3\r\n'''
def addTestData():
	global DataPath
	conn = sqlite3.connect(DataPath)
	c= conn.cursor()
	for x in range(20):
		print("3")
		c.execute('''INSERT INTO Company(CompanyName) VALUES (?);''',("test"+str(x),))
		print("4")
		c.execute('''INSERT INTO Tutor(Company,TutorGroup,TutorTeacher) VALUES (?,?,?);''',(int(x/2),x,"dave"+str(x)))
	c.close()
	conn.commit()
def getTestTableDB():
	global DataPath
	conn = sqlite3.connect(DataPath)
	c= conn.cursor()
	c.execute('''SELECT CompanyName,TutorGroup,TutorTeacher FROM Company INNER JOIN Tutor on Tutor.Company= Company.ID WHERE Company.ID==1;''')
	vals = c.fetchall()
	c.close()
	return vals

def CreatePyClass(_Table):
	rs='''class {0}:\r\n\tdef __init__(self,ID):\r\n\t\t"""{1}"""\r\n{2}'''
	doc=_Table.TableName+ " Table Contains columns: "
	Atributes="\t\tconn = sqlite3.connect(DataPath)\r\n\t\tc= conn.cursor()\r\n"
	for x in _Table.col.keys():
		doc+=x+" of type "+_Table.col[x]+"|| "
		Atributes+="\t\tc.execute('''SELECT {0} FROM {1} WHERE ID=?''',ID)\r\n\t\tself.{0}=c.fetchone()\r\n".format(x,_Table.TableName)
	doc+="Foreign Keys: "
	for x in _Table.ref:
		doc+=_Table.TableName+"."+x.TableForeignKey+" refrences "+x.ForeignTable+"."+x.ForeignTablePrimaryKey
	return rs.format(_Table.TableName,doc,Atributes)
#Check()

#addTestData()

#print(getTestTableDB())

