import requests
from functions.config import *

def symbol_value(symbol,type_fuction):
    url = "https://alpha-vantage.p.rapidapi.com/query"

    querystring = {"from_currency": symbol, "function": type_fuction, "to_currency": "USD"}

    headers = {
        'x-rapidapi-key':RAPIDAPI_KEY,
        'x-rapidapi-host': "alpha-vantage.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    return response.text




