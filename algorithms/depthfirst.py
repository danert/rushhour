import copy


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
            print("testtttt")
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

                        # add child to stack
                        else:
                            new_node = copy.deepcopy(node)
                            new_node.move(node.cars[j], k)

                            # check if new board is in archive
                            if "{}".format(new_node.coordinates) in self.archive:
                                pass

                            else:
                                # append board to archive
                                self.archive["{}".format(new_node.coordinates)] = new_node.coordinates

                                # check if car can move through exit
                                list_pos = new_node.width * new_node.cars[0].y + new_node.cars[0].x
                                checkpos = int(list_pos) + 2

                                # check if redcar is directly in front of exit
                                if list_pos == (original_node.width * original_node.exity + original_node.exitx):
                                    print("game has been won in {} turns with the following moves: {}.".format(self.turns, original_nodelist[i].moves))
                                    return True

                                # checks coordinates between exit and redcar
                                for x in range(checkpos, ((new_node.width * new_node.exity + new_node.exitx) + 2)):

                                    if new_node.coordinates[x] == True:
                                        break

                                    # checks if coordinate before exit is empty
                                    elif x == ((new_node.width * new_node.exity + new_node.exitx) + 1) and new_node.coordinates[x] == False:
                                        print("game has been won in {} turns with the following moves: {}.".format(len(new_node.turns), new_node.moves))
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
