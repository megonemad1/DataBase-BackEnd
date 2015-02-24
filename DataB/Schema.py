#CREATE TABLE IF NOT EXISTS Company (ID integer PRIMARY KEY AUTOINCREMENT, CompanyName text);
#CREATE TABLE IF NOT EXISTS Tutor (ID integer PRIMARY KEY AUTOINCREMENT, TutorGroup integer, Company integer, TutorTeacher text, FOREIGN KEY (Company) REFERENCES Company(ID));
#CREATE TABLE IF NOT EXISTS Customer (ID integer PRIMARY KEY AUTOINCREMENT, Tutor integer, CustomerName text, FOREIGN KEY (Tutor) REFERENCES Tutor(ID));
#CREATE TABLE IF NOT EXISTS Transac (ID integer PRIMARY KEY AUTOINCREMENT, Time timestamp, Customer integer, FOREIGN KEY (Customer) REFERENCES Customer(ID));
#CREATE TABLE IF NOT EXISTS FoodSupplyer (ID integer PRIMARY KEY AUTOINCREMENT, SupplyerName Text, Tell text, Email text, Address text);
#CREATE TABLE IF NOT EXISTS FoodIngredent (ID integer PRIMARY KEY AUTOINCREMENT, Ingredent Name, Supplyer integer, PricePerUnit integer, FOREIGN KEY (Supplyer) REFERENCES FoodSupplyer(ID));
#CREATE TABLE IF NOT EXISTS FoodOrder (ID integer PRIMARY KEY AUTOINCREMENT, FoodIngredent integer, Transac integer, FOREIGN KEY (Transac) REFERENCES Transac(ID), FOREIGN KEY (FoodIngredent) REFERENCES FoodIngredent(ID));
import sqlite3
import itertools
import functools
DataPath="FoodDataBase.db"
class Company:
	def __init__(self,ID):
		"""Company Table Contains columns: CompanyName of type text|| Foreign Keys: """
		self.ID=ID
	@classmethod
	def GetAllKeys(cls):
		global DataPath
		conn = sqlite3.connect(DataPath)
		c= conn.cursor()
		c.execute('''SELECT ID FROM Company''')
		Val= c.fetchall()
		c.close()
		return list(functools.reduce(itertools.chain,Val))
	@classmethod
	def CreateNode(cls):
		global DataPath
		conn = sqlite3.connect(DataPath)
		c= conn.cursor()
		c.execute("INSERT INTO Company(CompanyName) VALUES (?)",(None,))
		NewID=c.lastrowid
		c.close()
		conn.commit()
		return cls(NewID)
	@property
	def CompanyName(self):
		global DataPath
		conn = sqlite3.connect(DataPath)
		c= conn.cursor()
		c.execute('''SELECT CompanyName FROM Company WHERE ID=?''',(self.ID,))
		Val= c.fetchone()
		c.close()
		return Val[0]
	@CompanyName.setter
	def CompanyName(self,value):
		global DataPath
		conn = sqlite3.connect(DataPath)
		c= conn.cursor()
		c.execute('''UPDATE Company SET CompanyName=? WHERE ID=?''',(value,self.ID))
		c.close()
		conn.commit()
	def TableJson(self):
		r={"ID":self.ID}
		r["CompanyName"]=self.CompanyName
		return r
	def __str__(self):
		return str(self.TableJson())
