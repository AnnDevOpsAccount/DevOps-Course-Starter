import os


class Config:
    def __init__(self):
        """Base configuration variables."""
        
        self.MONGO_CONNECTION_STRING = os.environ.get('MONGO_CONNECTION_STRING')     
        if not self.MONGO_CONNECTION_STRING:
            raise ValueError("No MONGO_CONNECTION_STRING set for Flask application. Did you follow the setup instructions?")      
                    
        self.MONGO_DATABASE = os.environ.get('MONGO_DATABASE')     
        if not self.MONGO_DATABASE:
            raise ValueError("No MONGO_DATABASE set for Flask application. Did you follow the setup instructions?")      