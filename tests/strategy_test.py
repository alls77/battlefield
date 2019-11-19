import unittest
from unittest.mock import Mock
from Strategies.strategies import WeakestStrategy


class TestStrategy(unittest.TestCase):

    def setUp(self):
        self.strategy = WeakestStrategy()

    def test_choose(self):
        squad1 = Mock()
        squad1.inflict_damage.return_value = 10
        squad2 = Mock()
        squad2.inflict_damage.return_value = 20

        result = self.strategy.choose([squad1, squad2])
        self.assertIs(result, squad1)

    def test_choose_negative(self):
        with self.assertRaises(ValueError):
            self.strategy.choose([])


if __name__ == '__main__':
    unittest.main()
