from app import log, app, db
from app.models import Photostore, Order
from sqlalchemy.exc import *


ORDER_COST = 3000


class StoreRepository:
    @staticmethod
    def get_all():
        raise NotImplementedError

    @staticmethod
    def info(store_id):
        raise NotImplementedError

    @staticmethod
    def stat(store_id):
        raise NotImplementedError


class StoreRepositoryMock(StoreRepository):
    @staticmethod
    def stat(store_id):
        return Photostore.mock_stat(store_id)

    @staticmethod
    def get_all():
        return [Photostore.mock(), ]

    @staticmethod
    def info(store_id):
        return Photostore.mock(store_id)


class StoreRepositoryDB(StoreRepository):
    @staticmethod
    def stat(store_id):
        ret = {}
        orders_of_store = Order.query.filter_by(photostore_id=store_id).all()
        ret['orders_count'] = len(orders_of_store)

        services_sum = 0
        for o in orders_of_store:
            for s in o.services:
                services_sum += s.price
        ret['services_sum'] = services_sum

        ret['orders_sum'] = ORDER_COST*len(orders_of_store) + services_sum
        return ret

    @staticmethod
    def get_all():
        stores = Photostore.query.all()
        if stores is None:
            return []
        return [s.to_dict() for s in stores]

    @staticmethod
    def info(store_id):
        store = Photostore.query.filter_by(id=store_id).first()
        if store is None:
            return None
        return store.to_dict()