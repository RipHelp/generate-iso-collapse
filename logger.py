"""
    Простой логгер
"""

import sys
import logging

ENCODING_UTF8 = "utf-8"
LOG_FILE_NAME = "log_info.log"


class LogHelper:

    def __init__(self):
        logging.basicConfig(level=logging.INFO, filename=LOG_FILE_NAME, encoding=ENCODING_UTF8)
        logging.getLogger().addHandler(logging.StreamHandler(sys.stdout))

        self.save_generate_info()

    def save_generate_info(self, iso_name: str = 'iso_name', iso_size: float = 'iso_size', md5sum: hex = 'md5sum') -> bool:
        """Сохранение сгенерированной информации в файл"""
        with open("generate_info.txt", "a") as generate_log:
            if not generate_log.write(f"{iso_name}<>{iso_size}<>{md5sum}\n"):
                return False
        return True


