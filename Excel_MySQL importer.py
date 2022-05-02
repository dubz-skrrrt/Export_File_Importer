import mysql.connector
from mysql.connector import Error
import xlrd


try:
    connection = mysql.connector.connect(host="localhost",
                                         database="ExcelImporter",
                                         user="root",
                                         password="qwerty1234")
    if connection.is_connected():
        db_info = connection.get_server_info()
        print("Connected to MySQL server version ", db_info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)
except Error as e:
    print("Error while connecting to MySQL", e)

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()

#personal_details_table = "CREATE TABLE IF NOT EXISTS personal_details(id int)"