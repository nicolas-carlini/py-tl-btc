import json

def event_parser(event):
    message = json.loads(event['body'])
    print(message)
    event_parsed = {
        "chat_id": message['message']['chat']['id'],
        "text": message['message']['text']
    }
    print(event_parsed)
    return event_parsed
