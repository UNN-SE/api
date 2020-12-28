from app import log, app, db
from app.models import Photostore
from sqlalchemy.exc import *


class StoreRepository:
    @staticmethod
    def get_all():
        raise NotImplementedError

    @staticmethod
    def info(store_id):
        raise NotImplementedError


class StoreRepositoryMock(StoreRepository):
    @staticmethod
    def get_all():
        return [Photostore.mock(), ]

    @staticmethod
    def info(store_id):
        return Photostore.mock(store_id)


class StoreRepositoryDB(StoreRepository):
    @staticmethod
    def get_all():
        services = Photostore.query.all()
        if services is None:
            return []
        return [s.to_dict() for s in services]

    @staticmethod
    def info(store_id):
        service = Photostore.query.filter_by(id=store_id).first()
        if service is None:
            return None
        return service.to_dict()