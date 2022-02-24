import os
import requests
board_url = "https://api.trello.com/1/boards/6212689e46f57218f07af552/lists/open"
items_url = "https://api.trello.com/1/cards"

def get_items(key, token):
    items = []
    querystring = { "key": key,
                    "token":token,
                    "cards":"open"}
    response = requests.request("GET", board_url, params=querystring)
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
    response = requests.request("POST", items_url, params=querystring)
    return None

def complete_item(key, token, list_id, item_id):
    querystring = { "key": key,
                    "token":token,
                    "idList":list_id}
    response = requests.request("PUT", items_url + '/' + item_id, params=querystring)
    return None    