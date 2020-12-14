class User:
    id = 1
    email = "test@test.com"
    password = "qwerty123"
    phone = "891012345676"

    @staticmethod
    def mock(user_id=1):
        return {
            "id": user_id,
            "role": "client",
            "email": "test@test.com",
            "phone": 891012345676
            # TODO вписать поля, нужные фронтенду
        }


class Manager(User):
    pass


class Client(User):
    pass


class Employee(User):
    photo_salon_id = 1


class PhotoSalon():
    id = 1
    address = "Пушкина дом Колотушкина"

    @staticmethod
    def mock(salon_id=1):
        return {
            "id": salon_id,
            "address":  "Пушкина дом Колотушкина"
        }

    @staticmethod
    def mock_stat(salon_id=1):
        return {
            "id": salon_id,
            "profit_month": "$5000"
        }


class Order():
    id = 1
    client_id = 1
    source = "static/mock/lena.png"
    photo_salon_id = 1
    status = 1

    @staticmethod
    def mock(order_id=1):
        return {
                "id": order_id,
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
    description = "Описание"
    price = 1000

    @staticmethod
    def mock(service_id=1):
        return {
            "id": service_id,
            "tittle": "test",
            "description": "Описание",
            "price": 1000
        }


class PhotoSalon_Equipment():
    id = 1
    photo_salon_id = 1
    equipment_id = 1


class Equipment():
    id = 1
    tittle = "tittle"
    type = "type"

    @staticmethod
    def mock(equipment_id=1):
        return {
            "id": equipment_id,
            "tittle": "Epson JH431",
            "type":  "printer"
        }
