
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

    def set_coordinates(self, coordinates, width):

        # number of first coordinate
        list_position = width * self.y + self.x



        # set coordinate as taken in list
        coordinates[list_position][0] = True
        coordinates[list_position][1] = self.id

        # calculate other coordinates belonging to cars
        if self.length == 2 and self.direction == "hor":
            list_position += 1
            coordinates[list_position][0] = True
            coordinates[list_position][1] = self.id

        elif self.length == 2 and self.direction == "ver":
            list_position += width
            coordinates[list_position][0] = True
            coordinates[list_position][1] = self.id

        elif self.length == 3 and self.direction == "hor":
            list_position += 1
            coordinates[list_position][0] = True
            coordinates[list_position][1] = self.id
            list_position += 1
            coordinates[list_position][0] = True
            coordinates[list_position][1] = self.id

        elif self.length == 3 and self.direction == "ver":
            list_position += width
            coordinates[list_position][0] = True
            coordinates[list_position][1] = self.id
            list_position += width
            coordinates[list_position][0] = True
            coordinates[list_position][1] = self.id

        return coordinates

    def remove_coordinates(self, coordinates, width):

        # number of first coordinate
        list_position = width * self.y + self.x

        # set coordinate as taken in list
        coordinates[list_position][0] = False
        coordinates[list_position][1] = 0

        # calculate other coordinates belonging to cars
        if self.length == 2 and self.direction == "hor":
            list_position += 1
            coordinates[list_position][0] = False
            coordinates[list_position][1] = 0

        elif self.length == 2 and self.direction == "ver":
            list_position += width
            coordinates[list_position][0] = False
            coordinates[list_position][1] = 0

        elif self.length == 3 and self.direction == "hor":
            list_position += 1
            coordinates[list_position][0] = False
            coordinates[list_position][1] = 0
            list_position += 1
            coordinates[list_position][0] = False
            coordinates[list_position][1] = 0

        elif self.length == 3 and self.direction == "ver":
            list_position += width
            coordinates[list_position][0] = False
            coordinates[list_position][1] = 0
            list_position += width
            coordinates[list_position][0] = False
            coordinates[list_position][1] = 0

        return coordinates
