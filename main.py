import mysql.connector
from os import path
from config import *
from datetime import datetime

time = datetime.now()


def to_log(message, special=None):
    if special == "init":
        with open(log_name, "w") as f:
            f.write(str(time) + '\t' + message + '\n')
    else:
        f = open(log_name, "a")
        f.write(str(time) + '\t' + str(message) + '\n')
        f.close()


def create_log_file():
    to_log('Setup initialized', "init")


if not path.isfile(log_name):
    create_log_file()
else:
    to_log('\n')
    to_log(log_messages['start'])
try:
    connection = mysql.connector.connect(**dbconfig)
    to_log(log_messages['connect'])
    with connection as conn:
        cursor = conn.cursor()
        cursor.execute("SET time_zone = '+03:00'")
        query = f"insert into {table} values (Null, CURDATE(), CURTIME())"
        cursor.execute(query)
        connection.commit()
        cursor.close()
        connection.close()
except Exception as ex:
    to_log(log_messages['con_fall'])
    print(ex)
to_log(log_messages['close'])
