# some functions that can be used by multiple algorithms


def won(board):

    # check if car can move through exit
    list_pos = board.width * board.cars[0].y + board.cars[0].x
    checkpos = int(list_pos) + 2

    # check if redcar is directly in front of exit
    if list_pos == (board.width * board.exity + board.exitx):
        print("game has been won in {} turns with the following moves: {}.".format(len(board.moves), board.moves))
        return True

    # checks coordinates between exit and redcar
    for x in range(checkpos, ((board.width * board.exity + board.exitx) + 2)):

        if board.coordinates[x] == True:
            break

        # checks if coordinate before exit is empty
        elif x == ((board.width * board.exity + board.exitx) + 1) and board.coordinates[x] == False:
            print("game has been won in {} turns with the following moves: {}.".format(len(board.moves), board.moves))
            return True

    # return false if not won
    return False