class Tutor:
	def __init__(self,ID):
		"""Tutor Table Contains columns: TutorGroup of type integer|| Company of type integer|| TutorTeacher of type text|| Foreign Keys: Tutor.Company refrences Company.ID"""
		self.ID=ID
	@classmethod
	def GetAllKeys(cls):
		global DataPath
		conn = sqlite3.connect(DataPath)
		c= conn.cursor()
		c.execute('''SELECT ID FROM Tutor''')
		Val= c.fetchall()
		c.close()
		return list(functools.reduce(itertools.chain,Val))
	@classmethod
	def CreateNode(cls):
		global DataPath
		conn = sqlite3.connect(DataPath)
		c= conn.cursor()
		c.execute("INSERT INTO Tutor(TutorGroup,Company,TutorTeacher) VALUES (?,?,?)",(None,None,None,))
		NewID=c.lastrowid
		c.close()
		conn.commit()
		return cls(NewID)
	@property
	def TutorGroup(self):
		global DataPath
		conn = sqlite3.connect(DataPath)
		c= conn.cursor()
		c.execute('''SELECT TutorGroup FROM Tutor WHERE ID=?''',(self.ID,))
		Val= c.fetchone()
		c.close()
		return Val[0]
	@TutorGroup.setter
	def TutorGroup(self,value):
		global DataPath
		conn = sqlite3.connect(DataPath)
		c= conn.cursor()
		c.execute('''UPDATE Tutor SET TutorGroup=? WHERE ID=?''',(value,self.ID))
		c.close()
		conn.commit()
	@property
	def Company(self):
		global DataPath
		conn = sqlite3.connect(DataPath)
		c= conn.cursor()
		c.execute('''SELECT Company FROM Tutor WHERE ID=?''',(self.ID,))
		Val= c.fetchone()
		c.close()
		return Val[0]
	@Company.setter
	def Company(self,value):
		global DataPath
		conn = sqlite3.connect(DataPath)
		c= conn.cursor()
		c.execute('''UPDATE Tutor SET Company=? WHERE ID=?''',(value,self.ID))
		c.close()
		conn.commit()
	@property
	def TutorTeacher(self):
		global DataPath
		conn = sqlite3.connect(DataPath)
		c= conn.cursor()
		c.execute('''SELECT TutorTeacher FROM Tutor WHERE ID=?''',(self.ID,))
		Val= c.fetchone()
		c.close()
		return Val[0]
	@TutorTeacher.setter
	def TutorTeacher(self,value):
		global DataPath
		conn = sqlite3.connect(DataPath)
		c= conn.cursor()
		c.execute('''UPDATE Tutor SET TutorTeacher=? WHERE ID=?''',(value,self.ID))
		c.close()
		conn.commit()
	def TableJson(self):
		r={"ID":self.ID}
		r["TutorGroup"]=self.TutorGroup
		r["Company"]=self.Company
		r["TutorTeacher"]=self.TutorTeacher
		return r
	def __str__(self):
		return str(self.TableJson())
class Customer:
	def __init__(self,ID):
		"""Customer Table Contains columns: Tutor of type integer|| CustomerName of type text|| Foreign Keys: Customer.Tutor refrences Tutor.ID"""
		self.ID=ID
	@classmethod
	def GetAllKeys(cls):
		global DataPath
		conn = sqlite3.connect(DataPath)
		c= conn.cursor()
		c.execute('''SELECT ID FROM Customer''')
		Val= c.fetchall()
		c.close()
		return list(functools.reduce(itertools.chain,Val))
	@classmethod
	def CreateNode(cls):
		global DataPath
		conn = sqlite3.connect(DataPath)
		c= conn.cursor()
		c.execute("INSERT INTO Customer(Tutor,CustomerName) VALUES (?,?)",(None,None,))
		NewID=c.lastrowid
		c.close()
		conn.commit()
		return cls(NewID)
	@property
	def Tutor(self):
		global DataPath
		conn = sqlite3.connect(DataPath)
		c= conn.cursor()
		c.execute('''SELECT Tutor FROM Customer WHERE ID=?''',(self.ID,))
		Val= c.fetchone()
		c.close()
		return Val[0]
	@Tutor.setter
	def Tutor(self,value):
		global DataPath
		conn = sqlite3.connect(DataPath)
		c= conn.cursor()
		c.execute('''UPDATE Customer SET Tutor=? WHERE ID=?''',(value,self.ID))
		c.close()
		conn.commit()
	@property
	def CustomerName(self):
		global DataPath
		conn = sqlite3.connect(DataPath)
		c= conn.cursor()
		c.execute('''SELECT CustomerName FROM Customer WHERE ID=?''',(self.ID,))
		Val= c.fetchone()
		c.close()
		return Val[0]
	@CustomerName.setter
	def CustomerName(self,value):
		global DataPath
		conn = sqlite3.connect(DataPath)
		c= conn.cursor()
		c.execute('''UPDATE Customer SET CustomerName=? WHERE ID=?''',(value,self.ID))
		c.close()
		conn.commit()
	def TableJson(self):
		r={"ID":self.ID}
		r["Tutor"]=self.Tutor
		r["CustomerName"]=self.CustomerName
		return r
	def __str__(self):
		return str(self.TableJson())
