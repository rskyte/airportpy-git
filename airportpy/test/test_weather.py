#!/usr/bin/env python3
import sys
sys.path.append('./airportpy')

import unittest
from unittest.mock import Mock
from src.weather import Weather

class WeatherTest(unittest.TestCase):
    def setUp(self):
        self.weather = Weather()

    def test_can_inform_on_whether_it_is_stormy(self):
        value = self.weather.is_stormy()
        self.assertEqual(type(value), bool)

if __name__ == '__main__':
    unittest.main()