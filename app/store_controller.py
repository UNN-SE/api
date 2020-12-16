from flask import jsonify, request, make_response
from flask.views import MethodView

from .models import PhotoSalon
from app import auth


class StoresController(MethodView):
    @auth.login_required
    def get(self):
        """Получить инфу о всех фотосалонах"""
        # TODO return orders of current user
        return jsonify(orders=[PhotoSalon.mock(), ])

    @auth.login_required
    def post(self):
        """Создание фотосалона"""
        return make_response(jsonify({"id": 1, "msg": "order is created"}), 200)


class StoreItemController(MethodView):
    @auth.login_required
    def get(self, id):
        """Инфо о конкретном фотосалоне"""
        return jsonify(PhotoSalon.mock(id))

    @auth.login_required
    def put(self, id):
        """Правка фотосалона"""
        return make_response(jsonify({"id": id, "msg": "store is changed"}), 200)

    @auth.login_required
    def stat(id, params):
        return jsonify(PhotoSalon.mock_stat(id))