class Transac:
	def __init__(self,ID):
		"""Transac Table Contains columns: Time of type timestamp|| Customer of type integer|| Foreign Keys: Transac.Customer refrences Customer.ID"""
		self.ID=ID
	@classmethod
	def GetAllKeys(cls):
		global DataPath
		conn = sqlite3.connect(DataPath)
		c= conn.cursor()
		c.execute('''SELECT ID FROM Transac''')
		Val= c.fetchall()
		c.close()
		return list(functools.reduce(itertools.chain,Val))
	@classmethod
	def CreateNode(cls):
		global DataPath
		conn = sqlite3.connect(DataPath)
		c= conn.cursor()
		c.execute("INSERT INTO Transac(Time,Customer) VALUES (?,?)",(None,None,))
		NewID=c.lastrowid
		c.close()
		conn.commit()
		return cls(NewID)
	@property
	def Time(self):
		global DataPath
		conn = sqlite3.connect(DataPath)
		c= conn.cursor()
		c.execute('''SELECT Time FROM Transac WHERE ID=?''',(self.ID,))
		Val= c.fetchone()
		c.close()
		return Val[0]
	@Time.setter
	def Time(self,value):
		global DataPath
		conn = sqlite3.connect(DataPath)
		c= conn.cursor()
		c.execute('''UPDATE Transac SET Time=? WHERE ID=?''',(value,self.ID))
		c.close()
		conn.commit()
	@property
	def Customer(self):
		global DataPath
		conn = sqlite3.connect(DataPath)
		c= conn.cursor()
		c.execute('''SELECT Customer FROM Transac WHERE ID=?''',(self.ID,))
		Val= c.fetchone()
		c.close()
		return Val[0]
	@Customer.setter
	def Customer(self,value):
		global DataPath
		conn = sqlite3.connect(DataPath)
		c= conn.cursor()
		c.execute('''UPDATE Transac SET Customer=? WHERE ID=?''',(value,self.ID))
		c.close()
		conn.commit()
	def TableJson(self):
		r={"ID":self.ID}
		r["Time"]=self.Time
		r["Customer"]=self.Customer
		return r
	def __str__(self):
		return str(self.TableJson())
