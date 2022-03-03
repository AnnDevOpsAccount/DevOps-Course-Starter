class Item:
    def __init__(self, id, name, status = 'To Do'):
        self.id = id
        self.title = name
        self.status = status

    @classmethod
    def from_trello_card(cls, card, list):
        return cls(card['id'], card['name'], list['name'])