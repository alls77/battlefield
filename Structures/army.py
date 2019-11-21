from Structures.structure import Structure


class Army(Structure):
    def __init__(self, name, squads, strategy):
        self.squads = squads
        self.strategy = strategy
        super().__init__(name)

    @property
    def is_active(self):
        return any(squad for squad in self.active_squads)

    @property
    def active_squads(self):
        return [squad for squad in self.squads if squad.is_active]
