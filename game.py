from code.board import Board
from code.car import Car
from algorithms.random_move import Random
from algorithms.breadthfirst import Breadth_first
from algorithms.depthfirst import Depth_first

filename = "data/problem2.txt"

def main():

    # make new board
    board = Board(filename)
    board.loadgame()

    # random algorithm
    # random = Random(board)
    # random.play()

    # breadthfirst algorithm
    # breadth_first = Breadth_first(board)
    # while breadth_first.breadthfirst() == False:
    #     breadth_first.breadthfirst()

    # depthfirst algorithms
    depth_first = Depth_first(board)
    depth_first.depthfirst()


if __name__ == '__main__':
    main()
