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

        self.GITHUB_CLIENT_ID = os.environ.get('GITHUB_CLIENT_ID') 
        if not self.GITHUB_CLIENT_ID:
            raise ValueError("No GITHUB_CLIENT_ID set for Flask application. Did you follow the setup instructions?") 

        self.GITHUB_CLIENT_SECRET = os.environ.get('GITHUB_CLIENT_SECRET') 
        if not self.GITHUB_CLIENT_SECRET:
            raise ValueError("No GITHUB_CLIENT_SECRET set for Flask application. Did you follow the setup instructions?")             