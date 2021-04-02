import unittest
import game


class MyTestCase(unittest.TestCase):

    def test_switch_players(self):
        testable = game.Game()
        self.assertEqual("P1", testable.player.name)
        testable.switch_player()
        self.assertEqual("P2", testable.player.name)
        testable.switch_player()
        self.assertEqual("P1", testable.player.name)



if __name__ == '__main__':
    unittest.main()
