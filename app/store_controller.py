from flask import jsonify, request, make_response
from flask.views import MethodView

from .models import Photostore
from app import auth


class StoresController(MethodView):
    @staticmethod
    @auth.login_required
    def get():
        """Получить инфу о всех фотосалонах"""
        return jsonify(orders=[Photostore.mock(), ])

    @staticmethod
    @auth.login_required
    def post():
        """Создание фотосалона"""
        return make_response(jsonify({"id": 1, "msg": "order is created"}), 200)


class StoreController(MethodView):
    @staticmethod
    @auth.login_required
    def get(store_id):
        """Инфо о конкретном фотосалоне"""
        return jsonify(Photostore.mock(store_id))

    @staticmethod
    @auth.login_required
    def put(store_id):
        """Правка фотосалона"""
        return make_response(jsonify({"id": store_id, "msg": "store is changed"}), 200)

    @staticmethod
    @auth.login_required
    def stat(store_id, params):
        """Статистика фотосалона"""
        return jsonify(Photostore.mock_stat(store_id))
