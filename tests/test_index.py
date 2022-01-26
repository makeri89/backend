import unittest
import json

from src.index import app

class TestTests(unittest.TestCase):
    def test_api_is_running(self):
        response = app.test_client().get('/api/helloworld')
        res = json.loads(response.data.decode('utf-8'))
        assert response.status_code == 200
        assert res.get('message') == 'Hello, World!'

    def test_api_returns_data(self):
        response = app.test_client().get('/api/getdata')
        res = json.loads(response.data.decode('utf-8'))
        assert response.status_code == 200
        assert len(res) != 0
