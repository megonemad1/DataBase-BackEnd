from flask import Flask
app = Flask(__name__)
DataPath = "FoodDataBase.db"
SchemaPath = "Schema.py"
Folder=""
from DataB import Main_Views
#