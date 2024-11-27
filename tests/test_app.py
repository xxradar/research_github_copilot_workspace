import json
import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_hello_world(client):
    response = client.get('/hello')
    assert response.data == b'Hello, World!'
    assert response.status_code == 200

def test_personalized_hello(client):
    response = client.post('/hello', data=json.dumps({'name': 'Alice'}), content_type='application/json')
    assert response.data == b'Hello, Alice!'
    assert response.status_code == 200

def test_personalized_hello_no_name(client):
    response = client.post('/hello', data=json.dumps({}), content_type='application/json')
    assert response.data == b'Hello, World!'
    assert response.status_code == 200
