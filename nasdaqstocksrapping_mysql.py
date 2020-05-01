# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Importing packages
import mysql.connector
from mysql.connector import Error
import yfinance as yf
import pandas
from datetime import datetime, timedelta

# Create a user input to ask users to type in the stock symbol (eg: AMD, EDIT, NVO)
#stock_input = str(input("What stock symbol are you interested in?\n"))
stock_input = 'spy'


#Pulling option data
#opt = stock_data.option_chain('2022-12-15')
#calls = opt.calls

current_date = datetime.today() + timedelta(1)
start_date = current_date - timedelta(1)

current_date_string = str(current_date.year)+'-'+str(current_date.month)+'-'+str(current_date.day)
start_date_string = str(start_date.year)+'-'+str(start_date.month)+'-'+str(start_date.day)


# valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo  default is 1d
stock_data = yf.download(stock_input, interval = '5m', end = current_date_string, start = start_date_string)

# Move index data to 'Datetime' column; remove all other columns but 'Open'
stock_data_essential = stock_data['Open'].reset_index()

# Convert DataFrame to list of tuples
stock_data_essential_tuple = [tuple(r) for r in stock_data_essential.to_numpy()]


# ________________________________SQL______________________________________________
# Save event data to database
# Open database connection
db = mysql.connector.connect(user='root', password='qqqQQQ!!!111',
                             host='127.0.0.1', database='stockprices', use_pure=True)

# prepare a cursor object using cursor() method
#cursor = db.cursor()

# Prepare SQL query to INSERT a record into the database.
sql = "INSERT INTO stockprices(datetime, open) VALUES (%s, %s)"


try:
    if db.is_connected():
        db_Info = db.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = db.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)
    # Execute the SQL command with the required parameters
        cursor.execute(sql, stock_data_essential_tuple)
        print('Cursor Executed')
    # Commit your changes in the database
        db.commit()
        print(cursor.rowcount, "record inserted.")
except:
    # Rollback in case there is any error
    db.rollback()
    # disconnect from server
    db.close()
    print('no')












