import requests
import json

def getTicker (company_name):
    api_key = '195BBOTV47629JVY'
    # send a GET request with the company name as keyword in the url 
    res = requests.get(f'https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords={company_name}&apikey={api_key}')

    response = res.json()
    # print(response)

    # parsed = json.loads(response)
    # print(json.dumps(response, indent=4, sort_keys=True))
    return response

print(getTicker('microsoft'))