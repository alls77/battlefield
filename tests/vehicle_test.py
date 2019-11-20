import unittest
from unittest.mock import patch, PropertyMock

from Units.vehicle import Vehicle
from Units.soldier import Soldier


class TestVehicle(unittest.TestCase):

    @patch('Units.vehicle.Vehicle._active_operators', new_callable=PropertyMock)
    def test_get_damage(self, mock_active_operators):
        vehicle = Vehicle([Soldier(), Soldier(), Soldier()])
        mock_active_operators.return_value = vehicle.operators

        vehicle.get_damage(100)
        self.assertEqual(vehicle.health, 140)
        for operator in vehicle.operators:
            self.assertLess(operator.health, 100)

        mock_active_operators.return_value = []
        with self.assertRaises(IndexError):
            vehicle.get_damage(100)

    def test_get_damage_with_two_operators(self):
        vehicle = Vehicle([Soldier(), Soldier()])

        vehicle.get_damage(100)
        self.assertEqual(vehicle.health, 140)
        for operator in vehicle.operators:
            self.assertEqual(operator.health, 80)

    def test_get_damage_with_one_operator(self):
        vehicle = Vehicle([Soldier()])

        vehicle.get_damage(100)
        self.assertEqual(vehicle.health, 140)
        self.assertEqual(vehicle.operators[0].health, 60)

    def test_get_damage_max(self):
        vehicle = Vehicle([Soldier(), Soldier()])

        vehicle.get_damage(1000)
        self.assertFalse(vehicle.is_active)


if __name__ == '__main__':
    unittest.main()
