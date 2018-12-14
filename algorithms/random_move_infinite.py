# algorithm that returns a random picked car and random distance the car can move
from code.board import Board
from random import randint
from code.helpers import won
from code.helpers import visualisation
import copy


class Randominfinite(object):

    def __init__(self, board):
        self.board = board
        self.boardcopy = copy.deepcopy(board)


    def play(self):

        # if game hasn't been won yet, move a car
        while not won(self.board):

            # let the algorithm choose a move
            random_move = self.random_move()
            random_car = random_move[0]
            random_distance = random_move[1]
            #visualisation(board)

            # move car
            self.board.move(self.board.cars[random_car], random_distance)

        while True:


            # start algorithm again with new upper bound
            self.bound = len(self.board.moves)
            self.board = copy.deepcopy(self.boardcopy)

            while not won(self.board):

                # let the algorithm choose a move
                random_move = self.random_move()
                random_car = random_move[0]
                random_distance = random_move[1]

                # move car
                self.board.move(self.board.cars[random_car], random_distance)

                if len(self.board.moves) == self.bound:
                    break



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
