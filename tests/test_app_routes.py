import requests
from flask import request
import photostore


class TestAppRoutes:
    def setup(self):
        pass

    def teardown(self):
        pass

    def test_server_connect(self):
        response = requests.get("http://localhost:5000/api/orders")
        assert response.status_code == 200
        assert response.headers['Content-Type'] == "application/json"
