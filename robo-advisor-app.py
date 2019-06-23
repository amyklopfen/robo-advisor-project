# app/robo_advisor.py
investing = True 

import datetime
import csv

import requests 
from urllib.request import urlopen

import json
import os

from dotenv import load_dotenv
import requests

load_dotenv() #> loads contents of the .env file into the script's environment

api_key = os.environ.get("ALPHAVANTAGE_API_KEY") # pulls from .env in folder

#user input validation part 1
while investing: 
    symbol = input("Please enter a stock symbol to get started: ") #prompts user to input stock symbol

    if len(symbol) > 5: #ensure that the stock symbol is not longer than 5 letters
        print("Error, please enter a properly-formed stock symbol like 'MSFT.' Please try again.")
    elif symbol.isdigit(): #test to see whether an integer value was entered, looked up on https://pynative.com/python-check-user-input-is-number-or-string
        print("Error, please enter a properly-formed stock symbol like 'MSFT.' Please try again.")
    else: 
        break 


#user input validation part 2
while investing: 
    requests_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={api_key}"
    response = requests.get(requests_url)
    parsed_response = json.loads(response.text)

    if "Error Message" in parsed_response: #courtesy of Sean G.'s suggestion on slack channel
        print("Sorry, couldn't find any data for that stock symbol.") 
        quit() #log out of program if requested stock does not exist
    else: 
        break  
     

tsd = parsed_response["Time Series (Daily)"]


def to_usd(price):
    return "${0:,.2f}".format(price) 



date_keys = tsd.keys()
dates = list(date_keys)

latest_day = dates[0]
yesterday = dates[1]

last_refreshed = parsed_response["Meta Data"]["3. Last Refreshed"]

latest_close = tsd[latest_day]["4. close"]
yesterday_close = (tsd[yesterday]["4. close"])

high_prices = []
low_prices = []

for date in dates: 
    high_price = (tsd[latest_day]["2. high"])
    high_prices.append(float(high_price))
    low_price = (tsd[latest_day]["3. low"])
    low_prices.append(float(low_price))

recent_high = max(high_prices)
recent_low = min(low_prices)

if float(latest_close) / float(yesterday_close) > 1.025: 
    recommend = "BUY"
    reason = "PRICES HAVE INCREASED OVER THE PAST DAY."
elif (float(latest_close) / float(yesterday_close)) < 0.975: 
    recommend = "SELL"
    reason = "PRICES HAVE DECREASED OVER THE PAST DAY."
else: 
    recommend = "HOLD"
    reason = "PRICES HAVE NOT CHANGED SIGNIFICANTLY. WAIT AND SEE..."

csv_file_path = os.path.join(os.path.dirname(__file__),"data", "prices.csv") 


with open(csv_file_path, "w") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=["timestamp", "open", "high", "low", "close", "volume"])
    writer.writeheader()
    for date in dates: 
        daily_prices = tsd[date]
        writer.writerow({"timestamp": date, "open": daily_prices["1. open"], "high": daily_prices["2. high"], "low": daily_prices["3. low"], "close": daily_prices["4. close"], "volume": daily_prices["5. volume"]})

print("------------------------")
print(f"SELECTED SYMBOL:{symbol}")
print("------------------------")
print("REQUESTING STOCK MARKET DATA...")
print("REQUEST AT: ", datetime.datetime.now())
print("------------------------")
print(f"WRITING DATA TO CSV: {csv_file_path}...")
print("--------------------------")
print(f"LATEST DAY: {last_refreshed}")
print(f"LATEST CLOSE: {to_usd(float(latest_close))}")
print(f"RECENT HIGH: {to_usd(float(recent_high))}")
print(f"RECENT LOW: {to_usd(float(recent_low))}")
print("-----------------------")
print(f"RECOMMENDATION: {recommend}!")
print(f"BECAUSE: {reason}")
print("------------------------")
print("HAPPY INVESTING!")
print("-----------------------")

