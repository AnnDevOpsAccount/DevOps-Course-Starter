import os
import requests
get_items_url = "https://api.trello.com/1/boards/6212689e46f57218f07af552/lists/open"
add_item_url = "https://api.trello.com/1/cards"

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

def add_item(key, token, list_id, title):
    querystring = { "key": key,
                    "token":token,
                    "idList":list_id,
                    "name":title }
    response = requests.request("POST", add_item_url, params=querystring)
    return None

def save_item(item):
    # ToDo
    return None    