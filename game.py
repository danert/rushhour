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

        list_pos = board.width * board.cars[0].y + board.cars[0].x
        checkpos = int(list_pos) + 2

        # checks coordinates between exit and redcar
        for x in range(checkpos, 24):

            if board.coordinates[x] == True:
                return False

        return True

    # if game hasn't been won yet, move a car
    while not won():

        board.check_move(board.cars[4])

        # TEST move 1 tile
        #board.move(board.cars[2], 1)

        # increase turn counter
        turns = turns + 1

    # if won, print amount of steps
    turns = turns + 1
    print(f"amount of turns: {turns}")


if __name__ == '__main__':
    main()
