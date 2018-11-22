
class Car(object):
    def __init__(self, length, x, y, direction, width):
        self.x = x
        self.y = y
        self.length = length
        self.width = width
        self.list_position = width * self.y + self.x

        # horizontal or vertical direction
        self.direction = direction

    def set_coordinates(self, coordinates, width):

        # number of first coordinate
        self.list_position = width * self.y + self.x
        list_position = width * self.y + self.x

        # set coordinate as taken in list
        coordinates[list_position] = True

        # calculate other coordinates belonging to cars
        if self.length == 2 and self.direction == "hor":
            list_position += 1
            coordinates[list_position] = True

        elif self.length == 2 and self.direction == "ver":
            list_position += width
            coordinates[list_position] = True

        elif self.length == 3 and self.direction == "hor":
            list_position += 1
            coordinates[list_position] = True
            list_position += 1
            coordinates[list_position] = True

        elif self.length == 3 and self.direction == "ver":
            list_position += width
            coordinates[list_position] = True
            list_position += width
            coordinates[list_position] = True

        return coordinates

    def remove_coordinates(self, coordinates, width):

        # number of first coordinate
        list_position = width * self.y + self.x

        # set coordinate as taken in list
        coordinates[list_position] = False

        # calculate other coordinates belonging to cars
        if self.length == 2 and self.direction == "hor":
            list_position += 1
            coordinates[list_position] = False

        elif self.length == 2 and self.direction == "ver":
            list_position += width
            coordinates[list_position] = False

        elif self.length == 3 and self.direction == "hor":
            list_position += 1
            coordinates[list_position] = False
            list_position += 1
            coordinates[list_position] = False

        elif self.length == 3 and self.direction == "ver":
            list_position += width
            coordinates[list_position] = False
            list_position += width
            coordinates[list_position] = False

        return coordinates
