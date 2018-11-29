# algorithm that returns a random picked car and random distance the car can move
from code.board import Board
from random import randint


class Random(object):

    def __init__(self, board):
        self.board = board

        # turn counter
        self.turns = 0

    # if car can drive through exit, game has been won
    def won(self):

        board = self.board

        list_pos = board.width * board.cars[0].y + board.cars[0].x
        checkpos = int(list_pos) + 2

        # checks coordinates between exit and redcar (6x6: 24, 9x9: 45, 12x12:84)
        for x in range(checkpos, ((board.width * board.exity + board.exitx) + 2)):

            if board.coordinates[x] == True:
                return False

        return True


    def play(self):

        # if game hasn't been won yet, move a car
        while not self.won():

            # let the algorithm choose a move
            random_move = self.random_move()
            random_car = random_move[0]
            random_distance = random_move[1]

            # move car
            self.board.move(self.board.cars[random_car], random_distance)

            # increase turn counter
            self.turns = self.turns + 1

            print("turn ", self.turns)
            print("change: {}.".format(self.board.moves[self.turns - 1]))

        # if won, print amount of steps
        self.turns = self.turns + 1
        print("amount of turns: {}".format(self.turns))

    def random_move(self):

        # picks random car
        random_car = randint(0, (len(self.board.cars) - 1))

        # checks possible moves of random_car
        distances = self.board.check_move(self.board.cars[random_car])

        # if car cannot move, pick a new car
        while distances[0] == 0 and distances[1] == 0:
            random_car = randint(0, (len(self.board.cars) - 1))
            distances = self.board.check_move(self.board.cars[random_car])

        # chooses random distance
        random_distance = randint(distances[1], distances[0])

        # if distance = 0, try again
        while random_distance == 0:
            random_distance = randint(distances[1], distances[0])


        # returns random car and distance
        return [random_car, random_distance]
