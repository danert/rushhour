
class Board:
    def __init__(self):
        self.width
        self.height
        self.exitx
        self.exity
        self.cars = []
        self.redcar

        # how many turns have been made
        self.turns = 0

        # loads problem/game
        def loadgame():

            # opens text file
            with open("problem.txt", "r") as f:

                width = f.readline()
                height = f.readline()
                f.readline()

                self.exitx = f.readline()
                self.exity = f.readline()

                # creates red car
                length = f.readline()
                x = f.readline()
                y = f.readline()
                direction = f.readline()
                self.redcar = Car(length, x, y, direction)
                f.readline()

                # creates 'regular' cars until EOF
                while True:
                    length = f.readline()
                    x = f.readline()
                    y = f.readline()
                    direction = f.readline()
                    end = f.readline()

                    # adds car to list
                    car = Car(length, x, y, direction)
                    self.cars.append(car)

                    # if EOF, break
                    if end == "":
                        break

        # if location of red car == exit, game has been won
        def won():
            if redcar.x == self.exitx and redcar.y == self.exity:
                return True


if __name__ == '__main__':
    self.loadgame()

    # if game hasn't been won yet, move a car
    while not won():
        # increase turn counter
        self.turns = self.turns + 1

    # if won, print amount of steps
    print(self.turns)
