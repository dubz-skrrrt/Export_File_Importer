import mysql.connector
from mysql.connector import Error
import xlrd


try:
    connection = mysql.connector.connect(host="localhost",
                                         database="ExcelFileImporter",
                                         user="root",
                                         password="qwerty1234")
    if connection.is_connected():
        db_info = connection.get_server_info()
        print("Connected to MySQL server version ", db_info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)

        personal_details_table_Query = """CREATE TABLE IF NOT EXISTS personal_details (Id int(11) NOT NULL,
                                                                        photo varchar(250) NOT NULL,
                                                                        fname varchar(250) NOT NULL,
                                                                        mname varchar(250) NOT NULL,
                                                                        lname varchar(250) NOT NULL,
                                                                        member_since DATE NOT NULL,
                                                                        reg_data DATE NOT NULL,
                                                                        exp_data DATE NOT NULL,
                                                                        is_active int(5) NOT NULL,
                                                                        PRIMARY KEY (Id)) """
        result = cursor.execute(personal_details_table_Query)
        print("Personal Details Table created successfully ")
except Error as e:
    print("Error while connecting to MySQL", e)

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()

#personal_details_table = "CREATE TABLE IF NOT EXISTS personal_details(id int)"