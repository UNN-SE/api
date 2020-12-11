class User:
    id = None
    email = "test@test.com"
    password = "qwerty123"
    phone = "891012345676"
class Client(User):
    id = None
    email = "test@test.test"
    password = "qwerty123"
    phone = "87035568730"
class Order(Client):
    id = None
    client_id = None
    source = "source"
    photo_salon_id = None
    status = None
class PhotoSalon(Order):
    id = None
    address = "Пушкина дом Колотушкина"

class Order_Service(Order):
    id = None 
    order_id = None
    service_id = None

class Service(Order_Service):
    id = None
    tittle = "test"
    decription = "Описание"
    price = None

class Employee(PhotoSalon):
    photo_salon_id = None

class PhotoSalon_Equipment(PhotoSalon):
    id = None
    photo_salon_id = None
    equipment_id = None

class Equipment(PhotoSalon_Equipment):
    id = None
    tittle = "tittle"
    type = "type"