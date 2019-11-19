import unittest
from unittest.mock import patch
from Strategies.strategies import WeakestStrategy


class TestStrategy(unittest.TestCase):

    def setUp(self):
        self.strategy = WeakestStrategy()

    @patch('squad.Squad')
    @patch('squad.Squad')
    def test_choose(self, mock_squad1, mock_squad2):
        mock_squad1.inflict_damage.return_value = 10
        mock_squad2.inflict_damage.return_value = 20

        result = self.strategy.choose([mock_squad1, mock_squad2])
        self.assertIs(result, mock_squad1)

    def test_choose_negative(self):
        with self.assertRaises(ValueError):
            self.strategy.choose([])


if __name__ == '__main__':
    unittest.main()
