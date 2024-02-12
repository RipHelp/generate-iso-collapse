"""
    Генератор, заполняющий устройство рандомными iso файлами
"""

import random
import string
import subprocess

from tools import Tools
from logger import LogHelper


class GenerateCollapse:
    Log: LogHelper
    Tools: Tools

    def __init__(self, log: LogHelper, tools: Tools):
        self.Log = log
        self.Tools = tools

    def generate_collapse(self) -> bool:
        """Генерация 'коллапса' из iso файлов"""
        rand_file_name = f"{self.__gen_random_file_name()}.iso"
        full_path = self.Tools.get_full_path_filename(path=self.Tools.path, file_name=rand_file_name)
        if not self.__gen_random_iso_file(full_path_file=full_path, path=self.Tools.path):
            self.Log.log_error("Не удалось создать iso файл")
            return False
        if not self.Log.save_generate_info(iso_name=rand_file_name,
                                           iso_size=self.Tools.get_iso_size(path_to_file=full_path),
                                           md5sum=self.Tools.get_md5_file(full_path_file=full_path)):
            self.Log.log_error("Не удалось сохранить информацию в файл")
            return False
        self.Log.log_info("Успешно создан iso файл")
        return True

    def __gen_random_file_name(self) -> str:
        """Генерация рандомного имени файла"""
        rand_file_name = ''.join(random.choice(string.ascii_lowercase) for _ in range(16))
        if not rand_file_name:
            self.Log.log_error("Не удалось сгенерировать имя файла")
            return ''
        self.Log.log_info(f"Сгенерировано имя файла = {rand_file_name}")
        return rand_file_name

    def __gen_random_iso_file(self, full_path_file: str, path: str) -> bool:
        """Генерация рандомного iso файла"""
        res_gen = subprocess.run([f"genisoimage -o {full_path_file} {path}"],
                                 shell=True,
                                 stdout=subprocess.PIPE,
                                 stderr=subprocess.STDOUT)
        if not res_gen:
            self.Log.log_error("Не удалось создать iso файл")
            return False
        self.Log.log_info(f"Создание iso файла")
        return True
