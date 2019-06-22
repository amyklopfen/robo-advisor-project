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

parsed_response = json.loads(response.text)

last_refreshed = parsed_response["Meta Data"]["3. Last Refreshed"]
#breakpoint()
latest_close = parsed_response["Time Series (Daily)"]["2019-06-21"]["4. close"]


load_dotenv() #> loads contents of the .env file into the script's environment

API_KEY = os.environ.get("ALPHAVANTAGE_API_KEY") # default to using the "demo" key if an Env Var is not supplied

    
print("------------------------")
print("SELECTED SYMBOL: MSFT")
print("------------------------")
print("REQUESTING STOCK MARKET DATA...")
print("REQUEST AT: ", datetime.datetime.now())
print("------------------------")
print(f"LATEST DAY: {last_refreshed}")
print(f"LATEST CLOSE: ${latest_close}")
print("RECENT HIGH: $11111")
print("RECENT LOW: $999")
print("-----------------------")
print("RECOMMENDATION: BUY!")
print("BECAUSE: TODO")
print("------------------------")
print("HAPPY INVESTING!")
print("-----------------------")

