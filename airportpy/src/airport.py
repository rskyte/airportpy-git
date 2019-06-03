import sys
sys.path.append('./airportpy')

from src.weather import Weather

class Airport:
    DEFAULT_CAPACITY = 30

    def __init__(self, capacity = DEFAULT_CAPACITY, weather = Weather()):
        self.planes = []
        self.capacity = capacity
        self.weather = weather
    
    def land(self, plane):
        print(len(self.planes) >= self.capacity)
        print(self.weather.is_stormy())
        if len(self.planes) >= self.capacity or self.weather.is_stormy():
            raise Exception
        plane.land()
        self.planes.append(plane)

    def take_off(self, plane):
        if not plane in self.planes or self.weather.is_stormy():
            raise Exception 
        plane.take_off()
        self.planes.remove(plane)
