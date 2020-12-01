from flask import jsonify
from flask.views import MethodView

from .models import Order


class OrderController(MethodView):

    def get(self, order_id):
        if order_id is None:
            # TODO return orders of current user
            return jsonify(orders=[Order.mock(), ])
        else:
            return jsonify(Order.mock())
