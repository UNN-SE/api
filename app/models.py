class User:
    id = 1
    email = "test@test.com"
    password = "qwerty123"
    phone = "891012345676"

class Manager(User):
    pass

class Client(User):
    id = 1
    email = "test@test.test"
    password = "qwerty123"
    phone = "87035568730"
    
class Order(Client):
    id = 1
    client_id = 1
    source = "source"
    photo_salon_id = 1
    status = 1

class PhotoSalon(Order):
    id = 1
    address = "Пушкина дом Колотушкина"

class OrderService(Order):
    id = 1 
    order_id = 1
    service_id = 1

class Service(OrderService):
    id = 1
    tittle = "test"
    decription = "Описание"
    price = 1000

class Employee(PhotoSalon):
    photo_salon_id = 1

class PhotoSalonEquipment(PhotoSalon):
    id = 1
    photo_salon_id = 1
    equipment_id = 1

class Equipment(PhotoSalonEquipment):
    id = 1
    tittle = "tittle"
    type = "type"