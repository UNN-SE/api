import socket as s
from flask import request
import photostore


def setup():
    photostore.app.run()


def teardown():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()


class TestAppRoutes:
    def __init__(self):
        self._socket = None

    def setup(self):
        self._socket = s.socket(s.AF_INET, s.SOCK_STREAM)

    def teardown(self):
        self._socket.close()

    def test_server_connect(self):
        self._socket.connect(('localhost', 8081))
        assert self._socket
