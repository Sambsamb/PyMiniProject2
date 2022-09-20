# 9/20/2022 - INF601 - Advanced Python - Pandas class - Week 5
# pip install -r requirements.txt
# requirements.txt ==> pandas>=1.5.0, openpyxl>=3.0.10, Faker>=14.2.0, requests>=2.28.1

import pandas as pd
import requests
import json

# Manual creation of DF:
df = pd.DataFrame(
    {
        "Name": [
            "Braund, Mr. Owen Harris",
            "Allen, Mr. William Henry",
            "Bonnell, Miss. Elizabeth",
        ],
        "Age": [22, 35, 58],
        "Sex": ["male", "male", "female"],
    }
)

# Out to Excel:
df.to_excel("Sample1.xlsx", sheet_name="passengers", index=False)

# Get JSON data from FCC website
data = requests.get("https://opendata.fcc.gov/resource/bzun-59r8.json")
data.status_code #  200
myjson = data.json()
print(myjson)

# Or:

