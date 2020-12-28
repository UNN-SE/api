from app import log, app, db
from app.models import Equipment
from sqlalchemy.exc import *


class EquipmentRepository:
    @staticmethod
    def get_all():
        raise NotImplementedError

    @staticmethod
    def create(params):
        raise NotImplementedError


class EquipmentRepositoryMock(EquipmentRepository):
    @staticmethod
    def get_all():
        return [Equipment.mock(), ]

    @staticmethod
    def create(params):
        return 1


class EquipmentRepositoryDB(EquipmentRepository):
    @staticmethod
    def get_all():
        devices = Equipment.query.all()
        if devices is None:
            return []
        ret = []
        for d in devices:
            e = d.to_dict()
            e['store'] = [s.to_dict() for s in d.photoStore]
            ret.append(e)
        return ret

    @staticmethod
    def create(params):
        new_eq = Equipment(title=params['title'],
                           type=params['type'])

        db.session.add(new_eq)
        db.session.commit()
        return new_eq.id