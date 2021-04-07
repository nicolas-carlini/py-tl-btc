import requests
from functions.config import *

def send_message(text, chat_id):
    url = URL + f"sendMessage?text={text}&chat_id={chat_id}"
    req = requests.get(url)
    return req.status_code
