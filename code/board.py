from code.car import Car

class Board(object):
    def __init__(self, filename):

        self.cars = []
        self.filename = filename

    # loads problem/game
    def loadgame(self):

        # opens text file
        with open(self.filename, "r") as f:

            self.width = int(f.readline())
            self.height = int(f.readline())

            self.coordinates = [False] * (self.width * self.height)

            f.readline()

            self.exitx = int(f.readline())
            self.exity = int(f.readline())

            f.readline()

            # creates cars until EOF
            while True:
                length = int(f.readline())
                x = int(f.readline())
                y = int(f.readline())
                direction = f.readline().strip()
                end = f.readline()

                # adds car to list
                car = Car(length, x, y, direction, self.width)
                self.coordinates = car.set_coordinates(self.coordinates, self.width)
                self.cars.append(car)

                # if EOF, break
                if end == "":
                    break

    # checks if move is possible
    def check_move(self, car):

        # horizontal movement
        if car.direction == "hor":

            # x-coordinates of first spots next to car
            first_right_x = car.x + car.length
            first_left_x = car.x - 1

            # first position right of car
            position_right = car.list_position + car.length

            # first position left of car
            position_left = car.list_position - 1

            # initialise distances car can move
            distance_right = 0
            distance_left = 0

            # checks if car is standing against right wall
            if first_right_x == self.width:

                # move not possible
                pass

            # if car is not standing against wall
            else:
                for x in range(first_right_x, self.width):

                    # if car is blocked, stop
                    if self.coordinates[position_right] == True:
                        break

                    # if free space, update distance
                    else:
                        distance_right = distance_right + 1
                        position_right = position_right + 1

            # check move to left
            if first_left_x == -1:
                print("Cannot move left")

                # car is standing against left wall
                pass

            else:
                for x in range(first_left_x, -1):
                    if self.coordinates[position_left] == True:
                        break

                    else:
                        distance_left = distance_right - 1
                        position_left = position_right - 1

        # if car is vertical
        else:

            # y-coordinates of first spots next to car
            first_above_y = car.y + car.length
            first_below_y = car.y - 1

            # first position above car
            position_above = car.list_position + (car.length * self.width)

            # first position left of car
            position_below = car.list_position - self.width

            # initialise distances car can move
            distance_above = 0
            distance_below = 0

            # checks if car is standing against upper wall
            if first_above_y == self.self.height:

                # move not possible
                pass

            # if car is not standing against upper wall
            else:
                for x in range(first_above_y, self.height):

                    # if car is blocked, stop
                    if self.coordinates[position_above] == True:
                        break

                    # if free space, update distance
                    else:
                        distance_above = distance_above + 1
                        position_above = position_above + self.width

            # check move down
            if first_below_y == -1:

                # car is standing against lower wall
                pass

            else:
                for x in range(first_below_y, -1):
                    if self.coordinates[position_below] == True:
                        break

                    else:
                        distance_below = distance_below - 1
                        position_below = position_below - self.width

    # move a car
    def move(self, car, distance):

        # print start coordinates
        print("car at ({},{})".format(car.x, car.y))

        # change previous coordinates
        car.remove_coordinates(self.coordinates, self.width)

        # change start coordinate
        if car.direction == "hor":
            car.x = car.x + distance
        else:
            car.y = car.y + distance

        # print new coordinates
        print("moved to ({},{})".format(car.x, car.y))


        # set coordinates in list
        car.set_coordinates(self.coordinates, self.width)
