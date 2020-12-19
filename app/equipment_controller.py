from flask import jsonify, request, make_response
from flask.views import MethodView


from .models import Equipment, PhotoSalonEquipment
from app import auth


class EquipmentsController(MethodView):
    @staticmethod
    @auth.login_required
    def get(store_id):
        """Запрос инфы о оборудовании"""
        if store_id is None:
            # Получить инфу о всех девайсах и их принадлежности фотосалонам
            return jsonify(orders=[Equipment.mock(), ])
        return jsonify(store_id=store_id, equipments=[Equipment.mock(), ])

    @staticmethod
    @auth.login_required
    def post():
        """Добавление новгого девайса в систему"""
        return make_response(jsonify({"id": 1, "msg": "new equipment item is created"}), 200)


class EquipmentItemController(MethodView):
    @staticmethod
    @auth.login_required
    def get(store_id, entity_id):
        """Инфо о конкретном оборудовании в конкретном салоне (уровень запраки принтера или типа того)"""
        return jsonify(store_id=store_id, **Equipment.mock(entity_id))

    @staticmethod
    @auth.login_required
    def post(store_id, entity_id):
        """Присвоить оборудование с заданным id фотосалону"""
        return make_response(jsonify({"store_id": store_id, "id": entity_id, "msg": "equipment is changed"}), 200)

    @staticmethod
    @auth.login_required
    def delete(store_id, entity_id):
        """Забрать оборудование у фотосалона"""
        return make_response(jsonify({"store_id": store_id, "id": entity_id, "msg": "equipment is removed"}), 200)
