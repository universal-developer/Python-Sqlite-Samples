import pyodbc

try:
	con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\artush\Documents\Code\pydb.accdb;'
	conn = pyodbc.connect(con_string)

	cur = conn.cursor()
	first__number = 2000 
	second__number = 2020 
	cur.execute(f"SELECT Год FROM Таблица1 WHERE Год >= {first__number} AND ГОД <= {second__number}")
	
	for row in cur.fetchall():
		print('Названия фильмов с этим жанром: ', row)

except pyodbc.Error as e:
	print('Error in connection', e) 