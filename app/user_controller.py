from flask import jsonify, request, make_response
from flask.views import MethodView

from .models import User
from app import user_repository, auth


class UsersController(MethodView):
    @staticmethod
    def post():
        """Регистрация юзера"""
        return make_response(jsonify({"user_id": 1, "msg": "user successfully registered"}), 200)


class UserAuthController(MethodView):
    @staticmethod
    def post():
        """Авторизация юзера"""
        data = request.get_json()
        login = data['login']
        password = data['password']
        token = user_repository.authenticate(login, password)
        if token:
            return make_response(jsonify({"user_id": 1, "token": token, "msg": "logged in"}), 200)
        else:
            return make_response(jsonify({"msg": "login error"}), 401)


class UserController(MethodView):
    @auth.login_required
    def get(self, user_id):
        """Получить инфу о юзере"""
        return jsonify(User.mock(user_id))
