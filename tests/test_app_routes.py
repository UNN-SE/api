import requests
from flask import request
import photostore


def setup_module():
    photostore.app.run()


def teardown():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()


class TestAppRoutes:
    def setup(self):
        pass

    def teardown(self):
        pass

    def test_server_connect(self):
        response = requests.get("http://localhost:5000/api/orders")
        assert response.status_code == 200
        assert response.headers['Content-Type'] == "application/json"
