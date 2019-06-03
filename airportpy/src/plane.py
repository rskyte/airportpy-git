class Plane():
    def __init__(self):
        self.flying = False

    def take_off(self):
        if self.flying:
            raise Exception
        self.flying = True

    def land(self):
        if not self.flying:
            raise Exception
        self.flying = False