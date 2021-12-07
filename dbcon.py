#Connecting to database

import pyodbc
 
try:
    con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\artush\Documents\Code\pydb.accdb;'
    conn = pyodbc.connect(con_string)
    print("Connected To Database")
 
 
 
except pyodbc.Error as e:
    print("Error in Connection", e)