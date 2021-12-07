import pyodbc
 
 
 
try:
    con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\artush\Documents\Code\pydb.accdb;'
    conn = pyodbc.connect(con_string)
 
    user_id = int(input())
 
    cur = conn.cursor()
    cur.execute('DELETE FROM Таблица1 WHERE Код = ?', (user_id))
    conn.commit()
    print("Data Deleted ")

 
 
except pyodbc.Error as e:
    print("Error in connection", e)