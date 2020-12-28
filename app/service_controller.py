from flask import jsonify, request, make_response
from flask.views import MethodView

from .models import Service
from app import auth, service_repository


class ServicesController(MethodView):
    @staticmethod
    @auth.login_required
    def get():
        """Получить инфу о всех услугах"""
        return jsonify(services=service_repository.get_all())


class ServiceItemController(MethodView):
    @staticmethod
    @auth.login_required
    def get(service_id):
        """Инфо о конкретной услуге"""
        info = service_repository.info(service_id)
        if info:
            return jsonify(info)
        else:
            return make_response(jsonify({}), 404)
