from board import Board
from car import Car


def main():

    # make new board
    board = Board()
    board.loadgame()

    # turn counter
    turns = 0

    # if location of red car == exit, game has been won
    def won():
        if board.redcar.x == board.exitx and board.redcar.y == board.exity:
            return True

    # if game hasn't been won yet, move a car
    #while not won():
        # increase turn counter
    turns = turns + 1

    # TEST
    board.move(board.cars[1], 1)

    # if won, print amount of steps
    print(turns)

    def checkmove():
        pass



if __name__ == '__main__':
    main()