class FoodSupplyer:
	def __init__(self,ID):
		"""FoodSupplyer Table Contains columns: SupplyerName of type Text|| Tell of type text|| Email of type text|| Address of type text|| Foreign Keys: """
		self.ID=ID
	@classmethod
	def GetAllKeys(cls):
		global DataPath
		conn = sqlite3.connect(DataPath)
		c= conn.cursor()
		c.execute('''SELECT ID FROM FoodSupplyer''')
		Val= c.fetchall()
		c.close()
		return list(functools.reduce(itertools.chain,Val))
	@classmethod
	def CreateNode(cls):
		global DataPath
		conn = sqlite3.connect(DataPath)
		c= conn.cursor()
		c.execute("INSERT INTO FoodSupplyer(SupplyerName,Tell,Email,Address) VALUES (?,?,?,?)",(None,None,None,None,))
		NewID=c.lastrowid
		c.close()
		conn.commit()
		return cls(NewID)
	@property
	def SupplyerName(self):
		global DataPath
		conn = sqlite3.connect(DataPath)
		c= conn.cursor()
		c.execute('''SELECT SupplyerName FROM FoodSupplyer WHERE ID=?''',(self.ID,))
		Val= c.fetchone()
		c.close()
		return Val[0]
	@SupplyerName.setter
	def SupplyerName(self,value):
		global DataPath
		conn = sqlite3.connect(DataPath)
		c= conn.cursor()
		c.execute('''UPDATE FoodSupplyer SET SupplyerName=? WHERE ID=?''',(value,self.ID))
		c.close()
		conn.commit()
	@property
	def Tell(self):
		global DataPath
		conn = sqlite3.connect(DataPath)
		c= conn.cursor()
		c.execute('''SELECT Tell FROM FoodSupplyer WHERE ID=?''',(self.ID,))
		Val= c.fetchone()
		c.close()
		return Val[0]
	@Tell.setter
	def Tell(self,value):
		global DataPath
		conn = sqlite3.connect(DataPath)
		c= conn.cursor()
		c.execute('''UPDATE FoodSupplyer SET Tell=? WHERE ID=?''',(value,self.ID))
		c.close()
		conn.commit()
	@property
	def Email(self):
		global DataPath
		conn = sqlite3.connect(DataPath)
		c= conn.cursor()
		c.execute('''SELECT Email FROM FoodSupplyer WHERE ID=?''',(self.ID,))
		Val= c.fetchone()
		c.close()
		return Val[0]
	@Email.setter
	def Email(self,value):
		global DataPath
		conn = sqlite3.connect(DataPath)
		c= conn.cursor()
		c.execute('''UPDATE FoodSupplyer SET Email=? WHERE ID=?''',(value,self.ID))
		c.close()
		conn.commit()
	@property
	def Address(self):
		global DataPath
		conn = sqlite3.connect(DataPath)
		c= conn.cursor()
		c.execute('''SELECT Address FROM FoodSupplyer WHERE ID=?''',(self.ID,))
		Val= c.fetchone()
		c.close()
		return Val[0]
	@Address.setter
	def Address(self,value):
		global DataPath
		conn = sqlite3.connect(DataPath)
		c= conn.cursor()
		c.execute('''UPDATE FoodSupplyer SET Address=? WHERE ID=?''',(value,self.ID))
		c.close()
		conn.commit()
	def TableJson(self):
		r={"ID":self.ID}
		r["SupplyerName"]=self.SupplyerName
		r["Tell"]=self.Tell
		r["Email"]=self.Email
		r["Address"]=self.Address
		return r
	def __str__(self):
		return str(self.TableJson())
class FoodIngredent:
	def __init__(self,ID):
		"""FoodIngredent Table Contains columns: Ingredent of type Name|| Supplyer of type integer|| PricePerUnit of type integer|| Foreign Keys: FoodIngredent.Supplyer refrences FoodSupplyer.ID"""
		self.ID=ID
	@classmethod
	def GetAllKeys(cls):
		global DataPath
		conn = sqlite3.connect(DataPath)
		c= conn.cursor()
		c.execute('''SELECT ID FROM FoodIngredent''')
		Val= c.fetchall()
		c.close()
		return list(functools.reduce(itertools.chain,Val))
	@classmethod
	def CreateNode(cls):
		global DataPath
		conn = sqlite3.connect(DataPath)
		c= conn.cursor()
		c.execute("INSERT INTO FoodIngredent(Ingredent,Supplyer,PricePerUnit) VALUES (?,?,?)",(None,None,None,))
		NewID=c.lastrowid
		c.close()
		conn.commit()
		return cls(NewID)
	@property
	def Ingredent(self):
		global DataPath
		conn = sqlite3.connect(DataPath)
		c= conn.cursor()
		c.execute('''SELECT Ingredent FROM FoodIngredent WHERE ID=?''',(self.ID,))
		Val= c.fetchone()
		c.close()
		return Val[0]
	@Ingredent.setter
	def Ingredent(self,value):
		global DataPath
		conn = sqlite3.connect(DataPath)
		c= conn.cursor()
		c.execute('''UPDATE FoodIngredent SET Ingredent=? WHERE ID=?''',(value,self.ID))
		c.close()
		conn.commit()
	@property
	def Supplyer(self):
		global DataPath
		conn = sqlite3.connect(DataPath)
		c= conn.cursor()
		c.execute('''SELECT Supplyer FROM FoodIngredent WHERE ID=?''',(self.ID,))
		Val= c.fetchone()
		c.close()
		return Val[0]
	@Supplyer.setter
	def Supplyer(self,value):
		global DataPath
		conn = sqlite3.connect(DataPath)
		c= conn.cursor()
		c.execute('''UPDATE FoodIngredent SET Supplyer=? WHERE ID=?''',(value,self.ID))
		c.close()
		conn.commit()
	@property
	def PricePerUnit(self):
		global DataPath
		conn = sqlite3.connect(DataPath)
		c= conn.cursor()
		c.execute('''SELECT PricePerUnit FROM FoodIngredent WHERE ID=?''',(self.ID,))
		Val= c.fetchone()
		c.close()
		return Val[0]
	@PricePerUnit.setter
	def PricePerUnit(self,value):
		global DataPath
		conn = sqlite3.connect(DataPath)
		c= conn.cursor()
		c.execute('''UPDATE FoodIngredent SET PricePerUnit=? WHERE ID=?''',(value,self.ID))
		c.close()
		conn.commit()
	def TableJson(self):
		r={"ID":self.ID}
		r["Ingredent"]=self.Ingredent
		r["Supplyer"]=self.Supplyer
		r["PricePerUnit"]=self.PricePerUnit
		return r
	def __str__(self):
		return str(self.TableJson())
