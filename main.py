import logging
import sys
import argparse

from tools import Tools
from logger import LogHelper
from collapse_generate import GenerateCollapse


def parse_args() -> argparse.Namespace:
    parser = create_parser()
    return parser.parse_args(sys.argv[1:])


def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument('-path', nargs=1, help='Полный путь')
    parser.add_argument('-percent', nargs=1, help='Процентное заполнение')
    return parser


if __name__ == '__main__':

    args = parse_args()

    Log = LogHelper()
    Tools = Tools(path=args.path[0], percent=args.percent[0])
    if not Tools.verify_args():
        logging.error("Получены не валидные аргументы")
    GenerateCollapse = GenerateCollapse(log=Log, tools=Tools)

    while True:
        GenerateCollapse.generate_collapse()
        if Tools.checker_size(path=args.path[0]):
            break



