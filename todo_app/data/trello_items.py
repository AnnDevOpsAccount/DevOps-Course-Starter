import os
import requests
get_items_url = "https://api.trello.com/1/boards/6212689e46f57218f07af552/lists/open"

def get_items(key, token):
    items = []
    querystring = { "key": key,
                    "token":token,
                    "cards":"open"}
    response = requests.request("GET", get_items_url, params=querystring)
    response_json = response.json()     
    for trello_list in response_json:
        for card in trello_list['cards']:
            card['status'] = trello_list['name']
            card['title'] = card ['name']
            items.append(card)
    return items

def add_item(title):
    # ToDo
    return None

def save_item(item):
    # ToDo
    return None    