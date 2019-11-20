import os

from utils import load_json, random, dump_json, logger
from unit_factory import UNITS
from Configs.constants import MIN_ARMY_COUNT
from battlefield import Battlefield


def main():
    config = load_json(os.path.join('Configs', 'config.json'))
    random.seed(config['seed'])

    armies = []
    for data in config['armies']:
        armies.append(UNITS['Army']().create(data=data))

    if len(armies) >= MIN_ARMY_COUNT:
        Battlefield(armies).start_battle()
        dump_json(logger.report, os.path.join('Configs', 'report.json'))


if __name__ == '__main__':
    main()
