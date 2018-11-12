
class Car:
    def __init__(self, length, x, y, direction):
        self.x = x
        self.y = y
        self.length = length

        # horizontale of verticale rijrichting
        self.direction = direction

        # boolean die aangeeft of auto kan bewegen
        self.canmove

    def move(self, distance):

        if self.direction == horizontal:
            self.x = self.x + distance
        else:
            self.y = self.y + distance
