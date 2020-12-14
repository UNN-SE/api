import enum
from sqlalchemy.sql.schema import Column, ForeignKey, Table
from app import db
from sqlalchemy.orm import relationship

class UserType(enum.Enum):
    client = "CLIENT"
    manager = "MANAGER"
    employee = "EMPLOYEE"
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), unique=False, nullable=False)
    phone = db.Column(db.String(11), unique=True, nullable=False)
    orders = relationship("Order")
    type = db.Column(db.Enum(UserType, nullable = False))
    workingspace = db.Column(db.Integer, ForeignKey("photostore.id"))


photostoreEquipment = Table("photostore_Equipment", db.Model.metadata, Column("photostore_id", db.Integer, ForeignKey("photostore.id")),
Column("equipment_id", db.Integer, ForeignKey("equipment.id"))) 

orderService = Table("order_service", db.Model.metadata, Column("order_id", db.Integer, ForeignKey("order.id")),
Column("service_id", db.Integer, ForeignKey("service.id")))

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Integer, ForeignKey('user.id'))
    source = db.Column(db.String(120), unique=True, nullable=False)
    photostore_id = db.Column(db.Integer, ForeignKey("photostore.id"))
    status = db.Column(db.Integer)
    services = relationship("Service", secondary = orderService, back_populates = "orders")

class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tittle = db.Column(db.String(120), unique=True, nullable=False)
    decription = db.Column(db.String(120), unique=True, nullable=False)
    price = db.Column(db.Integer)
    orders = relationship("Order", secondary = orderService, back_populates = "services")
class Photostore(db.Model):
     id = db.Column(db.Integer, primary_key=True)
     address = db.Column(db.String(120), unique=True, nullable=False)
     equipments = relationship("Equipment", secondary = photostoreEquipment, back_populates = "photostores")
     workers = relationship("User")
class Equipment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tittle = db.Column(db.String(120), unique=True, nullable=False)
    type = db.Column(db.String(120), unique=True, nullable=False)
    photoStore = relationship("Photostore", secondary = photostoreEquipment, back_populates = "equipments")