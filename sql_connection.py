
import datetime
import mysql.connector
__cnx = None
def get_sql_connection():
    print("Opening mysql connection")
    global __cnx
    if __cnx is None:
        __cnx = mysql.connector.connect(user='root', password='use your password',
                                      host='localhost',port='3307',
                                      database='grocery_store')

    return __cnx



