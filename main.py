"""
(5) Initial comments with your name, class and project at the top of your .py file:
INF601 - Advanced Programming in Python
Sam Boutros
Mini Project 2
9/23/2022
"""


#region (5) Proper import of packages used:
import matplotlib.pyplot as plt
import os
import pandas as pd
import requests
import matplotlib.dates as mdates
from matplotlib.dates import MO, TU, WE, TH, FR, SA, SU
#endregion


#region Input and Initialize

statelist = ['NJ', 'KS', 'FL', 'CA', 'NY']
startdate = 20210101
enddate = 20210201
datasourceurl = 'https://api.covidtracking.com/v1/states/xx/daily.json'
combined = pd.DataFrame()  # Empty dataframe

if not os.path.exists('charts'): os.makedirs('charts')
if not os.path.exists('excel'):  os.makedirs('excel')

#endregion


#region (20) Using a data source of your choice, retrieve some data:

for state in statelist:
    stateurl = datasourceurl.replace('xx', state.lower())
    print(f'Working with API URL {stateurl}')
    # Putting in some error handling
    try:
        response = requests.get(stateurl)
        if response.status_code == 200:
            print(f'    Received API data')
        else:
            print(f'    Received no API data, stopping')
            print(f'    Details: {response}')
            exit(1)
    except ValueError as ve:
        print(f'    Error detail: {ve}')
        exit(1)

    # (10) Store this information in Pandas dataframe
    state_data = pd.read_json(stateurl)
    # Save to Excel
    filename = 'excel/covid_' + state + '.xlsx'
    state_data.to_excel(filename)
    print(f'    Saved data to {filename}')

    state_data = state_data[state_data['date'] > startdate]  # Get only dates after startdate
    state_data = state_data[state_data['date'] < enddate]  # Get only dates before enddate
    state_data = state_data.sort_values('date', ascending=True)  # Sort by date from old to new
    state_data['str_date'] = pd.to_datetime(state_data['date'].astype(str), format='%Y%m%d')  # Add new column - date as string
    combined[state] = state_data[['deathIncrease']]  # Build/add column to the final combined dataframe

    # (10) Using matplotlib, graph this data
    fig, ax = plt.subplots(1, figsize=(6.4, 4.8), constrained_layout=True)
    ax.plot('str_date', 'deathIncrease', data=state_data, label=state)
    ax.set_title('Daily Covid deaths delta in the state of ' + state, fontsize=13)
    ax.set_ylabel('Covid deaths delta')
    # Major ticks every Monday, minor ticks every day,
    ax.xaxis.set_major_locator(mdates.WeekdayLocator(byweekday=MO))
    ax.xaxis.set_minor_locator(mdates.DayLocator())
    # Display text in the x-axis in 'yy-mmm-dd' format:
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%y-%b-%d'))
    # Right-align and rotate and the x labels 30 degrees, so they don't crowd each other:
    for label in ax.get_xticklabels(which='major'):
        label.set(rotation=30, horizontalalignment='right')
    ax.grid(True)
    # (10) Save these graphs in a folder called charts as PNG files
    filename = 'charts/Covid_Deaths_Delta_' + \
               str(startdate)[0:4] + '-' + str(startdate)[4:6] + '-' + str(startdate)[6:8] + '_to_' + \
               str(enddate)[0:4] + '-' + str(enddate)[4:6] + '-' + str(enddate)[6:8] + '_' + state + '.png'
    plt.legend()
    plt.savefig(filename)
    print(f'    Saved graph to {filename}')
    plt.show()

# Plot the final combined graph
plt.plot(combined, label=combined.columns)
title = 'Daily Covid deaths delta in the ' + ', '.join(statelist) + ' states'
plt.title(title, fontsize=13)
xlabel = 'Day (' + str(startdate)[0:4] + '-' + str(startdate)[4:6] + '-' + str(startdate)[6:8] + ' to ' + \
         str(enddate)[0:4] + '-' + str(enddate)[4:6] + '-' + str(enddate)[6:8] + ')'
plt.xlabel(xlabel)
plt.ylabel('Covid deaths delta')
plt.grid()
filename = 'charts/Covid_Deaths_Delta_' + str(startdate) + '_to_' + str(enddate) + '_' + str(len(statelist)) + 'States.png'
plt.legend()
plt.savefig(filename)
print(f'    Saved combined graph to {filename}')
plt.show()

#endregion
