from utils import _id


class Structure:
    @_id
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @property
    def is_active(self):
        pass
