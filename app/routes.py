from flask import send_file

from app import app

app.url_map.strict_slashes = False


def setup_users():
    from .user_controller import UserController
    user_view = UserController.as_view('user_api')
    app.add_url_rule('/api/users/<int:user_id>', view_func=user_view, methods=['GET'])


def setup_orders():
    from .order_controller import OrdersController, OrderItemController
    orders_view = OrdersController.as_view('orders_api')
    app.add_url_rule('/api/orders/', view_func=orders_view, methods=['GET', 'POST'])
    order_item_view = OrderItemController.as_view('order_item_api')
    app.add_url_rule('/api/orders/<int:order_id>', view_func=order_item_view, methods=['GET', 'PUT'])
    # TODO загрузка фото и комментарии к заказу


def setup_stores():
    from .store_controller import StoresController, StoreItemController
    stores_view = StoresController.as_view('stores_api')
    app.add_url_rule('/api/stores/', view_func=stores_view, methods=['GET', 'POST'])
    item_view = StoreItemController.as_view('store_item_api')
    app.add_url_rule('/api/stores/<int:id>', view_func=item_view, methods=['GET', 'PUT'])
    stat_view = StoreItemController.stat
    app.add_url_rule('/api/stores/<int:id>/stat', view_func=stat_view, defaults={'params': None}, methods=['GET'])


def setup_services():
    from .service_controller import ServicesController, ServiceItemController
    services_view = ServicesController.as_view('services_api')
    app.add_url_rule('/api/services/', view_func=services_view, methods=['GET', 'POST'])
    item_view = ServiceItemController.as_view('service_item_api')
    app.add_url_rule('/api/services/<int:id>', view_func=item_view, methods=['GET', 'PUT', 'DELETE'])


def setup_equipments():
    from .equipment_controller import EquipmentsController, EquipmentItemController
    equipments_view = EquipmentsController.as_view('equipments_api')
    app.add_url_rule('/api/equipments/', methods=['GET', 'POST'],
                     view_func=equipments_view, defaults={'store_id': None})
    app.add_url_rule('/api/stores/<int:store_id>/equipments/', methods=['GET'],
                     view_func=equipments_view) # TODO move it to StoreController?
    item_view = EquipmentItemController.as_view('equipment_item_api')
    app.add_url_rule('/api/stores/<int:store_id>/equipments/<int:id>', methods=['GET', 'POST', 'DELETE'],
                     view_func=item_view)


@app.route('/')
def hello_world():
    return 'TODO render main page'

setup_users()
setup_orders()
setup_stores()
setup_services()
setup_equipments()

