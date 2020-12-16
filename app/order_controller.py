from flask import jsonify, request, make_response
from flask.views import MethodView
from werkzeug.utils import secure_filename

from .models import Order
from app import order_repository, auth


class OrdersController(MethodView):
    @auth.login_required
    def get(self):
        """Получить инфу о всех заказах юзера"""
        # TODO return orders of current user
        return jsonify(orders=[Order.mock(), ], user_id=auth.current_user()['id'])

    @auth.login_required
    def post(self):
        """Создание заказа"""
        return make_response(jsonify({"id": 1, "msg": "order is created"}), 200)


class OrderItemController(MethodView):
    @auth.login_required
    def get(self, order_id):
        """Инфо о конкретном заказе"""
        return jsonify(Order.mock(order_id))

    @auth.login_required
    def put(self, order_id):
        return make_response(jsonify({"id": order_id, "msg": "order is changed"}), 200)

    @auth.login_required
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
        except ValueError as e:
            return make_response(jsonify({"id": order_id, "msg": f"{e.args[0]}"}), 400)
        except OSError as e:
            return make_response(jsonify({"id": order_id, "msg": f"{e.args[0]}"}), 500)

        return make_response(jsonify({"id": order_id, "msg": "ok"}), 200)
