#CREATE TABLE IF NOT EXISTS Company (ID integer PRIMARY KEY AUTOINCREMENT, CompanyName text);
#CREATE TABLE IF NOT EXISTS Tutor (ID integer PRIMARY KEY AUTOINCREMENT, Company integer, TutorTeacher text, TutorGroup integer, FOREIGN KEY (Company) REFERENCES Company(ID));
#CREATE TABLE IF NOT EXISTS Customer (ID integer PRIMARY KEY AUTOINCREMENT, Tutor integer, CustomerName text, FOREIGN KEY (Tutor) REFERENCES Tutor(ID));
#CREATE TABLE IF NOT EXISTS Transac (ID integer PRIMARY KEY AUTOINCREMENT, Time timestamp, Customer integer, FOREIGN KEY (Customer) REFERENCES Customer(ID));
#CREATE TABLE IF NOT EXISTS FoodSupplyer (ID integer PRIMARY KEY AUTOINCREMENT, SupplyerName Text, Tell text, Email text, Address text);
#CREATE TABLE IF NOT EXISTS FoodIngredent (ID integer PRIMARY KEY AUTOINCREMENT, Ingredent Name, PricePerUnit integer, Supplyer integer, FOREIGN KEY (Supplyer) REFERENCES FoodSupplyer(ID));
#CREATE TABLE IF NOT EXISTS FoodOrder (ID integer PRIMARY KEY AUTOINCREMENT, Transac integer, FoodIngredent integer, FOREIGN KEY (Transac) REFERENCES Transac(ID), FOREIGN KEY (FoodIngredent) REFERENCES FoodIngredent(ID));
from DataB import DataPath
import sqlite3
class Company:
	def __init__(self,ID):
		"""Company Table Contains columns: CompanyName of type text|| Foreign Keys: """
		self.ID=ID
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
		return Val
	@CompanyName.setter
	def CompanyName(self,value):
		global DataPath
		conn = sqlite3.connect(DataPath)
		c= conn.cursor()
		c.execute('''UPDATE CompanyName SET Company=? WHERE ID=?''',(value,self.ID))
		c.close()
		conn.commit()
class Tutor:
	def __init__(self,ID):
		"""Tutor Table Contains columns: Company of type integer|| TutorTeacher of type text|| TutorGroup of type integer|| Foreign Keys: Tutor.Company refrences Company.ID"""
		self.ID=ID
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
	def Company(self):
		global DataPath
		conn = sqlite3.connect(DataPath)
		c= conn.cursor()
		c.execute('''SELECT Company FROM Tutor WHERE ID=?''',(self.ID,))
		Val= c.fetchone()
		c.close()
		return Val
	@Company.setter
	def Company(self,value):
		global DataPath
		conn = sqlite3.connect(DataPath)
		c= conn.cursor()
		c.execute('''UPDATE Company SET Tutor=? WHERE ID=?''',(value,self.ID))
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
		return Val
	@TutorTeacher.setter
	def TutorTeacher(self,value):
		global DataPath
		conn = sqlite3.connect(DataPath)
		c= conn.cursor()
		c.execute('''UPDATE TutorTeacher SET Tutor=? WHERE ID=?''',(value,self.ID))
		c.close()
		conn.commit()
	@property
	def TutorGroup(self):
		global DataPath
		conn = sqlite3.connect(DataPath)
		c= conn.cursor()
		c.execute('''SELECT TutorGroup FROM Tutor WHERE ID=?''',(self.ID,))
		Val= c.fetchone()
		c.close()
		return Val
	@TutorGroup.setter
	def TutorGroup(self,value):
		global DataPath
		conn = sqlite3.connect(DataPath)
		c= conn.cursor()
		c.execute('''UPDATE TutorGroup SET Tutor=? WHERE ID=?''',(value,self.ID))
		c.close()
		conn.commit()
class Customer:
	def __init__(self,ID):
		"""Customer Table Contains columns: Tutor of type integer|| CustomerName of type text|| Foreign Keys: Customer.Tutor refrences Tutor.ID"""
		self.ID=ID
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
	def Tutor(self):
		global DataPath
		conn = sqlite3.connect(DataPath)
		c= conn.cursor()
		c.execute('''SELECT Tutor FROM Customer WHERE ID=?''',(self.ID,))
		Val= c.fetchone()
		c.close()
		return Val
	@Tutor.setter
	def Tutor(self,value):
		global DataPath
		conn = sqlite3.connect(DataPath)
		c= conn.cursor()
		c.execute('''UPDATE Tutor SET Customer=? WHERE ID=?''',(value,self.ID))
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
		return Val
	@CustomerName.setter
	def CustomerName(self,value):
		global DataPath
		conn = sqlite3.connect(DataPath)
		c= conn.cursor()
		c.execute('''UPDATE CustomerName SET Customer=? WHERE ID=?''',(value,self.ID))
		c.close()
		conn.commit()
