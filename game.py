from code.board import Board
from code.car import Car
from random import randint

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

        # picks random car
        random_car = randint(0, (len(board.cars) - 1))

        # checks possible moves of random_car
        distances = board.check_move(board.cars[random_car])

        # if car cannot move, pick a new car
        while distances[0] == 0 and distances[1] == 0:
            random_car = randint(0, (len(board.cars) - 1))
            distances = board.check_move(board.cars[random_car])

        # chooses random distance
        random_distance = randint(distances[1], distances[0])

        # if distance = 0, try again
        while random_distance == 0:
            random_distance = randint(distances[1], distances[0])

        # move car
        board.move(board.cars[random_car], random_distance)

        # increase turn counter
        turns = turns + 1

    # if won, print amount of steps
    turns = turns + 1
    print("amount of turns: {}".format(turns))


if __name__ == '__main__':
    main()
