from code.board import Board
from code.car import Car
from algorithms.random_move import Random
from algorithms.breadthfirst import Breadth_first
from algorithms.depthfirst import Depth_first
from algorithms.random_move_infinite import Randominfinite

filename = "data/problem2.txt"

# choose between random, randominf, bf and df
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

    # plays random algorithm again and again, keeps finding a shorter solution
    elif algorithm == "randominf":
        randominf = Randominfinite(board)
        randominf.play()


if __name__ == '__main__':
    main()
