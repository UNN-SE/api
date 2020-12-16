import requests
import pytest
from flask import request
from app import create_app


@pytest.fixture
def app():
    test_app = create_app()
    return test_app


def test_server_connect(client):
    response = client.get("http://localhost:5000/api/orders")
    assert response.status_code == 200
    assert response.headers['Content-Type'] == "application/json"
