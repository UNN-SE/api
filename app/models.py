import enum
from app import db
from sqlalchemy import Column, Integer, String, ForeignKey, Table, Enum
from sqlalchemy.orm import relationship


class UserType(enum.Enum):
    client = "CLIENT"
    manager = "MANAGER"
    employee = "EMPLOYEE"


class User():
    id = Column(Integer, primary_key=True)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(120), unique=False, nullable=False)
    phone = Column(String(11), unique=True, nullable=False)
    orders = relationship("Order")
    type = Column(Enum(UserType, nullable=False))
    workingspace = Column(Integer, ForeignKey("photostore.id"))


    @staticmethod
    def mock(user_id):
        user = {
            "type": 1,
            "id": user_id,
            "email": "",
            "password": "",
            "phone": ""
        }
        return user


photostoreEquipment = Table("photostore_Equipment", db.Model.metadata,
                            Column("photostore_id", Integer, ForeignKey("photostore.id")),
                            Column("equipment_id", Integer, ForeignKey("equipment.id")))

orderService = Table("order_service", db.Model.metadata, Column("order_id", Integer, ForeignKey("order.id")),
                     Column("service_id", Integer, ForeignKey("service.id")))


class Order(db.Model):
    id = Column(Integer, primary_key=True)
    client_id = Column(Integer, ForeignKey('user.id'))
    source = Column(String(120), unique=True, nullable=False)
    photostore_id = Column(Integer, ForeignKey("photostore.id"))
    status = Column(Integer)
    services = relationship("Service", secondary=orderService, back_populates="orders")


class Service(db.Model):
    id = Column(Integer, primary_key=True)
    title = Column(String(120), unique=True, nullable=False)
    decription = Column(String(120), unique=True, nullable=False)
    price = Column(Integer)
    orders = relationship("Order", secondary=orderService, back_populates="services")


class Photostore(db.Model):
    id = Column(Integer, primary_key=True)
    address = Column(String(120), unique=True, nullable=False)
    equipments = relationship("Equipment", secondary=photostoreEquipment, back_populates="photoStore")
    workers = relationship("User")


class Equipment(db.Model):
    id = Column(Integer, primary_key=True)
    tittle = Column(String(120), unique=True, nullable=False)
    type = Column(String(120), unique=True, nullable=False)
    photoStore = relationship("Photostore", secondary=photostoreEquipment, back_populates="equipments")
