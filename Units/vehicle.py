from statistics import mean, geometric_mean as gmean

from utils import random
from Units.unit import Unit
from Configs.constants import VEHICLE


class Vehicle(Unit):
    def __init__(self, operators, health=VEHICLE['HEALTH'], recharge=VEHICLE['RECHARGE']):
        self._operators = operators
        super().__init__(health, recharge)

    @property
    def operators(self):
        return self._operators

    @property
    def total_health(self):
        return mean([operator.health for operator in self._active_operators]) + self.health

    @property
    def is_active(self):
        return self.health > 0 and any(self._active_operators)

    def inflict_damage(self):
        return 0.5 + sum(operator.experience for operator in self._active_operators)

    def get_damage(self, damage):
        self._health = max(0, self._health - (damage * 0.6))
        if self.health == 0:
            return

        random_operator = random.choice(self._active_operators)
        if len(self._active_operators) > 1:
            for operator in self._active_operators:
                if operator is random_operator:
                    operator.get_damage(damage * 0.2)
                else:
                    operator.get_damage((damage * 0.2) / (len(self._active_operators) - 1))
        else:
            random_operator.get_damage(damage * 0.4)

    def attack_probability(self):
        return 0.5 * (1 + self.health / 100) * gmean([operator.attack_probability()
                                                      for operator in self._active_operators])

    def get_experience(self):
        for operator in self._active_operators:
            operator.get_experience()

    @property
    def _active_operators(self):
        return [operator
                for operator in self.operators
                if operator.is_active
                ]
