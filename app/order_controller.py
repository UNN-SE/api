from flask import jsonify, request, make_response
from flask.views import MethodView
from werkzeug.utils import secure_filename

from .logic import order_repository
from .models import Order, UserType
from app import order_repository, auth


class OrdersController(MethodView):
    @staticmethod
    @auth.login_required
    def get():
        """Получить инфу о всех заказах юзера"""
        # параметры фильтра совпадают с названиями полей БД

        # для сотрудников и менеджера
        if auth.current_user().type != UserType.client:
            return jsonify(orders=order_repository.filter(request.args.to_dict()))
        else:
            # клиент может фильтровать только свои заказы
            user_id = auth.current_user().id
            if request.args.get('client_id', None) and int(request.args['client_id']) != user_id:
                return make_response(jsonify({}), 403)
            else:
                args = request.args.to_dict()
                args['client_id'] = user_id
                return jsonify(orders=order_repository.filter(args), user_id=user_id)

    @staticmethod
    @auth.login_required
    def post():
        """Создание заказа"""
        param = request.form.to_dict()
        param['client_id'] = auth.current_user().id
        id = order_repository.create(param)
        return make_response(jsonify({"id": id, "msg": "order is created"}), 200)


class OrderItemController(MethodView):
    @staticmethod
    @auth.login_required
    def get(order_id):
        """Инфо о конкретном заказе"""
        order_info = order_repository.info(order_id)
        if order_info is None:
            return make_response({'msg': 'No such order'}, 404)
        elif auth.current_user().type == UserType.client and auth.current_user().id != order_info['client']:
            return make_response({}, 403)
        else:
            return make_response(jsonify(order_info), 200)

    @staticmethod
    @auth.login_required
    def put(order_id):
        if auth.current_user().type != UserType.client:
            status = int(request.form['status'])
            order_repository.update_status(order_id, status)
            return make_response(jsonify({"id": order_id, "msg": "state of order is updated"}), 200)
        else:
            return make_response(jsonify({"id": order_id, "msg": "only workers allowed"}), 403)

    @staticmethod
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
        except ValueError as err:
            return make_response(jsonify({"id": order_id, "msg": f"{err.args[0]}"}), 400)
        except OSError as err:
            return make_response(jsonify({"id": order_id, "msg": f"{err.args[0]}"}), 500)

        return make_response(jsonify({"id": order_id, "msg": "ok"}), 200)
