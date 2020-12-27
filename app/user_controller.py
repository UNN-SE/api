from flask import jsonify, request, make_response
from flask.views import MethodView

from .models import User, UserType
from app import user_repository, auth, log


class UsersController(MethodView):
    @staticmethod
    def post():
        """Регистрация юзера"""
        data = request.form
        login = data['login']
        password = data['password']
        phone = data['phone']
        try:
            id = user_repository.register(login=login, password=password, phone=phone, type=UserType.client)
            return make_response(jsonify({"user_id": id, "msg": "user successfully registered"}), 200)
        except Exception as e:
            return make_response(jsonify({"user_id": -1, "msg": str(e)}), 400)


class UserAuthController(MethodView):
    @staticmethod
    def post():
        """Авторизация юзера"""
        data = request.form
        login = data['login']
        password = data['password']
        token = user_repository.authenticate(login, password)
        if token:
            return make_response(jsonify({"user_id": token[0], "token": token[1], "msg": "logged in"}), 200)
        return make_response(jsonify({"msg": "Incorrect username or password"}), 401)

    @staticmethod
    @auth.login_required
    def logout():
        try:
            token = auth.get_auth()['token']
            user_repository.logout(token)
            return make_response(jsonify({"msg": f"Goog bye, {auth.current_user().email}"}), 200)
        except Exception as e:
            return make_response(jsonify({"msg": str(e)}), 400)


class UserController(MethodView):
    @staticmethod
    @auth.login_required
    def get(user_id):
        """Получить инфу о юзере"""
        if auth.current_user().type != UserType.client or auth.current_user().id == user_id:
            return jsonify(user_repository.info(user_id))
        else:
            return make_response(jsonify({}), 403)
