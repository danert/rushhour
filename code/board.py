from code.car import Car

class Board(object):
    """A board of Rush Hour on which the game can be played.

    Args:
        filename (str): name and location of the problem that needs to be solved

    Attributes:
        self.cars (list): a list of cars that are placed on the board
        self.filename (str): the name of the problem that needs to be solved
        self.id (int): integer that increases when new cars are 'placed' on the
        board and is used to give each car a unique id
        self.coordinates (list): list that stores info about each coordinate
        on the board; is it occupied, and if so, by what car
        self.moves (list): contains all the moves that have been made on the board
        self.width (int): width of the board
        self.height (int): height of the board
        self.exitx (int): x-coordinate of the tile before the exit
        self.exity (int): y-coordinate of the tile before the exit
    """

    def __init__(self, filename):

        self.cars = []
        self.filename = filename
        self.id = 0
        self.coordinates = []

        # list that keeps track of all the made moves
        self.moves = []

    # loads problem/game
    def loadgame(self):
        """Loads information (height and width and location of exit) and a list
        of cars from a textfile and uses these to initialise the board. Information
        about cars from the textfile is used to create a list of cars on the board.
        """

        # opens text file
        with open(self.filename, "r") as f:

            # initialise width and height of board
            self.width = int(f.readline().strip())
            self.height = int(f.readline().strip())

            # make list of coordinates with id for each car
            for p in range(self.width * self.height):
                spot = [False, 0]
                self.coordinates.append(spot)

            f.readline()

            self.exitx = int(f.readline().strip())
            self.exity = int(f.readline().strip())

            f.readline()

            # creates cars until EOF
            while True:
                length = int(f.readline().strip())
                x = int(f.readline().strip())
                y = int(f.readline().strip())
                direction = f.readline().strip()
                end = f.readline()
                self.id = self.id + 1

                # adds car to list
                car = Car(length, x, y, direction, self.width, self.id)
                self.coordinates = car.update_coordinates(self.coordinates, "set")
                self.cars.append(car)

                # if EOF, break
                if end == "":
                    break

    # checks if move is possible
    def check_move(self, car):
        """Checks which possible moves a given car can perform.

        Args:
            car (Car): car on the board of which the possible moves are checked

        Returns:
            int: amount of spots the car can move up or to the right
            int: amount of spots the car can move up or to the left
        """

        if car.direction == "hor":
            coordinate = car.x
            addition = 1
        else:
            coordinate = car.y
            addition = self.width

        # x-coordinates of first spots next to car
        first_pos_coordinate = coordinate + car.length
        first_neg_coordinate = coordinate - 1

        # list position of car
        car_pos = self.width * car.y + car.x

        # first position right of or above car
        first_pos_position = car_pos + (car.length * addition)

        # first position left of or below car
        first_neg_position = car_pos - addition

        # initialise distances car can move
        pos_distance = 0
        neg_distance = 0

        # checks if car is standing against right or upper wall
        if first_pos_coordinate == self.width:

            # move not possible
            pass

        # if car is not standing against wall
        else:
            for x in range(first_pos_coordinate, self.width):

                # if car is blocked, stop
                if self.coordinates[first_pos_position][0] == True:
                    break

                # if free space, update distance
                else:
                    pos_distance = pos_distance + 1
                    first_pos_position = first_pos_position + addition

        # check move to left or down
        if first_neg_coordinate == -1:

            # car is standing against left or bottom wall
            pass

        else:
            for x in range(-1, first_neg_coordinate):

                if self.coordinates[first_neg_position][0] == True:
                    break

                else:
                    neg_distance = neg_distance - 1
                    first_neg_position = first_neg_position - addition

        # return distances
        return [pos_distance, neg_distance]

    # move a car
    def move(self, car, distance):
        """Move a given car a given distance.

        Args:
            car (Car): the car on the board that needs to be moved
            distance (int): the amount of coordinates the car needs to move
            (positive if to the right or up, negative if to the left or down)
        """


        # grab begin coordinates
        begin_x = car.x
        begin_y = car.y

        # change previous coordinates
        self.coordinates = car.update_coordinates(self.coordinates, "remove")

        # change start coordinate
        if car.direction == "hor":
            car.x = car.x + distance
        else:
            car.y = car.y + distance

        # set coordinates in list
        self.coordinates = car.update_coordinates(self.coordinates, "set")

        # grab end coordinates
        end_x = car.x
        end_y = car.y

        move = "({},{}) to ({},{})".format(begin_x, begin_y, end_x, end_y)

        # add move to movelist
        self.moves.append(move)
