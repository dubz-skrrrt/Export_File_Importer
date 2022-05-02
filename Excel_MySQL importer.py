import mysql.connector
from mysql.connector import Error
from sqlalchemy import create_engine
from tkinter import filedialog
import pandas as pd
import xlrd

def Database(file):
    try:
        df = pd.read_excel(file)
        print(df.head())
        engine = create_engine('mysql://root:qwerty1234@localhost/ExcelFileImporter')
        df.to_sql('personal_detail', con=engine, if_exists='append', index=False)
    except Error as e:
        print("Error while connecting to MySQL", e)

def Converter(file):
    #reading file content
    workbook = xlrd.open_workbook(file)
    worksheet = workbook.sheet_by_index(0)
    for i in range(0, worksheet.ncols):
        for j in range(0, worksheet.nrows):
            print(worksheet.cell_value(i, j), end='\t')
        print('')
def FindFileAction():
    #uploading file
    filename = filedialog.askopenfilename(filetypes =[('Text Files', '*.xls')])
    Converter(filename)
    Database(filename)


FindFileAction()