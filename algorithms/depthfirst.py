import copy
from code.helpers import won
from code.helpers import visualisation


class Depth_first(object):

    def __init__(self, board, bound):

        self.board = board

        # initialise stack
        self.stack = [self.board]

        # turn counter
        self.turns = 0

        # initialise archive (lists of coordinates)
        self.archive = {}

        # checks if bound has been given
        self.bound = bound


    def depthfirst(self):

        def next_child():

            # check if stack is empty
            if len(self.stack) == 0:
                print("Stack is empty, this probably means you should increase your bound!")
                return 1

            # grab top of stack
            node = self.stack[-1]

            # iterate over every car on board
            for j in range(len(node.cars)):

                # do nothing if no bound has been given
                if not self.bound:
                    pass

                # breaks if bound has been reached
                elif len(node.moves) == int(self.bound):
                    break

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
                            new_node.move(new_node.cars[j], k)

                            # check if new board is in archive
                            if "{}".format(new_node.coordinates) in self.archive:

                                # check turns of board in archive
                                if self.archive.get("{}".format(new_node.coordinates), None) > len(new_node.moves):

                                    # append board to archive (value = moves played on board)
                                    self.archive["{}".format(new_node.coordinates)] = len(new_node.moves)

                                    # check if game has been won
                                    if won(new_node) == True:
                                        return True

                                    # insert new node in stack
                                    visualisation(new_node)
                                    print("")
                                    self.stack.insert(0, new_node)
                                    return False

                                # if board has been encountered at an earlier stage in the tree before
                                else:
                                    pass

                            else:

                                # append board to archive (value = moves played on board)
                                self.archive["{}".format(new_node.coordinates)] = len(new_node.moves)

                                # check if game has been won
                                if won(new_node) == True:
                                    return True

                                # insert new node in stack
                                self.stack.insert(0, new_node)
                                return False

            # delete child if it's not the winning board
            self.stack.pop()
            return False

        # if not won, move to next child
        while next_child() == False:
            pass
