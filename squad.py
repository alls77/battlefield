from statistics import geometric_mean as gmean


class Squad:
    def __init__(self, name, units):
        self._name = name
        self.units = units

    @property
    def name(self):
        return self._name

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
        damage = self.inflict_damage()
        enemy.get_damage(damage)

        for unit in attacking_units:
            unit.get_experience()
            unit.recharge()

    @property
    def active_units(self):
        return [unit for unit in self.units if unit.is_active]

    @property
    def available_units(self):
        return [unit for unit in self.active_units if unit.is_available]
