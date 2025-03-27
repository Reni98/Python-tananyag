import mysql.connector
from mysql.connector import Error

try:
    conn = mysql.connector.connect(host='localhost',
                                   database = 'users',
                                   user='root',
                                   password='')
    print("Az adatbázis csatlakozás sikeres volt.")
except Error as e:

    print("Hiba lépet fel a csatlakozáskor.", e)