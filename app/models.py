import enum
from app import DB
from sqlalchemy import Column, Integer, String, ForeignKey, Table, Enum
from sqlalchemy.orm import relationship


class UserType(enum.Enum):
    client = "CLIENT"
    manager = "MANAGER"
    employee = "EMPLOYEE"


class User(DB.Model):
    id = Column(Integer, primary_key=True)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(120), unique=False, nullable=False)
    phone = Column(String(11), unique=True, nullable=False)
    orders = relationship("Order")
    type = Column(Enum(UserType, nullable=False))
    workingspace = Column(Integer, ForeignKey("photostore.id"))

    def mock(self, user_id):
        user = User()
        user.type = UserType.client
        user.id = user_id
        user.email = ""
        user.password = ""
        user.phone = ""
        return user


photostoreEquipment = Table("photostore_Equipment", DB.Model.metadata,
                            Column("photostore_id", Integer, ForeignKey("photostore.id")),
                            Column("equipment_id", Integer, ForeignKey("equipment.id")))

orderService = Table("order_service", DB.Model.metadata, Column("order_id", Integer, ForeignKey("order.id")),
                     Column("service_id", Integer, ForeignKey("service.id")))


class Order(DB.Model):
    id = Column(Integer, primary_key=True)
    client_id = Column(Integer, ForeignKey('user.id'))
    source = Column(String(120), unique=True, nullable=False)
    photostore_id = Column(Integer, ForeignKey("photostore.id"))
    status = Column(Integer)
    services = relationship("Service", secondary=orderService, back_populates="orders")


class Service(DB.Model):
    id = Column(Integer, primary_key=True)
    title = Column(String(120), unique=True, nullable=False)
    decription = Column(String(120), unique=True, nullable=False)
    price = Column(Integer)
    orders = relationship("Order", secondary=orderService, back_populates="services")


class Photostore(DB.Model):
    id = Column(Integer, primary_key=True)
    address = Column(String(120), unique=True, nullable=False)
    equipments = relationship("Equipment", secondary=photostoreEquipment, back_populates="photostores")
    workers = relationship("User")


class Equipment(DB.Model):
    id = Column(Integer, primary_key=True)
    tittle = Column(String(120), unique=True, nullable=False)
    type = Column(String(120), unique=True, nullable=False)
    photoStore = relationship("Photostore", secondary=photostoreEquipment, back_populates="equipments")
