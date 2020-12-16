from flask import jsonify, request, make_response
from flask.views import MethodView

from .models import Service
from app import auth


class ServicesController(MethodView):
    @auth.login_required
    def get(self):
        """Получить инфу о всех услугах"""
        return jsonify(orders=[Service.mock(), ])

    @auth.login_required
    def post(self):
        """Создание новой услуги"""
        return make_response(jsonify({"id": 1, "msg": "service is created"}), 200)


class ServiceItemController(MethodView):
    @auth.login_required
    def get(self, id):
        """Инфо о конкретной услуге"""
        return jsonify(Service.mock(id))

    @auth.login_required
    def put(self, id):
        """Правка услуги"""
        return make_response(jsonify({"id": id, "msg": "service is changed"}), 200)

    @auth.login_required
    def delete(self, id):
        """Удаление услуги"""
        return make_response(jsonify({"id": id, "msg": "service is removed"}), 200)
