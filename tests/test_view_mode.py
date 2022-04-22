import pytest
from todo_app.board import Board
from todo_app.data import trello_items
from todo_app.viewModel import ViewModel
from todo_app.item import Item

TEST_BOARD = Board ('ID', 'KEY', 'TOKEN', 'TO_DO_LIST_ID' , 'DONE_LIST_ID')

def get_test_items():
    test_items = [
            Item(1, 'Don tights and save world', 'To Do'),
            Item(2, 'Sit on sofa', 'Doing'),
            Item(3, 'Play Wordle', 'Doing'),
            Item(4, 'Play Chess', 'Doing'),
            Item(5, 'Play That Funky Music', 'Done'),
            Item(6, 'Eat chocolate', 'Done')
        ]
    return test_items

def mock_get_items(board):
    return get_test_items()  


def set_up_view_model (monkeypatch):
    
    monkeypatch.setattr(trello_items, 'get_items', mock_get_items)
    item_view_model = ViewModel(TEST_BOARD)
    return (item_view_model)


def test_mock_view_model_get_all_items(monkeypatch):

    #arrange:  set up view model 
    item_view_model = set_up_view_model (monkeypatch)

    #act: get all view model items  
    test_result_items = item_view_model.items

    #assert: the mocked items are returned
    test_items = get_test_items()
    for i in range(0, 5):
        assert test_result_items[i].title ==  test_items[i].title
    assert len (test_result_items) == 6


def test_mock_view_model_get_to_do_items(monkeypatch):

    #arrange:  set up view model 
    item_view_model = set_up_view_model (monkeypatch)

    #act: get to do view model items  
    test_result_items = item_view_model.to_do_items

    #assert: correct number of items returned
    assert test_result_items[0].title == 'Don tights and save world'
    assert len (test_result_items) == 1
    

def test_mock_view_model_get_doing_items(monkeypatch):

    #arrange:  set up view model 
    item_view_model = set_up_view_model (monkeypatch)

    #act: get doing view model items  
    test_result_items = item_view_model.doing_items

    #assert: correct number of items returned
    assert test_result_items[0].id == 2
    assert test_result_items[1].id == 3
    assert test_result_items[2].id == 4
    assert len (test_result_items) == 3
    

def test_mock_view_model_get_done_items(monkeypatch):

    #arrange:  set up view model 
    item_view_model = set_up_view_model (monkeypatch)

    #act: get done view model items  
    test_result_items = item_view_model.done_items

    #assert: correct number of items returned
    assert len (test_result_items) == 2
    assert test_result_items[0].id == 5
    assert test_result_items[1].id == 6