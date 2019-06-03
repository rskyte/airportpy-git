

class Airport:
    def __init__(self):
        self.planes = []
    
    def land(self, plane):
        try:
            plane.land()
            self.planes.append(plane)
        except Exception:
            print('Plane cannot land!')

    def take_off(self, plane):
        try:
            plane.take_off()
            self.planes.remove(plane)
        except Exception:
            print('Plane cannot take off!')