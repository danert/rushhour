from code.board import Board
from code.helpers import visualisation
from code.helpers import won
from random import randint
import sys


class Random(object):
    """Algorithm that randomly chooses cars on a board and moves these a
    random amount of tiles. Stops if the red car can move through the exit
    on the board.

    Args:
        board (Board): the board that needs to be played/solved

    Attributes:
        self.board (Board): board that the game is played on
        self.turns (int): keeps track of how many moves have been done on the
        board

    """

    def __init__(self, board):
        self.board = board

        # turn counter
        self.turns = 0

    def play(self):
        """Main function of the algorithm. Picks a random car on the board that
        is able to move, and executes a random move with this car. Keeps on
        doing this until a solution has been found.
        """

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

            visualisation(self.board)
            print("turn ", self.turns)
            sys.stdout.flush()
            print("change: {}.".format(self.board.moves[self.turns - 1]))

        # if won, print amount of steps
        self.turns = self.turns + 1
        print("amount of turns: {}".format(self.turns))

    def random_move(self):
        """Picks a random car and checks if it is able to move. If it can't,
        pick another car until it finds one that can move. Then picks a random
        move that this car can execute.

        Returns:
            Car: car that can be moved
            int: random distance this car can move on the board
        """

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
