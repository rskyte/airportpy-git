#!/usr/bin/env python3
import sys
import unittest
sys.path.append('./airportpy')
from src.airport import Airport

FAILURE = 'incorrect value'

class AirportTest(unittest.TestCase):
    def setUp(self):
        self.airport = Airport()


if __name__ == '__main__':
    unittest.main()