import unittest
from unittest import mock
from unittest.mock import patch
from world.text import world
from io import StringIO
import sys
import robot
from world import obstacles


class test_world(unittest.TestCase):
    obst = [(125, 51), (-130, 62), (141, 136), (118, -38)]
    @mock.patch("world.obstacles.generate_obstacles", return_value=obst)
    def test_generate_obstacles(self, mock_randint):
        obst = [(125, 51), (-130, 62), (141, 136), (118, -38)]
        assert(obstacles.generate_obstacles() == obst)


    def test_no_obstacle_in_position(self):
        assert(obstacles.is_position_blocked(-1,21) == False)


    def test_obstacle_in_position(self):
        self.maxDiff = None
        obstacles.obstacles.append((1,1))
        assert(obstacles.is_position_blocked(1,1) == True)


    def test_no_obstacle_in_the_path(self):
        self.maxDiff = None
        obstacles.obstacles.append((1,1))
        assert(obstacles.is_path_blocked(0,1,9,1) == False)


    def test_obstacle_in_the_path(self):
        self.maxDiff = None
        obstacles.obstacles.append((1,1))
        assert(obstacles.is_path_blocked(0,1,3,1) == True)

    
    

if __name__ == "__main__":
    unittest.main()