from code.board import Board
from code.car import Car
from algorithms.random_move import Random
from algorithms.breadthfirst import Breadth_first
from algorithms.depthfirst import Depth_first

filename = "data/problem2.txt"

# choose between random, bf and def
algorithm = "random"

def main():

    # make new board
    board = Board(filename)
    board.loadgame()

    # random algorithm
    if algorithm == "random":
        random = Random(board)
        random.play()

    # breadthfirst algorithm
    elif algorithm == "bf":
        breadth_first = Breadth_first(board)
        while breadth_first.breadthfirst() == False:
            breadth_first.breadthfirst()

    # depthfirst algorithm
    elif algorithm == "df":
        depth_first = Depth_first(board)
        depth_first.depthfirst()


if __name__ == '__main__':
    main()
