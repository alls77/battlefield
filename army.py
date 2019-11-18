class Army:
    def __init__(self, name, squads, strategy):
        self._name = name
        self.squads = squads
        self.strategy = strategy

    @property
    def name(self):
        return self._name

    @property
    def is_active(self):
        return any(squad for squad in self.active_squads)

    @property
    def active_squads(self):
        return [squad for squad in self.squads if squad.is_active]
