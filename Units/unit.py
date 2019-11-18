from utils import current_time_ms


class Unit:
    def __init__(self, health, recharge: int):
        self._health = health
        self.recharge_ms = recharge
        self.recharge_time = 0

    @property
    def health(self):
        return self._health

    @property
    def is_active(self):
        pass

    @property
    def is_available(self):
        return self.recharge_time <= current_time_ms()

    def get_damage(self, damage):
        pass

    def inflict_damage(self):
        pass

    def attack_probability(self):
        pass

    def recharge(self):
        self.recharge_time = current_time_ms() + self.recharge_ms
