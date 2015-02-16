#CREATE TABLE IF NOT EXISTS Company (ID integer PRIMARY KEY AUTOINCREMENT, CompanyName text);
#CREATE TABLE IF NOT EXISTS Tutor (ID integer PRIMARY KEY AUTOINCREMENT, TutorGroup integer, Company integer, TutorTeacher text, FOREIGN KEY (Company) REFERENCES Company(ID));
#CREATE TABLE IF NOT EXISTS Customer (ID integer PRIMARY KEY AUTOINCREMENT, CustomerName text, Tutor integer, FOREIGN KEY (Tutor) REFERENCES Tutor(ID));
#CREATE TABLE IF NOT EXISTS Transac (ID integer PRIMARY KEY AUTOINCREMENT, Customer integer, Time timestamp, FOREIGN KEY (Customer) REFERENCES Customer(ID));
#CREATE TABLE IF NOT EXISTS FoodSupplyer (ID integer PRIMARY KEY AUTOINCREMENT, Address text, Tell text, Email text, SupplyerName Text);
#CREATE TABLE IF NOT EXISTS FoodIngredent (ID integer PRIMARY KEY AUTOINCREMENT, Ingredent Name, PricePerUnit integer, Supplyer integer, FOREIGN KEY (Supplyer) REFERENCES FoodSupplyer(ID));
#CREATE TABLE IF NOT EXISTS FoodOrder (ID integer PRIMARY KEY AUTOINCREMENT, FoodIngredent integer, Transac integer, FOREIGN KEY (Transac) REFERENCES Transac(ID), FOREIGN KEY (FoodIngredent) REFERENCES FoodIngredent(ID));
from DataB import DataPath
import sqlite3
class Company:
	def __init__(self,ID):
		"""Company Table Contains columns: CompanyName of type text|| Foreign Keys: """
		conn = sqlite3.connect(DataPath)
		c= conn.cursor()
		c.execute('''SELECT CompanyName FROM Company WHERE ID=?''',ID)
		self.CompanyName=c.fetchone()
class Tutor:
	def __init__(self,ID):
		"""Tutor Table Contains columns: TutorGroup of type integer|| Company of type integer|| TutorTeacher of type text|| Foreign Keys: Tutor.Company refrences Company.ID"""
		conn = sqlite3.connect(DataPath)
		c= conn.cursor()
		c.execute('''SELECT TutorGroup FROM Tutor WHERE ID=?''',ID)
		self.TutorGroup=c.fetchone()
		c.execute('''SELECT Company FROM Tutor WHERE ID=?''',ID)
		self.Company=c.fetchone()
		c.execute('''SELECT TutorTeacher FROM Tutor WHERE ID=?''',ID)
		self.TutorTeacher=c.fetchone()
class Customer:
	def __init__(self,ID):
		"""Customer Table Contains columns: CustomerName of type text|| Tutor of type integer|| Foreign Keys: Customer.Tutor refrences Tutor.ID"""
		conn = sqlite3.connect(DataPath)
		c= conn.cursor()
		c.execute('''SELECT CustomerName FROM Customer WHERE ID=?''',ID)
		self.CustomerName=c.fetchone()
		c.execute('''SELECT Tutor FROM Customer WHERE ID=?''',ID)
		self.Tutor=c.fetchone()
class Transac:
	def __init__(self,ID):
		"""Transac Table Contains columns: Customer of type integer|| Time of type timestamp|| Foreign Keys: Transac.Customer refrences Customer.ID"""
		conn = sqlite3.connect(DataPath)
		c= conn.cursor()
		c.execute('''SELECT Customer FROM Transac WHERE ID=?''',ID)
		self.Customer=c.fetchone()
		c.execute('''SELECT Time FROM Transac WHERE ID=?''',ID)
		self.Time=c.fetchone()
class FoodSupplyer:
	def __init__(self,ID):
		"""FoodSupplyer Table Contains columns: Address of type text|| Tell of type text|| Email of type text|| SupplyerName of type Text|| Foreign Keys: """
		conn = sqlite3.connect(DataPath)
		c= conn.cursor()
		c.execute('''SELECT Address FROM FoodSupplyer WHERE ID=?''',ID)
		self.Address=c.fetchone()
		c.execute('''SELECT Tell FROM FoodSupplyer WHERE ID=?''',ID)
		self.Tell=c.fetchone()
		c.execute('''SELECT Email FROM FoodSupplyer WHERE ID=?''',ID)
		self.Email=c.fetchone()
		c.execute('''SELECT SupplyerName FROM FoodSupplyer WHERE ID=?''',ID)
		self.SupplyerName=c.fetchone()
class FoodIngredent:
	def __init__(self,ID):
		"""FoodIngredent Table Contains columns: Ingredent of type Name|| PricePerUnit of type integer|| Supplyer of type integer|| Foreign Keys: FoodIngredent.Supplyer refrences FoodSupplyer.ID"""
		conn = sqlite3.connect(DataPath)
		c= conn.cursor()
		c.execute('''SELECT Ingredent FROM FoodIngredent WHERE ID=?''',ID)
		self.Ingredent=c.fetchone()
		c.execute('''SELECT PricePerUnit FROM FoodIngredent WHERE ID=?''',ID)
		self.PricePerUnit=c.fetchone()
		c.execute('''SELECT Supplyer FROM FoodIngredent WHERE ID=?''',ID)
		self.Supplyer=c.fetchone()
class FoodOrder:
	def __init__(self,ID):
		"""FoodOrder Table Contains columns: FoodIngredent of type integer|| Transac of type integer|| Foreign Keys: FoodOrder.Transac refrences Transac.IDFoodOrder.FoodIngredent refrences FoodIngredent.ID"""
		conn = sqlite3.connect(DataPath)
		c= conn.cursor()
		c.execute('''SELECT FoodIngredent FROM FoodOrder WHERE ID=?''',ID)
		self.FoodIngredent=c.fetchone()
		c.execute('''SELECT Transac FROM FoodOrder WHERE ID=?''',ID)
		self.Transac=c.fetchone()
