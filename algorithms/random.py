# algorithm that returns a random picked car and random distance the car can move
from code.board import Board
from random import randint


class Random(object):

    def __init__(self, board):
        self.board = board

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
