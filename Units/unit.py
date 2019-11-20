from utils import current_time_ms, _id


class Unit:
    @_id
    def __init__(self, health: float, recharge: int):
        self._health = health
        self._recharge = recharge
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

    def inflict_damage(self) -> float:
        pass

    def attack_probability(self) -> float:
        pass

    def recharge(self):
        self.recharge_time = current_time_ms() + self._recharge
