import os

from app import log, app


class OrderRepository:
    def save_photo(self, order_id, chunk_index, chunks_count, chunk_offset, stream, size):
        raise NotImplementedError


class OrderRepositoryFolder(OrderRepository):
    def save_photo(self, order_id, chunk_index, chunks_count, chunk_offset, stream, size):
        # ValueError - 4xx ошибки (проблема у клиента)
        # OSError - 5xx ошибки (проблема на сервере)
        filename = f'{str(order_id)}.jpg' # TODO проверка типа файла
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
        else:
            log.debug(f'Chunk {chunk_index + 1}/{chunks_count}, file {filename}')
