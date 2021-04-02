import unittest
from unittest.mock import patch, MagicMock

import randomstub
from player import Player


class MyTestCase(unittest.TestCase):

    def test_name(self):
        ai = MagicMock()
        testable = Player("Testable", ai)
        self.assertEqual("Testable", testable.name)


    @patch('randomstub.RandomStub.random_number')
    def test_pick_and_get_one_chocolate(self, randmock):
        ai = MagicMock()
        testable = Player("P1", ai)
        choc = "B"

        randmock.return_value = 0

        testable.pick_chocolate(choc)

        self.assertEqual(choc, testable.return_chocolate())
        self.assertEqual(None, testable.return_chocolate())


    @patch('randomstub.RandomStub.random_number')
    def test_pick_and_get_two_chocolates(self, randmock):

        ai = MagicMock()
        testable = Player("P1", ai)
        choc1 = "B"
        choc2 = "S"

        randmock.side_effect = [1, 0]

        testable.pick_chocolate(choc1)
        testable.pick_chocolate(choc2)

        self.assertEqual(choc2, testable.return_chocolate())
        self.assertEqual(choc1, testable.return_chocolate())
        self.assertEqual(None, testable.return_chocolate())



if __name__ == '__main__':
    unittest.main()
