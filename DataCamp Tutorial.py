# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 18:56:51 2019

@author: Tyler H
"""

from pandas_datareader import data
import pandas as pd
import datetime
import quandl

#tsla = data.DataReader('TSLA', 'yahoo',
#                       end = datetime.time)

aapl = data.DataReader('AAPL', 'yahoo',
                          start = datetime.datetime(2006, 10, 1),
                          end = datetime.datetime(2012, 1, 1))


# Import Data from Google Finance for Apple Stock
aapl = quandl.get("WIKI/AAPL", start_date = "2006-10-01", end_date = "2012-01-01")

# Collect first five rows of data, last five rows of data, and basic statistics of data
head = aapl.head()
tail = aapl.tail()
describe = aapl.describe()

# Save data to a csv file - In case lose to database occurs
aapl.to_csv(r'C:\Users\Tyler H\Documents\GitHub\financial_modeling\aapl_ohlc.csv')
df = pd.read_csv(r'C:\Users\Tyler H\Documents\GitHub\financial_modeling\aapl_ohlc.csv', header=0, index_col='Date', parse_dates=True)


index = aapl.index
columns = aapl.columns
ts = aapl['Close'][-10:]

"""
# Pandas Practice
print(aapl.loc[pd.Timestamp('2006-11-01'):pd.Timestamp('2006-12-31')].head())
"""