class Transac:
	def __init__(self,ID):
		"""Transac Table Contains columns: Time of type timestamp|| Customer of type integer|| Foreign Keys: Transac.Customer refrences Customer.ID"""
		self.ID=ID
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
	def Time(self):
		global DataPath
		conn = sqlite3.connect(DataPath)
		c= conn.cursor()
		c.execute('''SELECT Time FROM Transac WHERE ID=?''',(self.ID,))
		Val= c.fetchone()
		c.close()
		return Val
	@Time.setter
	def Time(self,value):
		global DataPath
		conn = sqlite3.connect(DataPath)
		c= conn.cursor()
		c.execute('''UPDATE Time SET Transac=? WHERE ID=?''',(value,self.ID))
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
		return Val
	@Customer.setter
	def Customer(self,value):
		global DataPath
		conn = sqlite3.connect(DataPath)
		c= conn.cursor()
		c.execute('''UPDATE Customer SET Transac=? WHERE ID=?''',(value,self.ID))
		c.close()
		conn.commit()
class FoodSupplyer:
	def __init__(self,ID):
		"""FoodSupplyer Table Contains columns: SupplyerName of type Text|| Tell of type text|| Email of type text|| Address of type text|| Foreign Keys: """
		self.ID=ID
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
	def SupplyerName(self):
		global DataPath
		conn = sqlite3.connect(DataPath)
		c= conn.cursor()
		c.execute('''SELECT SupplyerName FROM FoodSupplyer WHERE ID=?''',(self.ID,))
		Val= c.fetchone()
		c.close()
		return Val
	@SupplyerName.setter
	def SupplyerName(self,value):
		global DataPath
		conn = sqlite3.connect(DataPath)
		c= conn.cursor()
		c.execute('''UPDATE SupplyerName SET FoodSupplyer=? WHERE ID=?''',(value,self.ID))
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
		return Val
	@Tell.setter
	def Tell(self,value):
		global DataPath
		conn = sqlite3.connect(DataPath)
		c= conn.cursor()
		c.execute('''UPDATE Tell SET FoodSupplyer=? WHERE ID=?''',(value,self.ID))
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
		return Val
	@Email.setter
	def Email(self,value):
		global DataPath
		conn = sqlite3.connect(DataPath)
		c= conn.cursor()
		c.execute('''UPDATE Email SET FoodSupplyer=? WHERE ID=?''',(value,self.ID))
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
		return Val
	@Address.setter
	def Address(self,value):
		global DataPath
		conn = sqlite3.connect(DataPath)
		c= conn.cursor()
		c.execute('''UPDATE Address SET FoodSupplyer=? WHERE ID=?''',(value,self.ID))
		c.close()
		conn.commit()
class FoodIngredent:
	def __init__(self,ID):
		"""FoodIngredent Table Contains columns: Ingredent of type Name|| PricePerUnit of type integer|| Supplyer of type integer|| Foreign Keys: FoodIngredent.Supplyer refrences FoodSupplyer.ID"""
		self.ID=ID
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
	def Ingredent(self):
		global DataPath
		conn = sqlite3.connect(DataPath)
		c= conn.cursor()
		c.execute('''SELECT Ingredent FROM FoodIngredent WHERE ID=?''',(self.ID,))
		Val= c.fetchone()
		c.close()
		return Val
	@Ingredent.setter
	def Ingredent(self,value):
		global DataPath
		conn = sqlite3.connect(DataPath)
		c= conn.cursor()
		c.execute('''UPDATE Ingredent SET FoodIngredent=? WHERE ID=?''',(value,self.ID))
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
		return Val
	@PricePerUnit.setter
	def PricePerUnit(self,value):
		global DataPath
		conn = sqlite3.connect(DataPath)
		c= conn.cursor()
		c.execute('''UPDATE PricePerUnit SET FoodIngredent=? WHERE ID=?''',(value,self.ID))
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
		return Val
	@Supplyer.setter
	def Supplyer(self,value):
		global DataPath
		conn = sqlite3.connect(DataPath)
		c= conn.cursor()
		c.execute('''UPDATE Supplyer SET FoodIngredent=? WHERE ID=?''',(value,self.ID))
		c.close()
		conn.commit()
class FoodOrder:
	def __init__(self,ID):
		"""FoodOrder Table Contains columns: Transac of type integer|| FoodIngredent of type integer|| Foreign Keys: FoodOrder.Transac refrences Transac.IDFoodOrder.FoodIngredent refrences FoodIngredent.ID"""
		self.ID=ID
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
	def Transac(self):
		global DataPath
		conn = sqlite3.connect(DataPath)
		c= conn.cursor()
		c.execute('''SELECT Transac FROM FoodOrder WHERE ID=?''',(self.ID,))
		Val= c.fetchone()
		c.close()
		return Val
	@Transac.setter
	def Transac(self,value):
		global DataPath
		conn = sqlite3.connect(DataPath)
		c= conn.cursor()
		c.execute('''UPDATE Transac SET FoodOrder=? WHERE ID=?''',(value,self.ID))
		c.close()
		conn.commit()
	@property
	def FoodIngredent(self):
		global DataPath
		conn = sqlite3.connect(DataPath)
		c= conn.cursor()
		c.execute('''SELECT FoodIngredent FROM FoodOrder WHERE ID=?''',(self.ID,))
		Val= c.fetchone()
		c.close()
		return Val
	@FoodIngredent.setter
	def FoodIngredent(self,value):
		global DataPath
		conn = sqlite3.connect(DataPath)
		c= conn.cursor()
		c.execute('''UPDATE FoodIngredent SET FoodOrder=? WHERE ID=?''',(value,self.ID))
		c.close()
		conn.commit()
