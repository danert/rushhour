from code.helpers import visualisation
from code.helpers import won
import copy

class Breadth_first(object):
    """Algorithm that finds a solution by traversing a tree, generation by
    generation. Checks for each node if it's a winning board, and creates
    every child for that board if it's not.

    Args:
        board (Board): board that needs to be solved

    Attributes:
        self.board (Board): board the game is played on
        self.nodes (list): list of nodes/boards that keeps expanding as more
        childs are added
        self.turns (int): keeps track of how many generations have been traversed
        self.archive (dict): keeps track of all the board formations that have
        been checked
    """

    def __init__(self, board):

        self.board = board

        # initialise list of nodes (each node is a new board)
        self.nodes = [self.board]

        # turn counter
        self.turns = 0

        # initialise archive (lists of coordinates)
        self.archive = {}

    def breadthfirst(self):
        """Moves down a generation in the tree. game.py calls this function
        each time a generation has been checked and the game hasn't been won yet.

        Returns:
            bool: True if game has been won, False if not yet won.
        """

        # reset original_nodelist
        original_nodelist = copy.deepcopy(self.nodes)

        # iterates through every node
        for i in range(len(original_nodelist)):

            # reset original_node
            original_node = original_nodelist[i]

            # check if game has been won
            if won(original_node) == True:
                return True

            # if game not won, create children of node
            # iterate over every car on board
            for j in range(len(original_node.cars)):

                # check possible moves of car
                distances = original_node.check_move(original_node.cars[j])

                # if car can't move, do nothing
                if distances[0] == 0 and distances[1] == 0:
                    pass

                else:

                    # iterate over every possible move
                    for k in range(distances[1], (distances[0] + 1)):

                        # do nothing if distance is zero
                        if k == 0:
                            pass

                        else:

                            # reset new_board
                            new_board = copy.deepcopy(original_node)

                            # move car and add new board to node list (DE MOVE FUNCTIE IN BOARD PRINT NU DE MOVES MAAR DAT MOET ER ANDERS UITZIEN, ZE MOVEN NIET ECHT)
                            new_board.move(new_board.cars[j], k)

                            # check if new board is in archive
                            if "{}".format(new_board.coordinates) in self.archive:
                                pass

                            else:
                                # append board to nodes list if not in archive
                                self.nodes.append(new_board)

                                # put board in archive
                                self.archive["{}".format(new_board.coordinates)] = 0

                                # show board in terminal
                                print("")
                                visualisation(new_board)

            # remove node from list
            self.nodes.remove(self.nodes[0])

        # increase turn counter
        self.turns = self.turns + 1

        print("turn ", self.turns)

        # let game.py know that game has not been won yet
        return False
