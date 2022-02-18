import mysql.connector

dbconfig = {'host': '127.0.0.1',
            'user': 'root',
            'password': 'root',
            'database': 'sakila'
            }

try:
    connection = mysql.connector.connect(**dbconfig)
    with connection as conn:
        cursor = conn.cursor()
        cursor.execute("select version()")
        version = cursor.fetchone()
        print(f"Database version: {version}")
except Exception as ex:
    print('It went out of our control')
    print(ex)
