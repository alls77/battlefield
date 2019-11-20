from utils import random, logger


class Battlefield:
    def __init__(self, armies):
        self.armies = armies

    def start_battle(self):
        while len(self.active_armies) > 1:
            self._move()

    @logger.move_log
    def _move(self):
        attacking_army, defending_army = self._get_warring_armies()
        attacking_squad, defending_squad = self._get_warring_squads(attacking_army, defending_army)

        if self._is_successful_attack(attacking_squad, defending_squad):
            if self._is_available_attack(attacking_squad):
                attacking_squad.attack(defending_squad)

    @logger.armies_log
    def _get_warring_armies(self):
        attacking_army = random.choice(self.active_armies)
        defending_army = random.choice([army for army in self.active_armies
                                        if army is not attacking_army])
        return attacking_army, defending_army

    @logger.squads_log
    def _get_warring_squads(self, attacking_army, defending_army):
        attacking_squad = random.choice(attacking_army.active_squads)
        defending_squad = attacking_army.strategy.choose(defending_army.active_squads)
        return attacking_squad, defending_squad

    @logger.successful_attack_log
    def _is_successful_attack(self, attacking_squad, defending_squad):
        return attacking_squad.attack_probability() > defending_squad.attack_probability()

    @logger.available_attack_log
    def _is_available_attack(self, attacking_squad):
        return len(attacking_squad.available_units) > 0

    @property
    def active_armies(self):
        return [army
                for army in self.armies
                if army.is_active
                ]
