from flask import jsonify, request, make_response
from flask.views import MethodView


from .models import Equipment, UserType
from app import auth, equipment_repository


class EquipmentsController(MethodView):
    @staticmethod
    @auth.login_required
    def get():
        """Запрос инфы о оборудовании"""
        if auth.current_user().type != UserType.manager:
            return make_response(jsonify(msg='restricted'), 403)

        return jsonify(equipments=equipment_repository.get_all())

    @staticmethod
    @auth.login_required
    def get(store_id):
        """Запрос инфы о оборудовании"""
        if auth.current_user().type != UserType.manager:
            return make_response(jsonify(msg='restricted'), 403)

        return jsonify(equipments=equipment_repository.get_of_store(store_id))

    @staticmethod
    @auth.login_required
    def post():
        """Добавление нового девайса в систему"""
        if auth.current_user().type != UserType.manager:
            return make_response(jsonify(msg='restricted'), 403)

        data = request.form
        try:
            id = equipment_repository.create(data)
            return make_response(jsonify({"equipment_id": id, "msg": "equipment successfully registered"}), 200)
        except Exception as e:
            return make_response(jsonify({"equipment_id": -1, "msg": str(e)}), 400)


class EquipmentItemController(MethodView):
    @staticmethod
    @auth.login_required
    def get(store_id, entity_id):
        """Инфо о конкретном оборудовании в конкретном салоне (уровень запраки принтера или типа того)"""
        if auth.current_user().type != UserType.manager:
            return make_response(jsonify(msg='restricted'), 403)

        return jsonify(store_id=store_id, **Equipment.mock(entity_id))

    @staticmethod
    @auth.login_required
    def post(store_id, entity_id):
        """Присвоить оборудование с заданным id фотосалону"""
        if auth.current_user().type != UserType.manager:
            return make_response(jsonify(msg='restricted'), 403)

        return make_response(jsonify({"store_id": store_id, "id": entity_id, "msg": "equipment is changed"}), 200)

    @staticmethod
    @auth.login_required
    def delete(store_id, entity_id):
        """Забрать оборудование у фотосалона"""
        if auth.current_user().type != UserType.manager:
            return make_response(jsonify(msg='restricted'), 403)
        
        return make_response(jsonify({"store_id": store_id, "id": entity_id, "msg": "equipment is removed"}), 200)
