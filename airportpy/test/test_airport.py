#!/usr/bin/env python3
import sys
sys.path.append('./airportpy')

import unittest
from unittest.mock import Mock
from src.airport import Airport

class AirportTest(unittest.TestCase):
    def setUp(self):
        self.airport = Airport()
        self.plane_1 = Mock()
        self.plane_2 = Mock()

    def test_airport_can_land_multiple_planes(self):
        self.airport.land(self.plane_1)
        self.airport.land(self.plane_2)
        value_1 = self.airport.planes[0]
        value_2 = self.airport.planes[1]
        self.assertIs(value_1, self.plane_1, "plane has not landed")
        self.assertIs(value_2, self.plane_2, "plane has not landed")
    
    def test_airport_can_allow_planes_to_take_off(self):
        self.airport.land(self.plane_1)
        self.airport.land(self.plane_2)
        self.airport.take_off(self.plane_1)
        value = self.airport.planes[0]
        self.assertIsNot(value, self.plane_1, "plane has not taken off")
        self.assertEqual(1, len(self.airport.planes), "plane has not taken off")
        



if __name__ == '__main__':
    unittest.main()