from functions.symbol_value import symbol_value
from functions.event_parser import event_parser
from functions.send_message import send_message
from functions.message_parser import message_parser
import json

def bot(event, context):
    event_parsered = event_parser(event)
    message_parsered = message_parser(event_parsered["text"])
    symbol = symbol_value(**message_parsered)
    print(symbol)
    send_message(str(symbol), event_parsered["chat_id"])
    return {
        'statusCode': 200
    }
