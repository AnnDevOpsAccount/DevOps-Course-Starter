import os


class Config:
    def __init__(self):
        """Base configuration variables."""
        self.TRELLO_BOARD_KEY = os.environ.get('TRELLO_BOARD_KEY')
        if not self.TRELLO_BOARD_KEY:
            raise ValueError("No TRELLO_BOARD_KEY set for Flask application. Did you follow the setup instructions?")

        self.TRELLO_BOARD_TOKEN = os.environ.get('TRELLO_BOARD_TOKEN')
        if not self.TRELLO_BOARD_TOKEN:
            raise ValueError("No TRELLO_BOARD_TOKEN set for Flask application. Did you follow the setup instructions?")