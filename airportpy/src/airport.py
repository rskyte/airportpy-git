

class Airport:
    def __init__(self):
        self.planes = []
    
    def land(self, plane):
        self.planes.append(plane)

    def take_off(self, plane):
        self.planes.remove(plane)