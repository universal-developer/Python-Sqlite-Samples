#Insert some data in file

import pyodbc
import random as r

try: 

    con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\artush\Documents\Code\pydb.accdb;'
    conn = pyodbc.connect(con_string)

    cursor = conn.cursor()

    count = cursor.execute('SELECT * FROM Таблица1')
    #8,9

    j = []

    for row in cursor.fetchall():
        cur = conn.cursor()
        a = r.randint(1000000, 1000000000)
        
        cur.execute(f"UPDATE Таблица1 SET Доллары = {a} WHERE Код = {row.Код}")  

    conn.commit()
    print('Data Insearted')

except pyodbc.Error as e:
	print('Error in connection', e)