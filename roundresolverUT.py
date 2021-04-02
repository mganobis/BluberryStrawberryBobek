import unittest
from unittest.mock import MagicMock, patch

from roundresolver import RoundResolver


class MyTestCase(unittest.TestCase):

    @patch('randomstub.RandomStub.roll_dice')
    def test_dice_and_choose_not_match(self, rds):

        testable = RoundResolver()
        board = ["B", "S"]

        player = MagicMock()
        player.choose_chocolate.return_value = 1
        rds.return_value = "B"

        testable.play_round(player, board)

        self.assertEqual(["B", "S"], board)


    @patch('randomstub.RandomStub.roll_dice')
    def test_dice_and_choose_match(self, rds):

        testable = RoundResolver()
        board = ["B", "S"]

        player = MagicMock()
        player.choose_chocolate.return_value = 1
        rds.return_value = "S"

        testable.play_round(player, board)

        self.assertEqual(["B"], board)


if __name__ == '__main__':
    unittest.main()
