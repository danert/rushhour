from code.board import Board
from code.helpers import won
from code.helpers import visualisation
import copy
from random import randint


class Randominfinite(object):
    """Algorithm that randomly chooses cars on a board and moves these a random
    distance, similar to the random algorithm. When a game is won, the algorithm
    prints the solution and uses it as an upper bound. It will run the algorithm
    again and again until the upper bound is reached or a new game is won.
    Algorithm goes on until the user stops the algorithm; the algorithm will
    continuously search for a solution with a shorter amount of steps than the
    previous solution.

    Args:
        board (Board): the board that needs to be played/solved

    Attributes:
        self.board (Board): board that the game is played on
        self.boardcopy(Board): copy of the original board, used to reset the
        board when looking for a new solution
        self.bound (int): bound that is used to make sure new solutions that
        are found are shorter than previous solutions
    """

    def __init__(self, board):
        self.board = board
        self.boardcopy = copy.deepcopy(board)


    def play(self):
        """Main function of the algorithm. Picks a random car on the board that
        is able to move, and executes a random move with this car. Keeps on
        doing this until a solution has been found. After a solution has been
        found, it sets a new bound for itself and keeps looking for solutions
        again and again.
        """

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
