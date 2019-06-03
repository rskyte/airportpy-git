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
        self.assertEqual(value, self.plane, "plane has not landed")
    


if __name__ == '__main__':
    unittest.main()