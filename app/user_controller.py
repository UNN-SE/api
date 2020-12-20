from flask import jsonify, request, make_response
from flask.views import MethodView

from .models import User
from app import USER_REPOSITORY, AUTH, LOG


class UsersController(MethodView):
    @staticmethod
    def post():
        """Регистрация юзера"""
        return make_response(jsonify({"user_id": 1, "msg": "user successfully registered"}), 200)


class UserAuthController(MethodView):
    @staticmethod
    def post():
        """Авторизация юзера"""
        data = request.form
        login = data['login']
        password = data['password']
        token = USER_REPOSITORY.authenticate(login, password)
        if token:
            return make_response(jsonify({"user_id": 1, "token": token, "msg": "logged in"}), 200)
        return make_response(jsonify({"msg": "login error"}), 401)

    @staticmethod
    @AUTH.login_required
    def logout():
        return make_response(jsonify({"msg": "logged out"}), 200)


class UserController(MethodView):
    @staticmethod
    @AUTH.login_required
    def get(user_id):
        """Получить инфу о юзере"""
        return jsonify(User.mock(user_id))
