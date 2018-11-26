from code.board import Board
from code.car import Car
from algorithms.random import Random

filename = "data/problem2.txt"

def main():

    # make new board
    board = Board(filename)
    board.loadgame()

    # turn counter
    turns = 0

    # if car can drive through exit, game has been won
    def won():

        list_pos = board.width * board.cars[0].y + board.cars[0].x
        checkpos = int(list_pos) + 2

        # checks coordinates between exit and redcar
        for x in range(checkpos, 24):

            if board.coordinates[x] == True:
                return False

        return True

    # if game hasn't been won yet, move a car
    while not won():

        # initialise random algorithm
        random = Random(board)

        # let the algorithm choose a move
        random_move = random.random_move()
        random_car = random_move[0]
        random_distance = random_move[1]

        # move car
        board.move(board.cars[random_car], random_distance)

        # increase turn counter
        turns = turns + 1

        print("turn ", turns)

    # if won, print amount of steps
    turns = turns + 1
    print("amount of turns: {}".format(turns))


if __name__ == '__main__':
    main()
