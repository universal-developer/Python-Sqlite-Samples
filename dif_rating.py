import pyodbc

try:
	con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\artush\Documents\Code\pydb.accdb;'
	conn = pyodbc.connect(con_string)

	cur = conn.cursor()
	cur.execute('SELECT IMDB - KP as rate FROM Таблица1')

	lst = []
	
	for row in cur.fetchall():
		lst.append(row.rate)

	print(max(lst))

except pyodbc.Error as e:
	print('Error in connection', e) 