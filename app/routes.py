from flask import send_file

from app import app
from .order_controller import OrderController

orders_view = OrderController.as_view('order_api')
app.add_url_rule('/orders/', view_func=orders_view, defaults={'order_id': None}, methods=['GET', 'POST'])
app.add_url_rule('/orders/<int:order_id>', view_func=orders_view, methods=['GET', ])

@app.route('/')
def hello_world():
    return 'TODO render main page'
