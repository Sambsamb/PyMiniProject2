# Mini Project 2
>INF601 - Advanced Programming in Python
> 
>Sam Boutros
> 
>FHSU - Fall 2022
>
>9/23/2022
> 
This mini project collects Covid 19 data from the Covid Tracking Project APIs at https://covidtracking.com/data/api. It saves the data in Excel files and plots the deaths delta in 5 US States during January 2021. 

The packages required for main.py are in the requirements.txt file.

To install these packages use:
```python
pip install -r requirements.txt
```
The list of States is defined in the "Input and Initialize" region line 22 and can be changed as desired:
```python
statelist = ['NJ', 'KS', 'FL', 'CA', 'NY']
```
The days to graph are defined in lines 23 and 24 similar to the following format:
```python
startdate = 20210101
enddate = 20210201
```
The script writes progress information to the console similar to
```python
Working with API URL https://api.covidtracking.com/v1/states/nj/daily.json
    Received API data
    Saved data to excel/covid_NJ.xlsx
    Saved graph to charts/Covid_Deaths_Delta_2021-01-01_to_2021-02-01_NJ.png
Working with API URL https://api.covidtracking.com/v1/states/ks/daily.json
    Received API data
    Saved data to excel/covid_KS.xlsx
    Saved graph to charts/Covid_Deaths_Delta_2021-01-01_to_2021-02-01_KS.png
Working with API URL https://api.covidtracking.com/v1/states/fl/daily.json
    Received API data
    Saved data to excel/covid_FL.xlsx
    Saved graph to charts/Covid_Deaths_Delta_2021-01-01_to_2021-02-01_FL.png
Working with API URL https://api.covidtracking.com/v1/states/ca/daily.json
    Received API data
    Saved data to excel/covid_CA.xlsx
    Saved graph to charts/Covid_Deaths_Delta_2021-01-01_to_2021-02-01_CA.png
Working with API URL https://api.covidtracking.com/v1/states/ny/daily.json
    Received API data
    Saved data to excel/covid_NY.xlsx
    Saved graph to charts/Covid_Deaths_Delta_2021-01-01_to_2021-02-01_NY.png
    Saved combined graph to charts/Covid_Deaths_Delta_20210101_to_20210201_5States.png
```

The script saves the PNG images to /charts folder. It creates the folder if it did not exist. 

The script also saves the Excel files to /excel folder. It creates the folder if it did not exist. 