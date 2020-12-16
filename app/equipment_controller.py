from flask import jsonify, request, make_response
from flask.views import MethodView

from .models import Equipment, PhotoSalon_Equipment
from app import auth


class EquipmentsController(MethodView):
    @auth.login_required
    def get(self, store_id):
        """Запрос инфы о оборудовании"""
        if store_id is None:
            # Получить инфу о всех девайсах и их принадлежности фотосалонам
            return jsonify(orders=[Equipment.mock(), ])
        else:
            return jsonify(store_id=store_id, equipments=[Equipment.mock(), ])

    @auth.login_required
    def post(self):
        """Добавление новгого девайса в систему"""
        return make_response(jsonify({"id": 1, "msg": "new equipment item is created"}), 200)


class EquipmentItemController(MethodView):
    @auth.login_required
    def get(self, store_id, id):
        """Инфо о конкретном оборудовании в конкретном салоне (уровень запраки принтера или типа того)"""
        return jsonify(store_id=store_id, **Equipment.mock(id))

    @auth.login_required
    def post(self, store_id, id):
        """Присвоить оборудование с заданным id фотосалону"""
        return make_response(jsonify({"store_id": store_id, "id": id, "msg": "equipment is changed"}), 200)

    @auth.login_required
    def delete(self, store_id, id):
        """Забрать оборудование у фотосалона"""
        return make_response(jsonify({"store_id": store_id, "id": id, "msg": "equipment is removed"}), 200)