class FoodOrder:
	def __init__(self,ID):
		"""FoodOrder Table Contains columns: FoodIngredent of type integer|| Transac of type integer|| Foreign Keys: FoodOrder.Transac refrences Transac.IDFoodOrder.FoodIngredent refrences FoodIngredent.ID"""
		self.ID=ID
	@classmethod
	def GetAllKeys(cls):
		global DataPath
		conn = sqlite3.connect(DataPath)
		c= conn.cursor()
		c.execute('''SELECT ID FROM FoodOrder''')
		Val= c.fetchall()
		c.close()
		return list(functools.reduce(itertools.chain,Val))
	@classmethod
	def CreateNode(cls):
		global DataPath
		conn = sqlite3.connect(DataPath)
		c= conn.cursor()
		c.execute("INSERT INTO FoodOrder(FoodIngredent,Transac) VALUES (?,?)",(None,None,))
		NewID=c.lastrowid
		c.close()
		conn.commit()
		return cls(NewID)
	@property
	def FoodIngredent(self):
		global DataPath
		conn = sqlite3.connect(DataPath)
		c= conn.cursor()
		c.execute('''SELECT FoodIngredent FROM FoodOrder WHERE ID=?''',(self.ID,))
		Val= c.fetchone()
		c.close()
		return Val[0]
	@FoodIngredent.setter
	def FoodIngredent(self,value):
		global DataPath
		conn = sqlite3.connect(DataPath)
		c= conn.cursor()
		c.execute('''UPDATE FoodOrder SET FoodIngredent=? WHERE ID=?''',(value,self.ID))
		c.close()
		conn.commit()
	@property
	def Transac(self):
		global DataPath
		conn = sqlite3.connect(DataPath)
		c= conn.cursor()
		c.execute('''SELECT Transac FROM FoodOrder WHERE ID=?''',(self.ID,))
		Val= c.fetchone()
		c.close()
		return Val[0]
	@Transac.setter
	def Transac(self,value):
		global DataPath
		conn = sqlite3.connect(DataPath)
		c= conn.cursor()
		c.execute('''UPDATE FoodOrder SET Transac=? WHERE ID=?''',(value,self.ID))
		c.close()
		conn.commit()
	def TableJson(self):
		r={"ID":self.ID}
		r["FoodIngredent"]=self.FoodIngredent
		r["Transac"]=self.Transac
		return r
	def __str__(self):
		return str(self.TableJson())
