import json

def event_parser(event):
    message = json.loads(event['body'])
    event_parsed = {
        "chat_id": message['message']['chat']['id'],
        "text": message['message']['text']
    }

    return event_parsed
