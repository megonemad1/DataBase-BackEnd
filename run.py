#!flask/bin/python
import CheckDb
print("checking")
CheckDb.Check()

from DataB import app
app.run(debug=True,port=80)

