from app import log, app, db
from app.models import Service
from sqlalchemy.exc import *


class ServiceRepository:
    @staticmethod
    def get_all():
        raise NotImplementedError

    @staticmethod
    def info(service_id):
        raise NotImplementedError


class ServiceRepositoryMock(ServiceRepository):
    @staticmethod
    def get_all():
        return [Service.mock(), ]

    @staticmethod
    def info(service_id):
        return Service.mock(service_id)


class ServiceRepositoryDB(ServiceRepository):
    @staticmethod
    def get_all():
        services = Service.query.all()
        if services is None:
            return []
        return [s.to_dict() for s in services]

    @staticmethod
    def info(service_id):
        service = Service.query.filter_by(id=service_id).first()
        if service is None:
            return None
        return service.to_dict()