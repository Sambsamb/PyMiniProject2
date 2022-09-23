# 9/20/2022 - INF601 - Advanced Python - Pandas class - Week 5
# pip install -r requirements.txt
# requirements.txt ==> pandas>=1.5.0, openpyxl>=3.0.10, Faker>=14.2.0, requests>=2.28.1

import pandas as pd
import numpy as np
import multitasking
import requests
import json
import yfinance as yf
import datetime as dt
import matplotlib.pyplot as plt

#region Manual creation of DF:
df = pd.DataFrame(
    {
        'Name': [
            'Braund, Mr. Owen Harris',
            'Allen, Mr. William Henry',
            'Bonnell, Miss. Elizabeth',
        ],
        'Age': [22, 35, 58],
        'Sex': ['male', 'male', 'female'],
    }
)

# Out to Excel:
df.to_excel('Sample1.xlsx', sheet_name='passengers', index=False)

#endregion

#region Get JSON data from FCC website
data = requests.get('https://opendata.fcc.gov/resource/bzun-59r8.json')
data.status_code #  200
myjson = data.json()
print(myjson)
#endregion

#region yfinance testing - Ref: https://algotrading101.com/learn/yfinance-guide/
apple = yf.Ticker('aapl')
apple.actions  # show actions (dividends, splits)
apple.dividends  # show dividends
apple.splits  # show splits
enddate = dt.date.today()
startdate = enddate + dt.timedelta(days=-5)
apple_historical = apple.history(start=startdate, end=enddate, interval='1m')
# Remove timezone from columns
apple_historical['Datetime'] = apple_historical['Datetime'].dt.tz_localize(None)  # ==> KeyError: 'Datetime'
apple_historical.to_excel('apple_historical1.xlsx')
# ValueError: Excel does not support datetimes with timezones. Please ensure that datetimes are timezone unaware before writing to Excel.

# Pulling multiple tickers in one call
enddate = dt.date.today()
startdate = enddate + dt.timedelta(days=-5)
data = yf.download('AMZN AAPL GOOG', start=(dt.date.today() + dt.timedelta(days=-5)), end=dt.date.today())
data

#
tickers_list = ['aapl', 'goog', 'amzn', 'BAC', 'BA']  # example list
tickers_data = {}  # empty dictionary
for ticker in tickers_list:
    ticker_object = yf.Ticker(ticker)
    # convert info() output from dictionary to dataframe
    temp = pd.DataFrame.from_dict(ticker_object.info, orient='index')
    temp.reset_index(inplace=True)
    temp.columns = ['Attribute', 'Recent']
    # add (ticker, dataframe) to main dictionary
    tickers_data[ticker] = temp
# Combine this dictionary of dataframes into a single dataframe
combined_data = pd.concat(tickers_data)
combined_data = combined_data.reset_index()
# Delete the unnecessary level_1 column and clean up the column names:
combined_data = combined_data.drop(columns = ['level_1'])
combined_data.columns = ['Ticker', 'Attribute', 'Recent']
# Build a table of fullTimeEmployees count
employees = combined_data[combined_data['Attribute'] == 'fullTimeEmployees'].reset_index()
employees = employees.drop(columns = ['index', 'Attribute'])
employees.columns = ['Ticker', 'fullTimeEmployees']
employees = employees.sort_values('fullTimeEmployees', ascending=False)
myNumPyArray = np.array(employees)
    plt.plot(myNumPyArray)
# Plot improvements
    title = 'Full time employees'
    plt.title(title, fontsize=13)
    plt.xlabel('Day')
    plt.ylabel('Price ($)')
    plt.grid()
# (10) Save the graph in a folder called charts as PNG file
    plt.savefig('charts/' + stock + '.png')
    plt.show()
    print()

#endregion


#region (20) Using a data source of your choice, retrieve some data, (10) Store this information in Pandas dataframe

# First we retrieve JSON data into a 2-dimensional dataframe
datasourceurl = "https://opendata.fcc.gov/resource/bzun-59r8.json"
df = pd.read_json(datasourceurl)  # <class 'pandas.core.frame.DataFrame'>

# Viewing the data shows that the column labels are not user-friendly. For example:
# for column in df.columns: print(column, end=", ")
# Shows that column labels are:
# hoconum, tech, d_1, d_2, d_3, d_4, d_5, d_6, d_7, d_8, u_1, u_2, u_3, u_4, u_5, u_6, u_7, u_8, u_9
# Explanation is provided at https://opendata.fcc.gov/Wireline/Provider-Table-June-2020-Status-V2/bzun-59r8
# So Next, I update the column names to a more user-friendly names:
df.rename(columns={
    "hoconum": "Provider Id",
    "d_1": "Down200K",
    "d_2": "Down4M",
    "d_3": "Down10M",
    "d_4": "Down10M",
    "d_5": "Down100M",
    "d_6": "Down250M",
    "d_7": "Down500M",
    "d_8": "Down1G",
    "u_1": "Up200K",
    "u_2": "Up1M",
    "u_3": "Up3M",
    "u_4": "Up10M",
    "u_5": "Up25M",
    "u_6": "Up100M",
    "u_7": "Up250M",
    "u_8": "Up500M",
    "u_9": "Up1G",
})



#endregion