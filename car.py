from board import Board

class Car(object):
    def __init__(self, length, x, y, direction):
        self.x = x
        self.y = y
        self.length = length

        # horizontal or vertical direction
        self.direction = direction

    def set_coordinates(self):

        # number of first coordinate
        list_position = board.width * self.y + self.x

        # set coordinate as taken in list
        board.coordinates[list_position] = True

        # calculate other coordinates belonging to cars
        if self.length == 2 and self.direction == "hor":
            list_position += 1
            board.coordinates[list_position] = True

        elif self.length == 2 and self.direction == "ver":
            list_position += board.width
            board.coordinates[list_position] = True

        elif self.length == 3 and self.direction == "hor":
            list_position += 1
            board.coordinates[list_position] = True
            list_position += 1
            board.coordinates[list_position] = True

        elif self.length == 3 and self.direction == "ver":
            list_position += board.width
            board.coordinates[list_position] = True
            list_position += board.width
            board.coordinates[list_position] = True

    # sets coordinates to false
    def remove_coordinates(self):

        # number of first coordinate
        list_position = board.width * self.y + self.x

        # set coordinate as taken in list
        board.coordinates[list_position] = False

        if self.length == 2 and self.direction == "hor":
            list_position += 1
            board.coordinates[list_position] = False

        elif self.length == 2 and self.direction == "ver":
            list_position += board.width
            board.coordinates[list_position] = False

        elif self.length == 3 and self.direction == "hor":
            list_position += 1
            board.coordinates[list_position] = False
            list_position += 1
            board.coordinates[list_position] = False

        elif self.length == 3 and self.direction == "ver":
            list_position += board.width
            board.coordinates[list_position] = False
            list_position += board.width
            board.coordinates[list_position] = False
