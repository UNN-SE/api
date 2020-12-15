from flask import jsonify, request, make_response
from flask.views import MethodView

from .models import PhotoSalon


class StoresController(MethodView):
    @staticmethod
    def get():
        """Получить инфу о всех фотосалонах"""
        # TODO return orders of current user
        return jsonify(orders=[PhotoSalon.mock(), ])

    @staticmethod
    def post():
        """Создание фотосалона"""
        return make_response(jsonify({"id": 1, "msg": "order is created"}), 200)


class StoreItemController(MethodView):
    @staticmethod
    def get(item_id):
        """Инфо о конкретном фотосалоне"""
        return jsonify(PhotoSalon.mock(item_id))

    @staticmethod
    def put(item_id):
        """Правка фотосалона"""
        return make_response(jsonify({"id": item_id, "msg": "store is changed"}), 200)

    @staticmethod
    def stat(item_id, params):
        return jsonify(PhotoSalon.mock_stat(item_id))
