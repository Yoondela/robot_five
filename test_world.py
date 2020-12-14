import unittest
from world.text import world


class test_world(unittest.TestCase):
    def test_update(self):

        world.update_position(1)
        x = world.position_x
        y = world.position_y
        self.assertEqual(x,0)
        self.assertEqual(y,7)
        world.position_x = 0
        world.position_y = 0

if __name__ == "__main__":
    unittest.main()