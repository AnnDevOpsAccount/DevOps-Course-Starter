from todo_app.data import trello_items

class ViewModel:
    def __init__(self, board):
        self._items = trello_items.get_items( board )

    @property
    def items(self):
        return self._items