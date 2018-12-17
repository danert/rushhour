from algorithms.breadthfirst import Breadth_first
from algorithms.depthfirst import Depth_first
from algorithms.random_move import Random
from algorithms.random_move_infinite import Randominfinite
from code.board import Board
from code.car import Car
import sys


def main():

    problem_nr = sys.argv[1]

    # checks if problem user has chosen exists
    if int(problem_nr) < 1 or int(problem_nr) > 7:
        print("Problem doesn't exist, please enter a number between 1 and 7.")
        return 1

    # converts chosen problem to filename
    filename = "data/problem{}.txt".format(problem_nr)

    # make new board
    board = Board(filename)
    board.loadgame()

    # random algorithm
    if sys.argv[2] == "random":
        random = Random(board)
        random.play()

    # breadthfirst algorithm
    elif sys.argv[2] == "bf":
        breadth_first = Breadth_first(board)
        while breadth_first.breadthfirst() == False:
            breadth_first.breadthfirst()

    # depthfirst algorithm
    elif sys.argv[2] == "df":

        # if bound has not been given
        if len(sys.argv) == 3:
            depth_first = Depth_first(board, False)

        # give bound to df if it has been given
        else:
            bound = sys.argv[3]
            depth_first = Depth_first(board, bound)

        depth_first.depthfirst()

    # plays random algorithm again and again, keeps finding a shorter solution
    elif sys.argv[2] == "randominf":
        randominf = Randominfinite(board)
        randominf.play()

    # warn user if invalid algorithm has been chosen
    else:
        print("Invalid algorithm entered, please choose between random, randominf, bf and df.")
        return 1


if __name__ == '__main__':
    main()
