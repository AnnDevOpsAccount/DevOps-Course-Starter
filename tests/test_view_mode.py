import pytest
from todo_app.board import Board
from todo_app.data import trello_items
from todo_app.viewModel import ViewModel

def mock_get_items(board):
    TEST_ITEMS = [
        { 'id': 1, 'status': 'To Do', 'title': 'Don tights and save world' },
        { 'id': 2, 'status': 'Doing', 'title': 'Sit on sofa' },
        { 'id': 3, 'status': 'Doing', 'title': 'Play Wordle' },
        { 'id': 4, 'status': 'Doing', 'title': 'Play Chess' },
        { 'id': 5, 'status': 'Done', 'title': 'Play That Funky Music' },
        { 'id': 6, 'status': 'Done', 'title': 'Eat chocolate' }
    ]
    return TEST_ITEMS   


def mock_view_model_gets_all_items(monkeypatch):

    #arrange:  set up so view model would get 4 items
    BOARD = Board ('ID', 'KEY', 'TOKEN', 'TO_DO_LIST_ID' , 'DONE_LIST_ID')
    monkeypatch.setattr(trello_items, 'get_items', mock_get_items)
    item_view_model = ViewModel(BOARD)

    #act: get view model items  
    test_result_items = item_view_model.items

    #assert: the mocked items are returned
    assert test_result_items == mock_get_items(BOARD)
    assert len (test_result_items) == 6

