from flask import jsonify, request, make_response
from flask.views import MethodView

from .models import Photostore


class StoresController(MethodView):
    @staticmethod
    def get():
        """Получить инфу о всех фотосалонах"""
        # TODO return orders of current user
        return jsonify(orders=[Photostore.mock(), ])

    @staticmethod
    def post():
        """Создание фотосалона"""
        return make_response(jsonify({"id": 1, "msg": "order is created"}), 200)


class StoreController(MethodView):
    @staticmethod
    def get(store_id):
        """Инфо о конкретном фотосалоне"""
        return jsonify(PhotoSalon.mock(store_id))

    @staticmethod
    def put(store_id):
        """Правка фотосалона"""
        return make_response(jsonify({"id": store_id, "msg": "store is changed"}), 200)

    @staticmethod
    def stat(store_id, params):
        return jsonify(PhotoSalon.mock_stat(store_id))
