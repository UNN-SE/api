from flask import jsonify, request, make_response
from flask.views import MethodView

from .models import Service
from app import auth


class ServicesController(MethodView):
    @staticmethod
    @auth.login_required
    def get():
        """Получить инфу о всех услугах"""
        return jsonify(services=[Service.mock(), ])

    @staticmethod
    @auth.login_required
    def post():
        """Создание новой услуги"""
        return make_response(jsonify({"id": 1, "msg": "service is created"}), 200)


class ServiceItemController(MethodView):
    @staticmethod
    @auth.login_required
    def get(service_id):
        """Инфо о конкретной услуге"""
        return jsonify(Service.mock(service_id))

    @staticmethod
    @auth.login_required
    def put(service_id):
        """Правка услуги"""
        return make_response(jsonify({"id": service_id, "msg": "service is changed"}), 200)

    @staticmethod
    @auth.login_required
    def delete(service_id):
        """Удаление услуги"""
        return make_response(jsonify({"id": service_id, "msg": "service is removed"}), 200)
