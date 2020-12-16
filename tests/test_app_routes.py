import socket as s
from photostore import app
from flask import request


def setup():
    app.run()


def teardown():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()


class TestAppRoutes:
    def setup(self):
        self._socket = s.socket(s.AF_INET, s.SOCK_STREAM)

    def teardown(self):
        self._socket.close()

    def test_server_connect(self):
        self._socket.connect(('localhost', 8081))
        assert self._socket
