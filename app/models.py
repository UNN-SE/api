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


class PhotoSalon():
    id = 1
    address = "Пушкина дом Колотушкина"


class Order():
    id = 1
    client_id = 1
    source = "static/mock/lena.png"
    photo_salon_id = 1
    status = 1

    @staticmethod
    def mock():
        return {
                "id": 1,
                "client_id": 1,
                "source": "static/mock/lena.png",
                "photo_salon_id": 1,
                "status": 1,
        }


class Order_Service():
    id = 1 
    order_id = 1
    service_id = 1


class Service():
    id = 1
    tittle = "test"
    decription = "Описание"
    price = 1000


class Employee():
    photo_salon_id = 1


class PhotoSalon_Equipment():
    id = 1
    photo_salon_id = 1
    equipment_id = 1


class Equipment():
    id = 1
    tittle = "tittle"
    type = "type"