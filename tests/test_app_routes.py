import pytest
from app import create_app
from flask import jsonify


@pytest.fixture(scope="module")
def app():
    test_app = create_app()
    return test_app


def test_server_connect(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.headers['Content-Type'] == "text/html; charset=utf-8"


def test_server_signup(client):
    response = client.post('/api/users',
                           data=jsonify({"login": "username", "password": "password", "phone": "phone"}).get_json(),
                           follow_redirects=True)
    assert response.status_code == 200
    assert response.headers['Content-Type'] == "application/json"


def test_server_signin(client):
    response = client.post('/api/users/login',
                           data=jsonify({"login": "username", "password": "password"}).get_json(),
                           follow_redirects=True)
    assert response.status_code == 200
    assert response.headers['Content-Type'] == "application/json"
    assert response.json["token"] is not None
