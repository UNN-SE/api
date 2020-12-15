from flask import jsonify, request, make_response
from flask.views import MethodView

from .models import User


class UserController(MethodView):
    @staticmethod
    def get(user_id):
        """Получить инфу о юзере"""
        return jsonify(orders=[User.mock(user_id), ])

# TODO авторизация, продумать стркутуру для различных ролей пользователей
