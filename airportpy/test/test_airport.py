#!/usr/bin/env python3
import sys
sys.path.append('./airportpy')

import unittest
from unittest.mock import Mock
from src.airport import Airport

FAILURE = 'incorrect value'

class AirportTest(unittest.TestCase):
    def setUp(self):
        self.airport = Airport()
        self.plane = Mock()

    def test_airport_can_land_planes(self):
        self.airport.land(self.plane)
        value = self.airport.plane
        self.assertIs(value, self.plane, "plane has not landed")
    
    def test_airport_can_allow_planes_to_take_off(self):
        self.airport.land(self.plane)
        self.airport.take_off(self.plane)
        value = self.airport.plane
        self.assertIsNot(value, self.plane, "plane has not taken off")

if __name__ == '__main__':
    unittest.main()