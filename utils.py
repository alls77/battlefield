import os
from random import Random
from time import monotonic
from json import load, dump

from battle_logger import BattleLogger

random = Random()
logger = BattleLogger()
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


def load_json(file_name: str):
    with open(os.path.join(ROOT_DIR, file_name)) as json_file:
        file = load(json_file)
    return file


def dump_json(data, file_name: str):
    with open(os.path.join(ROOT_DIR, file_name), 'w') as json_file:
        dump(data, json_file, indent=2)


def current_time_ms():
    return monotonic() * 1000


def _id(function):
    id_number = 0

    def wrapper(*args, **kwargs):
        nonlocal id_number
        id_number += 1
        setattr(args[0], '_id', args[0].__class__.__name__ + str(id_number))
        return function(*args, **kwargs)

    return wrapper
