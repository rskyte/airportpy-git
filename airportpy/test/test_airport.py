#!/usr/bin/env python3
import sys
sys.path.append('./airportpy')

import unittest
from unittest.mock import Mock
from unittest.mock import MagicMock
from src.airport import Airport

class AirportTest(unittest.TestCase):
    def setUp(self):
        self.plane_1 = Mock()
        self.plane_1.land = MagicMock()
        self.plane_1.take_off = MagicMock()

        self.plane_2 = Mock()
        self.plane_2.land = MagicMock()
        self.plane_2.take_off = MagicMock()

        self.error_plane = Mock()
        self.error_plane.land = MagicMock(return_value=Exception)
        self.error_plane.take_off = MagicMock(return_value=Exception)

        self.good_weather = Mock()
        self.good_weather.is_stormy = MagicMock(return_value=False)

        self.bad_weather = Mock()
        self.bad_weather.is_stormy = MagicMock(return_value=True)

        self.airport = Airport(3, self.good_weather)
        self.stormy_airport = Airport(3, self.bad_weather)
        
    def test_airport_makes_planes_aware_of_landing(self):
        self.airport.land(self.plane_1)
        self.plane_1.land.assert_called_once()

    def test_airport_makes_planes_aware_of_take_off(self):
        self.airport.land(self.plane_1)
        self.airport.take_off(self.plane_1)
        self.plane_1.take_off.assert_called_once()

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
        
    def test_planes_not_in_airport_cannot_take_off_from_it(self):
        with self.assertRaises(Exception):
            self.airport.take_off(self.plane_1)
        
    def test_planes_cannot_land_if_airport_is_at_max_capacity(self):
        for i in range(0, 3):
            self.airport.land(self.plane_1)
        with self.assertRaises(Exception):
            self.airport.land(self.plane_1)

    def test_planes_cannot_take_off_during_stormy_weather(self):
        self.stormy_airport.planes.append(self.plane_1)
        with self.assertRaises(Exception):
            self.stormy_airport.take_off(self.plane_1)

    def test_planes_cannot_land_during_stormy_weather(self):
        with self.assertRaises(Exception):
            self.stormy_airport.land(self.plane_1)

if __name__ == '__main__':
    unittest.main()