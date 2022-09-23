"""
(5) Initial comments with your name, class and project at the top of your .py file:
INF601 - Advanced Programming in Python
Sam Boutros
Mini Project 2
9/22/2022
"""


#region (5) Proper import of packages used:
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf
import datetime as dt
import os
import pandas as pd
import requests
import json
#endregion

#region Input and Initialize

statelist = ['NJ', 'KS', 'FL', 'CA', 'NY']
datasourceurl = 'https://api.covidtracking.com/v1/states/xx/daily.json'

if not os.path.exists('charts'):
    os.makedirs('charts')

#endregion

#region (20) Using a data source of your choice, retrieve some data, (10) Store this information in Pandas dataframe

for state in statelist:
    stateurl = datasourceurl.replace('xx', state.lower())
    print(f'Working with API URL {stateurl}')
    # Putting in some error handling
    try:
        json_data = requests.get(stateurl)
        if json_data.status_code == 200:
            print(f'    Received API data')
        else:
            print(f'    Received no API data, stopping')
            print(f'    Details: {json_data}')
            exit(1)
    except ValueError as ve:
        print(f'    Error detail: {ve}')
        exit(1)


    state_data = pd.read_json(stateurl)
    # df.to_excel('Covid_' + state + '.xlsx')

    state_data = state_data[state_data['date'] > 20200301]  # Get only dates after  3/1/2020
    state_data = state_data[state_data['date'] < 20210302]  # Get only dates before 3/2/2021
    state_data.sort_values('date', ascending=False)
    state_data = state_data[['deathIncrease']]  # Get only these 1 column

    # (10) Plot the graph
    plt.plot(state_data)
    title = 'Daily Covid deaths delta in the state of ' + state
    plt.title(title, fontsize=13)
    plt.xlabel('Day (3/1/2020 to 3/1/2021)')
    plt.ylabel('Covid deaths delta')
    plt.grid()
    plt.savefig('charts/Covid_Deaths_Delta_March2020_March2021_' + state + '.png')
    plt.show()
"""
# Plot improvements
    title = "Adjusted closing price of " + state + " stock in the past " + str(countOfDays) + " days"
    plt.title(title, fontsize=13)
    plt.xlabel('Day')
    plt.ylabel('Price ($)')
    plt.grid()
# (10) Save the graph in a folder called charts as PNG file
    plt.savefig('charts/' + state + '.png')
    # plt.show()
    # print()

print()  # Blank line
print("Collecting the closing price of the following", len(myStockList), "stock tickers for the last", countOfDays,
      "trading days:")
print()


"""
#endregion


# (10) Using matplotlib, graph this data in a way that will visually represent the data




# (10) Save these graphs in a folder called charts as PNG files





