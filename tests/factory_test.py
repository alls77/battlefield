import unittest

from unit_factory import SquadFactory, ArmyFactory


class TestFactory(unittest.TestCase):

    def test_army_create(self):
        test_data = {
            "name": "Army 1",
            "strategy": "random",
            "squads": [
                {
                    "name": "S1",
                    "units": [
                        {
                            "type": "Soldier",
                            "count": 2
                        },
                        {
                            "type": "Vehicle",
                            "count": 3
                        }
                    ]
                }
            ]
        }

        army = ArmyFactory().create(test_data)
        self.assertEqual(army.name, "Army 1")
        self.assertEqual(army.strategy.name, "random")
        self.assertEqual(len(army.squads), 1)

    def test_squad_create(self):
        test_data = {
            "name": "S1",
            "units": [
                {
                    "type": "Soldier",
                    "count": 2
                },
                {
                    "type": "Vehicle",
                    "count": 3
                }
            ]
        }

        squad = SquadFactory().create(test_data)
        self.assertEqual(squad.name, "S1")
        self.assertEqual(len(squad.units), 5)


if __name__ == '__main__':
    unittest.main()
