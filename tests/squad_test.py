import unittest
from unittest.mock import patch

from Units.soldier import Soldier
from Structures.squad import Squad


class TestSquad(unittest.TestCase):

    @patch('squad.Squad.inflict_damage')
    def test_attack(self, mock_inflict_damage):
        mock_inflict_damage.return_value = 10
        enemy = Squad('s2', [Soldier()])
        squad = Squad('s1', [Soldier()])

        squad.attack(enemy)
        self.assertEqual(enemy.units[0].health, 90)


if __name__ == '__main__':
    unittest.main()
