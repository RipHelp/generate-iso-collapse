"""
    Класс выполняющий вспомогательные функции
"""
import os
import hashlib
import logging


class Tools:
    __start_size_device: float = 0
    __target_size: float = 0
    __target_percent: int = 0
    path: str = ''

    def __init__(self, path: str, percent: int):
        self.path = path
        self.__target_percent = int(percent)
        self.__start_size_device = self.__get_free_size_device(path=path)
        self.__target_size = self.__start_size_device - self.__calc_target_size(percent=self.__target_percent)

    def __get_free_size_device(self, path: str) -> float:
        """Получение свободного места на устройстве"""
        device_info = os.statvfs(path)
        free_space = round(device_info.f_bavail * device_info.f_frsize / 1024 ** 2, 2)
        if not free_space:
            logging.error("Не удалось получить размер свободного места на устройстве")
            return 0
        logging.info(f"Свободного места = {free_space} МБ")
        return free_space

    def __calc_target_size(self, percent: int) -> float:
        """Вычисление размера, на которое необходимо заполнить устройство"""
        return (self.__start_size_device * percent) / 100

    def checker_size(self, path: str) -> bool:
        """Проверяет, достигли мы необходимого размера на устройстве"""
        return True if self.__get_free_size_device(path=path) <= self.__target_size else False

    def verify_args(self) -> bool:
        """Проверка переданных аргументов"""
        logging.info(f"Получены аргументы path={self.path} и percent={self.__target_percent}")
        res_path, res_percent = isinstance(self.path, str), isinstance(self.__target_percent, int)
        return res_path and res_percent

    def get_iso_size(self, path_to_file: str) -> float:
        """Получение размера файла"""
        res_size = round(os.path.getsize(path_to_file) / 1024 ** 2, 2)
        if not res_size:
            logging.error("Не удалось получить размер файла файла")
            return 0
        logging.info(f"Размер iso файла = {res_size} МБ")
        return res_size

    def get_md5_file(self, full_path_file) -> hex:
        """Получение хэша файла"""
        res_md5 = hashlib.md5(open(full_path_file, 'rb').read()).hexdigest()
        if not res_md5:
            logging.error("Не удалось получить хэш iso файла")
            return ''
        logging.info(f"Хэш iso файла = {res_md5}")
        return res_md5

    def get_full_path_filename(self, path: str, file_name: str) -> str:
        """Получение полного пути к файлу"""
        return os.path.join(path, file_name)
