import unittest
from Units.soldier import Soldier


class TestSoldier(unittest.TestCase):

    def setUp(self):
        self.soldier = Soldier()

    def test_get_damage(self):
        self.soldier.get_damage(50)
        self.assertEqual(self.soldier.health, 50)

    def test_get_damage_max(self):
        self.soldier.get_damage(150)
        self.assertEqual(self.soldier.health, 0)

    def test_is_active(self):
        self.assertTrue(self.soldier.is_active)

    def test_is_active_negative(self):
        self.soldier.get_damage(100)
        self.assertFalse(self.soldier.is_active)

    def test_inflict_damage(self):
        self.assertEqual(self.soldier.inflict_damage(), 0.5)

    def test_get_experience(self):
        self.soldier.get_experience(1)
        self.assertEqual(self.soldier.experience, 1)

    def test_get_experience_max(self):
        self.soldier.get_experience(55)
        self.assertEqual(self.soldier.experience, 50)

    def test_is_available(self):
        self.assertTrue(self.soldier.is_available)
        self.soldier.recharge()
        self.assertFalse(self.soldier.is_available)

    def test_recharge(self):
        self.assertEqual(self.soldier.recharge_time, 0)
        self.soldier.recharge()
        self.assertNotEqual(self.soldier.recharge_time, 0)


if __name__ == '__main__':
    unittest.main()
