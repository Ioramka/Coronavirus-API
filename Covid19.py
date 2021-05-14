import requests
import json

import sqlite3
connection = sqlite3.connect("Covid.db")
cursor = connection.cursor()


url = "https://covid-19-coronavirus-statistics.p.rapidapi.com/v1/stats"

country = input("Enter country: ").title()


querystring = {"country":country}

headers = {
    'x-rapidapi-key': "e37af63ad3msh2bdcfa6097b6b13p1a7c05jsna570de9ef693",
    'x-rapidapi-host': "covid-19-coronavirus-statistics.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

dict_data = json.loads(response.text)

data = dict_data['data']['covid19Stats'][0]

c_country = (data['country'])
confirmed  = (data['confirmed'])
deaths = (data['deaths'])
recovered = (data['recovered'])
date = data['lastUpdate'][:10]



cursor.execute("""CREATE TABLE IF NOT EXISTS CovidStats(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        country VARCHAR,
                        confirmed INTEGER,
                        deaths INTEGER,
                        recovered INTEGER,
                        date VARCHAR)""")


cursor.execute("""INSERT INTO CovidStats(country,confirmed,deaths,recovered,date)
                  VALUES(?,?,?,?,?)""",(c_country,confirmed,deaths,recovered,date))
connection.commit()


# cursor.execute("""SELECT * FROM CovidStats""")
# covid_data = cursor.fetchall()
# for index,item in enumerate(covid_data):
#     print(index,". ",item)