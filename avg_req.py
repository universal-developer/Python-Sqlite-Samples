import pyodbc

try:
	con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\artush\Documents\Code\pydb.accdb;'
	conn = pyodbc.connect(con_string)

	cur = conn.cursor()

	lst = cur.execute("SELECT AVG(IMDB) AS avg FROM Таблица1")

	for row in cur.fetchall():
		print(row.avg)

except pyodbc.Error as e:
	print('Error in connection', e) 