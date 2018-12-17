
class Car(object):
    """An object that's a part of a game of Rush Hour. Cars occupy coordinates
    on a board and can move on this board.

    Args:
        length (int): the length of the car (can be 2 or 3)
        x (int): the x-coordinate of the car that's the closed to the bottom
        left corner of the board
        y (int): the y-coordinate of the car that's the closed to the bottom
        left corner of the board
        direction (str): shows if the car is standing horizontally or vertically
        (can be "hor" or "ver")
        width (int): width of the board the car is standing on
        id (int): unique integer that's used to identify the car

    Attributes:
        self.list_position (int): coordinate the car is standing on converted to
        the position in the list of coordinates of the board
        other attributes: see Args above
    """

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
