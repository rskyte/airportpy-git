class Plane():
    def __init__(self):
        self.flying = None

    def take_off(self):
        if self.flying is not None:
            if self.flying:
                raise Exception
        self.flying = True

    def land(self):
        if self.flying is not None:
            if not self.flying:
                raise Exception
        self.flying = False