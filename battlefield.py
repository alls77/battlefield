from utils import random


class Battlefield:
    def __init__(self, armies):
        self.armies = armies

    def start_battle(self):
        count = 0
        report = {}
        while len(self.active_armies) > 1:
            count += 1
            attacking_army = random.choice(self.active_armies)
            defending_army = random.choice([army for army in self.active_armies
                                            if army is not attacking_army])
            attacking_squad = random.choice(attacking_army.active_squads)
            defending_squad = attacking_army.strategy.choose(defending_army.active_squads)

            report[count] = {'armies': f'{attacking_army.name} (strategy: {attacking_army.strategy.name}) '
                             f'attacks {defending_army.name} (strategy: {defending_army.strategy.name});'}

            report[count]['attack'] = f'the attack failed'

            if attacking_squad.attack_probability() > defending_squad.attack_probability():
                report[count]['squads'] = f'{attacking_squad.name} of {attacking_army.name} has no available_units ' \
                    f'to attack'
                if len(attacking_squad.available_units) > 0:
                    report[count]['squads'] = f'{attacking_squad.name} of {attacking_army.name} inflict damage' \
                        f'({attacking_squad.inflict_damage()}) to {defending_squad.name} of {defending_army.name}'
                    attacking_squad.attack(defending_squad)
                    report[count]['attack'] = f'the attack was successful'

        return report

    @property
    def active_armies(self):
        return [army
                for army in self.armies
                if army.is_active
                ]
