from unittest.mock import patch
import unittest
from squad import Squad
from Units.soldier import Soldier


class TestSquad(unittest.TestCase):

    @patch('squad.Squad.inflict_damage')
    def test_attack(self, mock_inflict_damage):
        mock_inflict_damage.return_value = 10
        enemy = Squad('s2', [Soldier()])
        squad = Squad('s1', [Soldier()])

        squad.attack(enemy)
        self.assertEqual(enemy.units[0].health, 90)

    @patch('Units.soldier.Soldier')
    @patch('Units.vehicle.Vehicle')
    def test_active_units(self, mock_vehicle, mock_soldier):
        squad = Squad('s1', [mock_soldier, mock_vehicle])

        self.assertEqual(len(squad.active_units), 2)


if __name__ == '__main__':
    unittest.main()
