

class Airport:
    DEFAULT_CAPACITY = 30

    def __init__(self, capacity = DEFAULT_CAPACITY):
        self.planes = []
        self.capacity = capacity
    
    def land(self, plane):
        if len(self.planes) >= self.capacity:
            raise Exception
        plane.land()
        self.planes.append(plane)

    def take_off(self, plane):
        if not plane in self.planes:
            raise Exception 
        plane.take_off()
        self.planes.remove(plane)
