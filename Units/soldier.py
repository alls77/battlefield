"""This module contains the following classes: Soldier"""

from Units.unit import Unit
from Configs.constants import SOLDIER
from utils import random


class Soldier(Unit):
    """Soldier class (Unit subclass)"""

    def __init__(self, health=SOLDIER['HEALTH'], recharge=SOLDIER['RECHARGE'], experience=0):
        """Create a soldier.
        Extend Unit constructor
        """
        self._experience = experience
        super().__init__(health, recharge)

    @property
    def experience(self):
        return self._experience

    @property
    def is_active(self):
        return self.health > 0

    def get_damage(self, damage):
        """Reduces soldier health by damage value"""
        self._health = max(0, self._health - damage)

    def inflict_damage(self):
        """Calculate a damage done by a soldier"""
        return 0.5 + self._experience

    def attack_probability(self):
        """Calculate a probability of a soldier attack"""
        return 0.5 * (1 + self.health / 100) * random.randint(50 + self.experience, 101) / 100

    def get_experience(self, experience=SOLDIER['EXPERIENCE']):
        """Increase soldier experience by experience value"""
        self._experience = min(self._experience + experience, 50)
