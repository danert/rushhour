# algorithm that returns a random picked car and random distance the car can move
from code.board import Board
from random import randint
from code.helpers import won
from code.helpers import visualisation
import sys


class Random(object):

    def __init__(self, board):
        self.board = board

        # turn counter
        self.turns = 0

    def play(self):

        # if game hasn't been won yet, move a car
        while not won(self.board):

            # let the algorithm choose a move
            random_move = self.random_move()
            random_car = random_move[0]
            random_distance = random_move[1]

            # move car
            self.board.move(self.board.cars[random_car], random_distance)

            # increase turn counter
            self.turns = self.turns + 1

            #print("game has been won in {} turns with the following moves: {}.".format(self.turns, self.board.moves))
            visualisation(self.board)
            print("turn ", self.turns)
            sys.stdout.flush()
            print("change: {}.".format(self.board.moves[self.turns - 1]))

            #if self.board.width == 6:
            #print(board.coordinates[0][1] + board.coordinates[1][1] + board.coordinates[2][1] + board.coordinates[3][1] + board.coordinates[4][1] + board.coordinates[5][1])
            #sys.stdout.flush()

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
