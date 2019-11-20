from abc import abstractmethod

from utils import random

STRATEGIES = {}


def register(cls):
    STRATEGIES[cls.name] = cls()
    return cls


class Strategy:
    name: str

    @abstractmethod
    def choose(self, squads):
        pass


@register
class RandomStrategy(Strategy):
    name = 'random'

    def choose(self, squads):
        return random.choice(squads)


@register
class WeakestStrategy(Strategy):
    name = 'weakest'

    def choose(self, squads):
        return min(squads, key=lambda squad: squad.inflict_damage())


@register
class StrongestStrategy(Strategy):
    name = 'strongest'

    def choose(self, squads):
        return max(squads, key=lambda squad: squad.inflict_damage())
