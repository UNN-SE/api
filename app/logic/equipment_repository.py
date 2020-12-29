from app import log, app, db
from app.models import Equipment, Photostore
from sqlalchemy.exc import *


class EquipmentRepository:
    @staticmethod
    def get_all():
        raise NotImplementedError

    @staticmethod
    def get_of_store(store_id):
        raise NotImplementedError

    @staticmethod
    def create(params):
        raise NotImplementedError

    @staticmethod
    def assign(store_id, item_id):
        raise NotImplementedError

    @staticmethod
    def revoke(store_id, item_id):
        raise NotImplementedError



class EquipmentRepositoryMock(EquipmentRepository):
    @staticmethod
    def get_all():
        return [Equipment.mock(), ]

    @staticmethod
    def get_of_store(store_id):
        raise Equipment.mock()

    @staticmethod
    def create(params):
        return 1

    @staticmethod
    def assign(store_id, item_id):
        pass

    @staticmethod
    def revoke(store_id, item_id):
        pass


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
    def get_of_store(store_id):
        return [e.to_dict for e in Photostore.query.filter_by(id=store_id).first().equipments]

    @staticmethod
    def create(params):
        new_eq = Equipment(title=params['title'],
                           type=params['type'])

        db.session.add(new_eq)
        db.session.commit()
        return new_eq.id

    @staticmethod
    def assign(store_id, item_id):
        store = Photostore.query.filter_by(id=store_id).first()
        item = Equipment.query.filter_by(id=item_id).first()
        store.equipments.append(item)
        db.session.commit()

    @staticmethod
    def revoke(store_id, item_id):
        store = Photostore.query.filter_by(id=store_id).first()
        item = Equipment.query.filter_by(id=item_id).first()
        store.equipments.remove(item)
        db.session.commit()