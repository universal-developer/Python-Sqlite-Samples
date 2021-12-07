import pyodbc

try:
	con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\artush\Documents\Code\pydb.accdb;'
	conn = pyodbc.connect(con_string)

	input__name = int(input())

	cur = conn.cursor()
	cur.execute('SELECT Название FROM Таблица1 WHERE Жанр = ?', (input__name))
	
	for row in cur.fetchall():
		print('Названия фильмов с этим жанром: ', row)

except pyodbc.Error as e:
	print('Error in connection', e) 