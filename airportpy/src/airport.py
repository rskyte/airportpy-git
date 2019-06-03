

class Airport:
    def __init__(self):
        self.planes = []
    
    def land(self, plane):
        plane.land()
        self.planes.append(plane)

    def take_off(self, plane):
        if not plane in self.planes:
            raise Exception 
        plane.take_off()
        self.planes.remove(plane)
