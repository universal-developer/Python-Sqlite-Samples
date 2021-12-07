#Insert some data in file

import pyodbc

try: 

    con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\artush\Documents\Code\pydb.accdb;'
    conn = pyodbc.connect(con_string)

    cursor = conn.cursor()

    ask_user_number = int(input("Введите номер: "))
    ask_user_title = str(input("Введите название: "))
    ask_user_rite_1 = float(input("Введите оценку для IMDB: "))
    ask_user_rite_2 = float(input("Введите оценку для KP: "))
    ask_user_age_limit = str(input("Введите возрастное ограничение: "))
    ask_user_genre = int(input("Введите цифру для жанра: ")) 
    ask_user_date = int(input("Введите дату релиза: "))

    my_user = (

    	(ask_user_number, ask_user_title, ask_user_rite_1, ask_user_rite_2, ask_user_age_limit, ask_user_genre, ask_user_date),

    	)


    cursor.executemany('INSERT INTO Таблица1 VALUES (?,?,?,?,?,?,?)', my_user)
    conn.commit()
    print('Data Insearted')

except pyodbc.Error as e:
	print('Error in connection', e)