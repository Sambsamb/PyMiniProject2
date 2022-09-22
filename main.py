"""
(5) Initial comments with your name, class and project at the top of your .py file:
INF601 - Advanced Programming in Python
Sam Boutros
Mini Project 2
9/22/2022
"""


# (5) Proper import of packages used:
import pandas as pd
import requests
import json


# (20) Using a data source of your choice, retrieve some data
data = requests.get("https://opendata.fcc.gov/resource/bzun-59r8.json")
data.status_code #  200
myjson = data.json()


# (10) Store this information in Pandas dataframe




# (10) Using matplotlib, graph this data in a way that will visually represent the data




# (10) Save these graphs in a folder called charts as PNG files





