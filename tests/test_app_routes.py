import pytest
import tempfile
import os
from app import create_app
from flask import jsonify


@pytest.fixture
def app():
    test_app = create_app()
    return test_app


def test_server_connect(client):
    response = client.get("http://localhost:5000/")
    assert response.status_code == 200
    assert response.headers['Content-Type'] == "text/html; charset=utf-8"


def test_server_login(client):
    response = client.post('http://localhost:5000/api/users/login',
                data=jsonify({"login": "username", "password": "password"}).get_json(), follow_redirects=True)
    assert response.status_code == 200
    response = client.get("http://localhost:5000/api/stores/")
    assert response.status_code == 200
    assert response.headers['Content-Type'] == "application/json"
