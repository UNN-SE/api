import enum
from app import db
from sqlalchemy import Column, Integer, String, ForeignKey, Table, Enum
from sqlalchemy.orm import relationship


class UserType(enum.Enum):
    client = "CLIENT"
    manager = "MANAGER"
    employee = "EMPLOYEE"


class User(db.Model):
    id = Column(Integer, primary_key=True)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(120), unique=False, nullable=False)
    phone = Column(String(11), unique=True, nullable=False)
    orders = relationship("Order")
    type = Column(Enum(UserType, nullable=False))
    workingspace = Column(Integer, ForeignKey("photostore.id"))

    @staticmethod
    def mock(user_id=1):
        return {
            "id": user_id,
            "role": "client",
            "email": "test@test.com",
            "phone": 891012345676,
        }


class RevokedTokens(db.Model):
    __tablename__ = 'revoked_tokens'
    token = Column(String, primary_key=True)


photostoreEquipment = Table("photostore_Equipment", db.Model.metadata,
                            Column("photostore_id", Integer, ForeignKey("photostore.id")),
                            Column("equipment_id", Integer, ForeignKey("equipment.id")))

orderService = Table("order_service", db.Model.metadata, Column("order_id", Integer, ForeignKey("order.id")),
                     Column("service_id", Integer, ForeignKey("service.id")))


class Order(db.Model):
    id = Column(Integer, primary_key=True)
    client_id = Column(Integer, ForeignKey('user.id'))
    source = Column(String(120), nullable=False)
    photostore_id = Column(Integer, ForeignKey("photostore.id"))
    status = Column(Integer)
    services = relationship("Service", secondary=orderService, back_populates="orders")

    def to_dict(self):
        services = [s.to_dict() for s in self.services]

        return {
            'client': self.client_id,
            'store': self.photostore_id,
            'photo': self.source,
            'status': self.status,
            'id': self.id,
            'services': services
        }

    @staticmethod
    def mock(order_id=1):
        return {
            "id": order_id,
            "client_id": 1,
            "source": "static/mock/lena.png",
            "photostore_id": 1,
            "status": 1,
        }


class Service(db.Model):
    id = Column(Integer, primary_key=True)
    title = Column(String(120), unique=True, nullable=False)
    decription = Column(String(120), unique=True, nullable=False)
    price = Column(Integer)
    filter_name = Column(String(120), unique=True)
    orders = relationship("Order", secondary=orderService, back_populates="services")

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.decription,
            'price': self.price,
            'is_filter': self.filter_name is not None
        }

    @staticmethod
    def mock(service_id=1):
        return {
            "id": service_id,
            "title": "test",
            "description": "Описание",
            "price": 1000
        }


class Photostore(db.Model):
    id = Column(Integer, primary_key=True)
    address = Column(String(120), unique=True, nullable=False)
    equipments = relationship("Equipment", secondary=photostoreEquipment, back_populates="photoStore")
    workers = relationship("User")

    def to_dict(self):
        return {
            'id': self.id,
            'address': self.address
        }

    @staticmethod
    def mock(salon_id=1):
        return {
            "id": salon_id,
            "address": "Пушкина дом Колотушкина"
        }

    @staticmethod
    def mock_stat(salon_id=1):
        return {
            "id": salon_id,
            "profit_month": "$5000"
        }


class Equipment(db.Model):
    id = Column(Integer, primary_key=True)
    title = Column(String(120), unique=True, nullable=False)
    type = Column(String(120), unique=True, nullable=False)
    photoStore = relationship("Photostore", secondary=photostoreEquipment, back_populates="equipments")

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'type': self.type
        }

    @staticmethod
    def mock(equipment_id=1):
        return {
            "id": equipment_id,
            "title": "Epson JH431",
            "type": "printer"
        }
