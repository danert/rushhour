import copy

class Breadth_first(object):

    def __init__(self, board):

        self.board = board

        # initialise list of nodes (each node is a new board)
        self.nodes = [self.board]

        # turn counter
        self.turns = 0

        # initialise archive (lists of coordinates)
        self.archive = {}

    # move down a generation
    def breadthfirst(self):

        # reset original_nodelist
        original_nodelist = copy.deepcopy(self.nodes)

        # iterates through every node
        for i in range(len(original_nodelist)):

            # reset original_node
            original_node = original_nodelist[i]

            # check if car can move through exit
            list_pos = original_nodelist[i].width * original_nodelist[i].cars[0].y + original_nodelist[i].cars[0].x
            checkpos = int(list_pos) + 2

            # checks coordinates between exit and redcar
            for x in range(checkpos, ((original_nodelist[i].width * original_nodelist[i].exity + original_nodelist[i].exitx) + 2)):

                if original_nodelist[i].coordinates[x] == True:
                    break

                # checks if coordinate before exit is empty
                elif x == ((original_nodelist[i].width * original_nodelist[i].exity + original_nodelist[i].exitx) + 1) and original_nodelist[i].coordinates[x] == False:
                    print("game has been won in {} turns with the following moves: {}.".format(self.turns, original_nodelist[i].moves))
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
                                self.archive["{}".format(new_board.coordinates)] = new_board.coordinates

            # remove node from list
            self.nodes.remove(self.nodes[0])

        # increase turn counter
        self.turns = self.turns + 1

        print("turn ", self.turns)

        # let game.py know that game has not been won yet
        return False
