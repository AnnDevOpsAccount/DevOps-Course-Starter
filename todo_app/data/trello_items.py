import os
import requests
from todo_app.item import Item
from todo_app.board import Board

board_url = "https://api.trello.com/1/boards/"
items_url = "https://api.trello.com/1/cards"

def get_items( board ):
    items = []
    querystring = { "key": board.key,
                    "token":board.token,
                    "cards":"open"}                 
    response = requests.request("GET", board_url + board.id + "/lists/open", params=querystring)
    response_json = response.json()     
    for trello_list in response_json:
        for card in trello_list['cards']:
            items.append (Item.from_trello_card(card, trello_list))
    return items

def add_item( board, title):
    querystring = { "key": board.key,
                    "token": board.token,
                    "idList": board.to_do_list,
                    "name":title }
    response = requests.request("POST", items_url, params=querystring)

def complete_item(board, item_id):
    querystring = { "key": board.key,
                    "token": board.token,
                    "idList":board.done_list}
    response = requests.request("PUT", items_url + '/' + item_id, params=querystring)   