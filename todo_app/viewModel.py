from todo_app.data import mongo_items

class ViewModel:
    def __init__(self, app):
        self._items = mongo_items.get_items( app )
    @property
    def items(self):
        return self._items

    @property
    def to_do_items(self):
       to_do_items = []
       for item in self._items:
           if item.status == "To Do":
            to_do_items.append(item)
       return to_do_items

    @property
    def doing_items(self):
       doing_items = []
       for item in self._items:
           if item.status == "Doing":
            doing_items.append(item)
       return doing_items
       
    @property
    def done_items(self):
       done_items = []
       for item in self._items:
           if item.status == "Done":
            done_items.append(item)
       return done_items