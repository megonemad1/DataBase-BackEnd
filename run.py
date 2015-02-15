#!flask/bin/python
from DataB import app
from DataB import DataPath
import CheckDb
CheckDb.DataPath=DataPath
CheckDb.Check()
app.run(debug=True,host="0.0.0.0", port=80)

