# app/robo_advisor.py
investing = True 

import datetime
import csv

import json
import os

from dotenv import load_dotenv
import requests
requests_url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=MSFT&apikey=demo"

response = requests.get(requests_url)

#print(type(response))
#print(response.status_code)
#print(response.text)
def to_usd(price):
    return "${0:,.2f}".format(price) 

parsed_response = json.loads(response.text)

tsd = parsed_response["Time Series (Daily)"]

date_keys = tsd.keys()
dates = list(date_keys)

latest_day = dates[0]

last_refreshed = parsed_response["Meta Data"]["3. Last Refreshed"]
#breakpoint()
latest_close = tsd[latest_day]["4. close"]

high_prices = []

for date in dates: 
    high_price = (tsd[latest_day]["2. high"])
    high_prices.append(float(high_price))

recent_high = max(high_prices)


load_dotenv() #> loads contents of the .env file into the script's environment

API_KEY = os.environ.get("ALPHAVANTAGE_API_KEY") # default to using the "demo" key if an Env Var is not supplied

    
print("------------------------")
print("SELECTED SYMBOL: MSFT")
print("------------------------")
print("REQUESTING STOCK MARKET DATA...")
print("REQUEST AT: ", datetime.datetime.now())
print("------------------------")
print(f"LATEST DAY: {last_refreshed}")
print(f"LATEST CLOSE: {to_usd(float(latest_close))}")
print(f"RECENT HIGH: {to_usd(float(recent_high))}")
print("RECENT LOW: $999")
print("-----------------------")
print("RECOMMENDATION: BUY!")
print("BECAUSE: TODO")
print("------------------------")
print("HAPPY INVESTING!")
print("-----------------------")

