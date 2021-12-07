import pyodbc

try:
	con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\artush\Documents\Code\pydb.accdb;'
	conn = pyodbc.connect(con_string)

	cur = conn.cursor()
	lst = cur.execute("SELECT IMDB FROM Таблица1")

	a = []

	for row in cur.fetchall():
		a.append(float(row.IMDB))
	
	print(a)

	avg = sum(a) / len(a)

	print(avg)


except pyodbc.Error as e:
	print('Error in connection', e) 