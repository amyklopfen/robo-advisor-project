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

breakpoint()

quit()

load_dotenv() #> loads contents of the .env file into the script's environment

API_KEY = os.environ.get("ALPHAVANTAGE_API_KEY") # default to using the "demo" key if an Env Var is not supplied

while investing: 

    try: 
        company_stock = input("Please input the stock symbol for a company of your choice: ")
        
        if len(company_stock) <= 5:
            break 
        else:
            print("Error, please enter a valid stock symbol") 
    except ValueError:
        print("Error, please enter a valid stock")
    
def get_response(company_stock):
    request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={company_stock}&apikey={API_KEY}"
    response = requests.get(request_url)
    parsed_response = json.loads(response.text)
    return parsed_response



