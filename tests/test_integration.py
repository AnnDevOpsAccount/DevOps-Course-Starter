import os
import pytest
import requests 
import mongomock
from todo_app import app
from dotenv import load_dotenv, find_dotenv

@pytest.fixture
def client():
    # Use our test integration config instead of the 'real' version
    file_path = find_dotenv('.env.test')
    load_dotenv(file_path, override=True)

    with mongomock.patch(servers=(('fakemongo.com', 27017),)):
        # Create the new app.
        test_app = app.create_app()

        # Use the app to create a test_client that can be used in our tests.
        with test_app.test_client() as client:
            yield client

class StubResponse():
    def __init__(self, fake_response_data):
        self.fake_response_data = fake_response_data

    def json(self):
        return self.fake_response_data

# Stub replacement for requests.get(url)
def stub(url, params):
    fake_response_data = [{'_id': ObjectId('63556597e561f3969374d358'), 'title': 'wash the floor', 'status:': 'To Do'}]
    return StubResponse(fake_response_data)

def test_index_page(monkeypatch, client):
    # Replace requests.get(url) with our own function
    monkeypatch.setattr(requests, 'get', stub)    

    # Make a request to our app's index page
    response = client.get('/')

    assert response.status_code == 200
    #assert 'wash the floor' in response.data.decode()