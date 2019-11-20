class BattleLogger:

    def __init__(self):
        self.report = {}
        self.data = {}

    def move_log(self, function):
        self.data['count'] = 0

        def wrapper(*args, **kwargs):
            self.data['count'] += 1
            return function(*args, **kwargs)

        return wrapper

    def armies_log(self, function):
        def wrapper(*args, **kwargs):
            attacking_army, defending_army = function(*args, **kwargs)
            self.data['attacking_army'], self.data['defending_army'] = attacking_army, defending_army

            self.report[self.data['count']] = {
                'armies': f'{attacking_army.name} (strategy: {attacking_army.strategy.name}) '
                f'attacks {defending_army.name} (strategy: {defending_army.strategy.name});'}
            return attacking_army, defending_army

        return wrapper

    def squads_log(self, function):
        def wrapper(*args, **kwargs):
            attacking_squad, defending_squad = function(*args, **kwargs)
            self.data['attacking_squad'], self.data['defending_squad'] = attacking_squad, defending_squad
            return attacking_squad, defending_squad

        return wrapper

    def successful_attack_log(self, function):
        def wrapper(*args, **kwargs):
            result = function(*args, **kwargs)
            if not result:
                self.report[self.data['count']]['attack'] = f'the attack failed'
            self.data['successful_attack'] = result
            return result

        return wrapper

    def available_attack_log(self, function):
        def wrapper(*args, **kwargs):
            result = function(*args, **kwargs)
            if result:
                self.report[self.data['count']]['squads'] = f'{self.data["attacking_squad"].name} of ' \
                    f'{self.data["attacking_army"].name} inflict damage' \
                    f'({self.data["attacking_squad"].inflict_damage()}) to {self.data["defending_squad"].name} of ' \
                    f'{self.data["defending_army"].name}'
                self.report[self.data['count']]['attack'] = f'the attack was successful'
            else:
                self.report[self.data['count']]['squads'] = f'{self.data["attacking_squad"].name} of ' \
                    f'{self.data["attacking_army"].name} has no available_units ' \
                    f'to attack'
                self.report[self.data['count']]['attack'] = f'the attack failed'
            return result

        return wrapper
