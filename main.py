import mysql.connector
from os import path
from config import *
from datetime import datetime

time = datetime.now()


def to_log(message, special=None):
    with open(log_name, "a") as f:
        f.write(str(time) + '\t' + str(message) + '\n')


if not path.isfile(log_name):
    with open(log_name, "w") as f:
            f.write(str(time) + '\t' + 'Setup initialized' + '\n')
else:
    to_log('\n')
    to_log(messages['start'])
try:
    connection = mysql.connector.connect(**c)
    to_log(messages['con'])
    with connection as conn:
        cursor = conn.cursor()
        cursor.execute("SET time_zone = '+03:00'")
        query = f"insert into {table} values (Null, CURDATE(), CURTIME())"
        cursor.execute(query)
        connection.commit()
        cursor.close()
        connection.close()
except Exception as ex:
    to_log(messages['fall'])
    print(ex)
to_log(messages['close'])
