from sqlalchemy.sql.schema import ForeignKey
from app import db
from sqlalchemy.orm import relationship
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), unique=False, nullable=False)
    phone = db.Column(db.String(11), unique=True, nullable=False)
    orders = relationship("Order")

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Integer, ForeignKey('user.id'))
    source = db.Column(db.String(120), unique=True, nullable=False)
    photo_salon_id = db.Column(db.Integer)
    status = db.Column(db.Integer)

# class PhotoSalon(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     address = db.Column(db.String(120), unique=True, nullable=False)

# class Order_Service(db.Model):
#     id = db.Column(db.Integer, primary_key=True) 
#     order_id = db.Column(db.Integer)
#     service_id = db.Column(db.Integer, primary_key=True)

# class Service(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     tittle = db.Column(db.String(120), unique=True, nullable=False)
#     decription = db.Column(db.String(120), unique=True, nullable=False)
#     price = db.Column(db.Integer)

# class Employee(db.Model):
#     photo_salon_id = db.Column(db.Integer, primary_key=True)

# class PhotoSalon_Equipment(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     photo_salon_id = db.Column(db.Integer)
#     equipment_id = db.Column(db.Integer, primary_key=True)

# class Equipment(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     tittle = db.Column(db.String(120), unique=True, nullable=False)
#     type = db.Column(db.String(120), unique=True, nullable=False)