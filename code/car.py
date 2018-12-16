
class Car(object):
    def __init__(self, length, x, y, direction, width, id):
        self.x = x
        self.y = y
        self.length = length
        self.width = width
        self.list_position = width * self.y + self.x
        self.id = id

        # horizontal or vertical direction
        self.direction = direction

        # number that is used to determine by how many positions a car should shift in coordinate list when moving (see update_coordinates function)
        if direction == "hor":
            self.increase_nr = 1
        else:
            self.increase_nr = self.width

    def update_coordinates(self, coordinates, command):

        if command == "set":
            bool = True
            car = self.id

        # if command is remove
        else:
            bool = False
            car = 0

        # number of first coordinate
        list_position = self.width * self.y + self.x

        # update other coordinates belonging to car
        for x in range (0, self.length):
            coordinates[list_position][0] = bool
            coordinates[list_position][1] = car
            list_position += self.increase_nr

        return coordinates
