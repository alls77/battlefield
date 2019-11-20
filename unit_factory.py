from abc import abstractmethod

from Units.vehicle import Vehicle
from Units.soldier import Soldier
from squad import Squad
from army import Army
from Strategies.strategies import STRATEGIES
from Configs.constants import VEHICLE

UNITS = {}


def unit_register(name):
    def register(cls):
        UNITS[name] = cls
        return cls

    return register


class Factory:
    @abstractmethod
    def create(self, data):
        pass


@unit_register("Soldier")
class SoldierFactory(Factory):
    def create(self, data=None):
        return Soldier()


@unit_register("Vehicle")
class VehicleFactory(Factory):
    def create(self, data={'operator_count': VEHICLE['OPERATOR_COUNT'], 'operator_type': VEHICLE['OPERATOR_TYPE']}):
        operators = [UNITS[data['operator_type']]().create() for _ in range(data['operator_count'])]
        return Vehicle(operators)


@unit_register("Squad")
class SquadFactory(Factory):
    def create(self, data):
        units = []

        for unit in data['units']:
            for _ in range(unit['count']):
                units.append(UNITS[unit['type']]().create())

        return Squad(data['name'], units)


@unit_register("Army")
class ArmyFactory(Factory):
    def create(self, data):
        squads = []

        for squad in data['squads']:
            squads.append(UNITS['Squad']().create(squad))

        return Army(data['name'], squads, STRATEGIES[data['strategy']])
