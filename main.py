import pymysql

try:
    print(pymysql)
except Exception as ex:
    print('It went out of our control')
    print(ex)
