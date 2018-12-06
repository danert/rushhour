import copy
from code.helpers import won


class Depth_first(object):

    def __init__(self, board):

        self.board = board

        # initialise stack
        self.stack = [self.board]

        # turn counter
        self.turns = 0

        # initialise archive (lists of coordinates)
        self.archive = {}

    def depthfirst(self):

        def next_child():

            # grab top of stack
            node = self.stack[0]

            # iterate over every car on board
            for j in range(len(node.cars)):

                # check possible moves of car
                distances = node.check_move(node.cars[j])

                # if car can't move, do nothing
                if distances[0] == 0 and distances[1] == 0:
                    pass

                else:

                    # iterate over every possible move
                    for k in range(distances[1], (distances[0] + 1)):

                        # do nothing if distance is zero
                        if k == 0:
                            pass

                        # move car
                        else:
                            new_node = copy.deepcopy(node)
                            new_node.move(node.cars[j], k)

                            # check if new board is in archive
                            if "{}".format(new_node.coordinates) in self.archive:
                                pass

                            else:
                                # append board to archive
                                self.archive["{}".format(new_node.coordinates)] = new_node.coordinates

                                # check if game has been won
                                if won(new_node) == True:
                                    return True

                                # insert new node in stack
                                self.stack.insert(0, new_node)
                                return False

            # delete child if it's not the winning board
            self.stack.pop(0)
            return False

        # if not won, move to next child
        while next_child() == False:
            pass