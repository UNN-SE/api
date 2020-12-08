from flask import jsonify, request, make_response
from flask.views import MethodView

from .models import PhotoSalon

class StoresController(MethodView):
    def get(self):
        """Получить инфу о всех фотосалонах"""
        # TODO return orders of current user
        return jsonify(orders=[PhotoSalon.mock(), ])

    def post(self):
        """Создание фотосалона"""
        return make_response(jsonify({"id": 1, "msg": "order is created"}), 200)


class StoreItemController(MethodView):
    def get(self, id):
        """Инфо о конкретном фотосалоне"""
        return jsonify(PhotoSalon.mock(id))

    def put(self, id):
        """Правка фотосалона"""
        return make_response(jsonify({"id": id, "msg": "store is changed"}), 200)

    def stat(id, params):
        return jsonify(PhotoSalon.mock_stat(id))
