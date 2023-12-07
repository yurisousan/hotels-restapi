import sqlite3

connection = sqlite3.connect('base.db')
cursor = connection.cursor()

create_table = "CREATE TABLE IF NOT EXISTS hotels (\
    hotel_id text PRIMARY_KEY, name text, stars real, diary real, city text)"

create_hotel = "INSERT INTO hotels VALUES (\
    'alpha', 'Alpha Hotel', 4.3, 500.00, 'Sao Paulo')"

cursor.execute(create_table)
cursor.execute(create_hotel)

connection.commit()
connection.close()
