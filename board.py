from car import Car

class Board(object):
    def __init__(self):

        self.cars = []

    # loads problem/game
    def loadgame(self):

        # opens text file
        with open("problem.txt", "r") as f:

            self.width = int(f.readline())
            self.height = int(f.readline())

            self.coordinates = [False] * (self.width * self.height)

            f.readline()

            self.exitx = int(f.readline())
            self.exity = int(f.readline())

            f.readline()

            # creates red car
            length = int(f.readline())
            x = int(f.readline())
            y = int(f.readline())
            direction = f.readline()
            self.redcar = Car(length, x, y, direction)
            f.readline()

            # creates 'regular' cars until EOF
            while True:
                length = int(f.readline())
                x = int(f.readline())
                y = int(f.readline())
                direction = f.readline().strip()
                end = f.readline()

                # adds car to list
                car = Car(length, x, y, direction)
                self.cars.append(car)

                # if EOF, break
                if end == "":
                    break

    # move a car
    def move(self, car, distance):

        # print start coordinates
        print("car at ({},{})".format(car.x, car.y))

        # change start coordinate
        if car.direction == "hor":
            car.x = car.x + distance
        else:
            car.y = car.y + distance

        # print new coordinates
        print("moved to ({},{})".format(car.x, car.y))
        # change previous coordinates
        car.remove_coordinates()

        # set coordinates in list
        car.set_coordinates()

    # if location of red car == exit, game has been won
    def won(self):
        if redcar.x == self.exitx and redcar.y == self.exity:
            return True
