from statistics import geometric_mean as gmean

from Structures.structure import Structure


class Squad(Structure):
    def __init__(self, name, units):
        self.units = units
        super().__init__(name)

    @property
    def is_active(self):
        return any(unit for unit in self.active_units)

    def attack_probability(self):
        return gmean([unit.attack_probability() for unit in self.active_units])

    def get_damage(self, damage):
        for unit in self.active_units:
            unit.get_damage(damage / len(self.active_units))

    def inflict_damage(self):
        return sum(unit.inflict_damage() for unit in self.available_units)

    def attack(self, enemy):
        attacking_units = self.available_units
        enemy.get_damage(self.inflict_damage())

        for unit in attacking_units:
            unit.get_experience()
            unit.recharge()

    @property
    def active_units(self):
        return [unit for unit in self.units if unit.is_active]

    @property
    def available_units(self):
        return [unit for unit in self.active_units if unit.is_available]
