from functions.config import *

def message_parser(query):
    query = query.upper().split(" ")
    type_fuction = None
    symbol = None

    for word in query:
        if word in stocks_name:
            type_fuction = stk
            symbol = word
        if word in crypt_name:
            type_fuction = crry
            symbol = word

    payload = {
        "type_fuction": type_fuction,
        "symbol": symbol
    }

    return payload






