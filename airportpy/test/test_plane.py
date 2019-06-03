#!/usr/bin/env python3
import sys
sys.path.append('./airportpy')

import unittest
from unittest.mock import Mock
from src.plane import Plane

class PlaneTest(unittest.TestCase):
    def setUp(self):
        self.plane = Plane()
        self.airport = Mock()

    def test_planes_can_take_off(self):
        self.plane.take_off()
        self.assertTrue(self.plane.flying, 'plane does not correctly take off')

    def test_planes_can_land(self):
        self.plane.take_off()
        self.plane.land()
        self.assertFalse(self.plane.flying, 'plane does not correctly land')


if __name__ == '__main__':
    unittest.main()