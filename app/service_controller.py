from flask import jsonify, request, make_response
from flask.views import MethodView

from .models import Service


class ServicesController(MethodView):

    def get(self):
        """Получить инфу о всех услугах"""
        return jsonify(orders=[Service.mock(), ])

    def post(self):
        """Создание новой услуги"""
        return make_response(jsonify({"id": 1, "msg": "service is created"}), 200)


class ServiceItemController(MethodView):
    def get(self, id):
        """Инфо о конкретной услуге"""
        return jsonify(Service.mock(id))

    def put(self, id):
        """Правка услуги"""
        return make_response(jsonify({"id": id, "msg": "service is changed"}), 200)

    def delete(self, id):
        """Удаление услуги"""
        return make_response(jsonify({"id": id, "msg": "service is removed"}), 200)
