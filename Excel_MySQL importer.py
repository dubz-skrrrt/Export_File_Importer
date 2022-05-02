import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb
import xlrd

database = MySQLdb.connect(host="localhost", user="root", passwd="qwerty1234", db="mysql")
cursor = database.cursor()
