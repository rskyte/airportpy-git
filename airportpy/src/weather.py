from random import randint

class Weather():
    def __init__(self):
        self.stormy = randint(0, 100) > 85

    def is_stormy(self):
        return self.stormy