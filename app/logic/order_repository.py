import os

from app import log, app, db
from app.models import Order, Service
from flask import send_from_directory
from .image_filters import apply_to_image
from sqlalchemy.exc import *


class OrderRepository:
    @staticmethod
    def filter(criteria):
        raise NotImplementedError

    @staticmethod
    def info(order_id):
        raise NotImplementedError

    @staticmethod
    def create(params):
        raise NotImplementedError

    @staticmethod
    def update_status(order_id, new_status):
        raise NotImplementedError

    @staticmethod
    def download_photo(order_id):
        raise NotImplementedError

    @staticmethod
    def upload_photo(order_id, chunk_index, chunks_count, chunk_offset, stream, size):
        raise NotImplementedError

    @staticmethod
    def _save_photo(order_id, chunk_index, chunks_count, chunk_offset, stream, size):
        # ValueError - 4xx ошибки (проблема у клиента)
        # OSError - 5xx ошибки (проблема на сервере)
        filename = f'{str(order_id)}.jpg'  # TODO проверка типа файла
        save_path = os.path.join(app.config['PHOTOS_DIR'], filename)

        # if os.path.exists(save_path) and chunk_index == 0:
        #     raise ValueError('Фото уже существует')

        try:
            with open(save_path, 'wb') as file:
                file.seek(chunk_offset)
                file.write(stream.read())
        except OSError as err:
            log.exception(f'Could not write to file {err}')
            raise OSError("Ошибка записи на диск") from err

        # TODO ограничение максимального размера файла
        if chunk_index + 1 == chunks_count:
            if os.path.getsize(save_path) != size:
                log.error(f"File {filename} was completed, "
                          f"but has a size mismatch."
                          f"Was {os.path.getsize(save_path)} but we"
                          f" expected {size} ")
                raise ValueError('Некорректный размер')
            log.info(f'Файл {filename} загружен успешно')
            return save_path
        else:
            log.debug(f'Chunk {chunk_index + 1}/{chunks_count}, file {filename}')
            return None


class OrderRepositoryFolder(OrderRepository):
    @staticmethod
    def filter(criteria):
        return [Order.mock(), ]

    @staticmethod
    def create(params):
        return 1

    @staticmethod
    def info(order_id):
        return Order.mock(order_id)

    @staticmethod
    def update_status(order_id, new_status):
        pass

    @staticmethod
    def download_photo(order_id):
        return send_from_directory('app/static/mock', 'lena.png')

    @staticmethod
    def upload_photo(order_id, chunk_index, chunks_count, chunk_offset, stream, size):
        super()._save_photo(order_id, chunk_index, chunks_count, chunk_offset, stream, size)


class OrderRepositoryDB(OrderRepository):
    @staticmethod
    def create(params):
        new_order = Order(client_id=params['client_id'],
                          source='photo not loaded yet',
                          photostore_id=params['photostore_id'],
                          status=0)

        services_id = params['services']
        for i in services_id:
            service = Service.query.filter_by(id=i).first()
            new_order.services.append(service)

        filters_id = params['filters']
        for i in filters_id:
            filter = Service.query.filter(Service.filter_name.isnot(None)).filter_by(id=i).first()
            new_order.services.append(filter)

        db.session.add(new_order)
        db.session.commit()
        return new_order.id

    @staticmethod
    def info(order_id):
        order = Order.query.filter_by(id=order_id).first()
        if order is None:
            return None

        services = [s.to_dict() for s in order.services]

        return {
            'client': order.client_id,
            'store': order.photostore_id,
            'photo': order.source,
            'status': order.status,
            'services': services
        }

    @staticmethod
    def filter(criteria):
        return [o.to_dict() for o in Order.query.filter_by(**criteria).all()]

    @staticmethod
    def update_status(order_id, new_status):
        Order.query.filter_by(id=order_id).update({'status': new_status})
        db.session.commit()

    @staticmethod
    def download_photo(order_id):
        filename = f'{str(order_id)}.jpg'  # TODO проверка типа файла
        if os.path.exists(os.path.join(app.config['PHOTOS_DIR'], filename)):
            return send_from_directory(app.config['PHOTOS_DIR'], filename)
        else:
            return None

    @staticmethod
    def upload_photo(order_id, chunk_index, chunks_count, chunk_offset, stream, size):
        path = super(OrderRepositoryDB,OrderRepositoryDB)._save_photo(order_id, chunk_index, chunks_count, chunk_offset, stream, size)
        if path:
            services = Order.query.filter_by(id=order_id).first().services
            for f in services:
                if f.filter_name:
                    apply_to_image(path, f.filter_name)
            Order.query.filter_by(id=order_id).update({'source': path})
            db.session.commit()
