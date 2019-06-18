# app/robo_advisor.py
investing = True 

import datetime

while investing: 

    try: 
        company_stock = input("Please input the stock symbol for a company of your choice: ")
        
        if len(company_stock) == 4:
            break 
        else:
            print("Error, please enter a valid stock symbol") 
    except ValueError:
        print("Error, please enter a valid stock")
    
print("-------------------------")
print("SELECTED SYMBOL:", company_stock)
print("-------------------------")
print("REQUESTING STOCK MARKET DATA...")
print("REQUEST AT:", datetime.datetime.now())
print("-------------------------")
print("LATEST DAY: 2018-02-20")
print("LATEST CLOSE: $100,000.00")
print("RECENT HIGH: $101,000.00")
print("RECENT LOW: $99,000.00")
print("-------------------------")
print("RECOMMENDATION: BUY!")
print("RECOMMENDATION REASON: TODO")
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")