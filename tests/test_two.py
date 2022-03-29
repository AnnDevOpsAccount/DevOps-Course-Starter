from todo_app.board import Board

def test_two(monkeypatch):

    TEST_ITEMS = [
        { 'id': 1, 'status': 'Not Started', 'title': 'List saved todo items' },
        { 'id': 2, 'status': 'Not Started', 'title': 'Allow new items to be added' },
        { 'id': 3, 'status': 'Not Started', 'title': 'Play Wordle' },
        { 'id': 4, 'status': 'Not Started', 'title': 'Don tights and save world' }
    ]
    BOARD = Board ('ID', 'KEY', 'TOKEN', 'TO_DO_LIST_ID' , 'DONE_LIST_ID')

    def mock_get_items(board):
        return TEST_ITEMS()

    monkeypatch.setattr(trello_items, 'get_items', mock_get_items)

    
    item_view_model = ViewModel(BOARD)

    assert 1 == 1