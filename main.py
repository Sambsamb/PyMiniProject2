"""
(5) Initial comments with your name, class and project at the top of your .py file:
INF601 - Advanced Programming in Python
Sam Boutros
Mini Project 2
9/22/2022
"""


#region (5) Proper import of packages used:
import pandas as pd
import requests
import json
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


# test


# (10) Using matplotlib, graph this data in a way that will visually represent the data




# (10) Save these graphs in a folder called charts as PNG files





