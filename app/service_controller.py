from flask import jsonify, request, make_response
from flask.views import MethodView

from .models import Service


class ServicesController(MethodView):
    @staticmethod
    def get():
        """Получить инфу о всех услугах"""
        return jsonify(orders=[Service.mock(), ])

    @staticmethod
    def post():
        """Создание новой услуги"""
        return make_response(jsonify({"id": 1, "msg": "service is created"}), 200)


class ServiceItemController(MethodView):
    @staticmethod
    def get(service_id):
        """Инфо о конкретной услуге"""
        return jsonify(Service.mock(service_id))

    @staticmethod
    def put(service_id):
        """Правка услуги"""
        return make_response(jsonify({"id": service_id, "msg": "service is changed"}), 200)

    @staticmethod
    def delete(service_id):
        """Удаление услуги"""
        return make_response(jsonify({"id": service_id, "msg": "service is removed"}), 200)
