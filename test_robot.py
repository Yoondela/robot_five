import unittest
from unittest.mock import patch
from world.turtle import world
from io import StringIO
import sys
import robot
import test_base
import world.obstacles as obstacles


class test_world(unittest.TestCase):
    

    def test_replay_range_invalid(self):
        with test_base.captured_io(StringIO('HAL\nforward 3\nforward 2\nforward 1\nreplay 3--a\noff\n')) as (out, err):
            obstacles.random.randint = lambda a, b: 0
            robot.robot_start()

        output = out.getvalue().strip()
        self.assertEqual("""HAL: What must I do next?  > HAL moved forward by 3 steps.
 > HAL now at position (0,3).
HAL: What must I do next?  > HAL moved forward by 2 steps.
 > HAL now at position (0,5).
HAL: What must I do next?  > HAL moved forward by 1 steps.
 > HAL now at position (0,6).
HAL: What must I do next? HAL: Sorry, I did not understand 'replay 3--a'.
HAL: What must I do next? HAL: Shutting down..""", output[-387:])

    def test_do_back(self):

        with test_base.captured_io(StringIO('HAL\nback 10\noff\n')) as (out, err):
            robot.robot_start()

        val = out.getvalue().strip()

        self.assertEqual(val[-135:],"""HAL: What must I do next?  > HAL moved back by 10 steps.
 > HAL now at position (0,-10).
HAL: What must I do next? HAL: Shutting down..""")


if __name__ == "__main__":
    unittest.main()