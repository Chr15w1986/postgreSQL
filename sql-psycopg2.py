import psycopg2

# connect to the "chinook" database

connection = psycopg2.connect(database="chinook")

cursor = connection.cursor()

results = cursor.fetchall()

