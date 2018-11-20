from code.board import Board
from code.car import Car

filename = "data/problem.txt"

def main():

    # make new board
    board = Board(filename)
    board.loadgame()

    # turn counter
    turns = 0

    # if car can drive through exit, game has been won
    def won():

        list_pos = board.width * board.redcar.y + board.redcar.x
        checkpos = int(list_pos) + 2

        # checks coordinates between exit and redcar
        for x in range(checkpos, 24):
            if board.coordinates[x] == True:
                return False

        return True

    # if game hasn't been won yet, move a car
    while not won():

        # TEST move 1 tile
        board.move(board.redcar, 1)

        # increase turn counter
        turns = turns + 1

    # if won, print amount of steps
    turns = turns + 1
    print(turns)


if __name__ == '__main__':
    main()
