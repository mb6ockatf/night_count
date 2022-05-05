import mysql.connector
from logging import basicConfig, DEBUG, info, error
from datetime import datetime as dt

time = dt.now
basicConfig(filename='general.log', filemode='w', encoding='utf-8',
            level=DEBUG)
config = {'host': '127.0.0.1', 'user': 'root', 'password': 'root',
          'database': 'night_count'}
try:
    connection = mysql.connector.connect(**config)
    info('database connected')
    with connection as conn:
        cursor = conn.cursor()
        cursor.execute("SET time_zone = '+03:00'")
        query = f"insert into {'nightcount'} values (Null, CURDATE(), " \
                f"CURTIME())"
        cursor.execute(query)
        connection.commit()
        cursor.close()
        connection.close()
except Exception as ex:
    error('!' + str(ex))
info('exit')
