from flask import jsonify, request, make_response
from flask.views import MethodView

from .models import Photostore
from app import auth, photostore_repository


class StoresController(MethodView):
    @staticmethod
    @auth.login_required
    def get():
        """Получить инфу о всех фотосалонах"""
        return jsonify(stores=photostore_repository.get_all())


class StoreController(MethodView):
    @staticmethod
    @auth.login_required
    def get(store_id):
        """Инфо о конкретном фотосалоне"""
        info = photostore_repository.info(store_id)
        if info:
            return jsonify(info)
        else:
            return make_response(jsonify({}), 404)

    @staticmethod
    @auth.login_required
    def stat(store_id, params):
        """Статистика фотосалона"""
        return jsonify(Photostore.mock_stat(store_id))
