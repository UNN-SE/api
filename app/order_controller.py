from flask import jsonify, request, make_response
from flask.views import MethodView

from .models import Order


class OrdersController(MethodView):
    def get(self):
        """Получить инфу о всех заказах юзера"""
        # TODO return orders of current user
        return jsonify(orders=[Order.mock(), ])

    def post(self):
        """Создание заказа"""
        # TODO загрузка фото в заказ
        return make_response(jsonify({"id": 1, "msg": "order is created"}), 200)


class OrderItemController(MethodView):
    def get(self, order_id):
        """Инфо о конкретном заказе"""
        return jsonify(Order.mock(order_id))
    
    def put(self, order_id):
        return make_response(jsonify({"id": order_id, "msg": "order is changed"}), 200)

