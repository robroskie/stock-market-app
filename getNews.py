from config import api_key
import requests
import json

def getNews(ticker):
    key = api_key
        # send a GET request with the company name as keyword in the url 
    res = requests.get(f'https://www.alphavantage.co/query?function=NEWS_SENTIMENT&tickers={ticker}&apikey={key}')


    response = res.json()
    # print(response)

    # parsed = json.loads(response)
    # print(json.dumps(response, indent=4, sort_keys=True))
    return response


print(getNews('MSFT'))