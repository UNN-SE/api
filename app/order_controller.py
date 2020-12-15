from flask import jsonify, request, make_response
from flask.views import MethodView
from werkzeug.utils import secure_filename

from .logic import order_repository
from .models import Order


class OrdersController(MethodView):
    @staticmethod
    def get():
        """Получить инфу о всех заказах юзера"""
        # TODO return orders of current user
        return jsonify(orders=[Order.mock(), ])

    @staticmethod
    def post():
        """Создание заказа"""
        # TODO загрузка фото в заказ
        return make_response(jsonify({"id": 1, "msg": "order is created"}), 200)


class OrderItemController(MethodView):
    @staticmethod
    def get(order_id):
        """Инфо о конкретном заказе"""
        return jsonify(Order.mock(order_id))

    @staticmethod
    def put(order_id):
        return make_response(jsonify({"id": order_id, "msg": "order is changed"}), 200)

    @staticmethod
    def upload_photo(order_id):
        file = next(request.files.values())  # first file in request
        params = request.args if len(request.args) > 0 else request.form
        # https://stackoverflow.com/questions/44727052/handling-large-file-uploads-with-flask
        chunk_index = int(params['dzchunkindex'])
        total_chunks = int(params['dztotalchunkcount'])
        chunk_byte_offset = int(params['dzchunkbyteoffset'])
        file_size = int(params['dztotalfilesize'])
        file_name = secure_filename(file.filename)

        try:
            # 400 and 500s will tell dropzone that an error occurred and show an error
            order_repository.save_photo(order_id, chunk_index, total_chunks, chunk_byte_offset, file.stream, file_size)
        except ValueError as err:
            return make_response(jsonify({"id": order_id, "msg": f"{err.args[0]}"}), 400)
        except OSError as err:
            return make_response(jsonify({"id": order_id, "msg": f"{err.args[0]}"}), 500)

        return make_response(jsonify({"id": order_id, "msg": "ok"}), 200)
