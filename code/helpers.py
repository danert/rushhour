def won(board):
    """Checks if the red car can move through the exit (if so, game has been won).

    Args:
        board (Board): board that this function needs to check

    Returns:
        boolean: True if game has been won on the board, False if not yet won
    """

    # grab position of car and position that needs to be checked
    list_pos = board.width * board.cars[0].y + board.cars[0].x
    checkpos = int(list_pos) + 2

    # check if redcar is directly in front of exit
    if list_pos == (board.width * board.exity + board.exitx):
        print("game has been won in {} turns with the following moves: {}.".format(len(board.moves), board.moves))
        return True

    # checks coordinates between exit and redcar
    for x in range(checkpos, ((board.width * board.exity + board.exitx) + 2)):

        if board.coordinates[x][0] == True:
            break

        # checks if coordinate before exit is empty
        elif x == ((board.width * board.exity + board.exitx) + 1) and board.coordinates[x][0] == False:
            print("game has been won in {} turns with the following moves: {}.".format(len(board.moves), board.moves))
            return True

    # return false if not won
    return False


def visualisation(board):
    """Prints a visualisation of the given board to the terminal. 0 means the coordinate
    is empty (there's no car on it), 1 means the coordinate is occupied by the red car and
    any other number means the coordinate is occupied by a car with that id.

    Args:
        board (Board): board that needs to be visualised
    """


    if board.width == 6:

        print(board.coordinates[30][1], " ", board.coordinates[31][1], " ", board.coordinates[32][1], " ", board.coordinates[33][1], " ", board.coordinates[34][1], " ", board.coordinates[35][1])
        print(" ")
        print(board.coordinates[24][1], " ", board.coordinates[25][1], " ", board.coordinates[26][1], " ", board.coordinates[27][1], " ", board.coordinates[28][1], " ", board.coordinates[29][1])
        print(" ")
        print(board.coordinates[18][1], " ", board.coordinates[19][1], " ", board.coordinates[20][1], " ", board.coordinates[21][1], " ", board.coordinates[22][1], " ", board.coordinates[23][1])
        print(" ")
        print(board.coordinates[12][1], " ", board.coordinates[13][1], " ", board.coordinates[14][1], " ", board.coordinates[15][1], " ", board.coordinates[16][1], " ", board.coordinates[17][1])
        print(" ")
        print(board.coordinates[6][1], " ", board.coordinates[7][1], " ", board.coordinates[8][1], " ", board.coordinates[9][1], " ", board.coordinates[10][1], " ", board.coordinates[11][1])
        print(" ")
        print(board.coordinates[0][1], " ", board.coordinates[1][1], " ", board.coordinates[2][1], " ", board.coordinates[3][1], " ", board.coordinates[4][1], " ", board.coordinates[5][1])
        print(" ")

    if board.width == 9:

        print(board.coordinates[72][1], " ", board.coordinates[73][1], " ", board.coordinates[74][1], " ", board.coordinates[75][1], " ", board.coordinates[76][1], " ", board.coordinates[77][1], " ", board.coordinates[78][1], " ", board.coordinates[79][1], " ", board.coordinates[80][1])
        print(" ")
        print(board.coordinates[63][1], " ", board.coordinates[64][1], " ", board.coordinates[65][1], " ", board.coordinates[66][1], " ", board.coordinates[67][1], " ", board.coordinates[68][1], " ", board.coordinates[69][1], " ", board.coordinates[70][1], " ", board.coordinates[71][1])
        print(" ")
        print(board.coordinates[54][1], " ", board.coordinates[55][1], " ", board.coordinates[56][1], " ", board.coordinates[57][1], " ", board.coordinates[58][1], " ", board.coordinates[59][1], " ", board.coordinates[60][1], " ", board.coordinates[61][1], " ", board.coordinates[62][1])
        print(" ")
        print(board.coordinates[45][1], " ", board.coordinates[46][1], " ", board.coordinates[47][1], " ", board.coordinates[48][1], " ", board.coordinates[49][1], " ", board.coordinates[50][1], " ", board.coordinates[51][1], " ", board.coordinates[52][1], " ", board.coordinates[53][1])
        print(" ")
        print(board.coordinates[36][1], " ", board.coordinates[37][1], " ", board.coordinates[38][1], " ", board.coordinates[39][1], " ", board.coordinates[40][1], " ", board.coordinates[41][1], " ", board.coordinates[42][1], " ", board.coordinates[43][1], " ", board.coordinates[44][1])
        print(" ")
        print(board.coordinates[27][1], " ", board.coordinates[28][1], " ", board.coordinates[29][1], " ", board.coordinates[30][1], " ", board.coordinates[31][1], " ", board.coordinates[32][1], " ", board.coordinates[33][1], " ", board.coordinates[34][1], " ", board.coordinates[35][1])
        print(" ")
        print(board.coordinates[18][1], " ", board.coordinates[19][1], " ", board.coordinates[20][1], " ", board.coordinates[21][1], " ", board.coordinates[22][1], " ", board.coordinates[23][1], " ", board.coordinates[24][1], " ", board.coordinates[25][1], " ", board.coordinates[26][1])
        print(" ")
        print(board.coordinates[9][1], " ", board.coordinates[10][1], " ", board.coordinates[11][1], " ", board.coordinates[12][1], " ", board.coordinates[13][1], " ", board.coordinates[14][1], " ", board.coordinates[15][1], " ", board.coordinates[16][1], " ", board.coordinates[17][1])
        print(" ")
        print(board.coordinates[0][1], " ", board.coordinates[1][1], " ", board.coordinates[2][1], " ", board.coordinates[3][1], " ", board.coordinates[4][1], " ", board.coordinates[5][1], " ", board.coordinates[6][1], " ", board.coordinates[7][1], " ", board.coordinates[8][1])
        print(" ")



    # if board.width == 12: (crasht nog, en print nog op z'n kop)
    #     print(board.coordinates[0][1], " ", board.coordinates[1][1], " ", board.coordinates[2][1], " ", board.coordinates[3][1], " ", board.coordinates[4][1], " ", board.coordinates[5][1], " ", board.coordinates[6][1], " ", board.coordinates[7][1], " ", board.coordinates[8][1], " ", board.coordinates[9][1], " ", board.coordinates[10][1], " ", board.coordinates[11][1])
    #     print(" ")
    #     print(board.coordinates[12][1], " ", board.coordinates[13][1], " ", board.coordinates[14][1], " ", board.coordinates[15][1], " ", board.coordinates[16][1], " ", board.coordinates[17][1], " ", board.coordinates[18][1], " ", board.coordinates[19][1], " ", board.coordinates[20][1], " ", board.coordinates[21][1], " ", board.coordinates[22][1], " ", board.coordinates[23][1])
    #     print(" ")
    #     print(board.coordinates[24][1], " ", board.coordinates[25][1], " ", board.coordinates[26][1], " ", board.coordinates[27][1], " ", board.coordinates[28][1], " ", board.coordinates[29][1], " ", board.coordinates[30][1], " ", board.coordinates[31][1], " ", board.coordinates[32][1], " ", board.coordinates[33][1], " ", board.coordinates[34][1], " ", board.coordinates[35][1])
    #     print(" ")
    #     print(board.coordinates[36][1], " ", board.coordinates[37][1], " ", board.coordinates[38][1], " ", board.coordinates[39][1], " ", board.coordinates[40][1], " ", board.coordinates[41][1], " ", board.coordinates[42][1], " ", board.coordinates[43][1], " ", board.coordinates[44][1]), " ", board.coordinates[45][1], " ", board.coordinates[46][1], " ", board.coordinates[47][1])
    #     print(" ")
    #     print(board.coordinates[48][1], " ", board.coordinates[49][1], " ", board.coordinates[50][1], " ", board.coordinates[51][1], " ", board.coordinates[52][1], " ", board.coordinates[53][1], " ", board.coordinates[54][1], " ", board.coordinates[55][1], " ", board.coordinates[56][1]), " ", board.coordinates[57][1], " ", board.coordinates[58][1], " ", board.coordinates[59][1])
    #     print(" ")
    #     print(board.coordinates[60][1], " ", board.coordinates[61][1], " ", board.coordinates[62][1] " ", board.coordinates[63][1], " ", board.coordinates[64][1], " ", board.coordinates[65][1], " ", board.coordinates[66][1], " ", board.coordinates[67][1], " ", board.coordinates[68][1]), " ", board.coordinates[69][1], " ", board.coordinates[70][1], " ", board.coordinates[71][1])
    #     print(" ")
    #     print(board.coordinates[72][1], " ", board.coordinates[73][1], " ", board.coordinates[74][1], " ", board.coordinates[75][1], " ", board.coordinates[76][1], " ", board.coordinates[77][1], " ", board.coordinates[78][1], " ", board.coordinates[79][1], " ", board.coordinates[80][1]), " ", board.coordinates[81][1], " ", board.coordinates[82][1], " ", board.coordinates[83][1])
    #     print(" ")
    #     print(board.coordinates[84][1], " ", board.coordinates[85][1], " ", board.coordinates[86][1], " ", board.coordinates[87][1], " ", board.coordinates[88][1], " ", board.coordinates[89][1], " ", board.coordinates[90][1], " ", board.coordinates[91][1], " ", board.coordinates[92][1]), " ", board.coordinates[93][1], " ", board.coordinates[94][1], " ", board.coordinates[95][1])
    #     print(" ")
    #     print(board.coordinates[96][1], " ", board.coordinates[97][1], " ", board.coordinates[98][1], " ", board.coordinates[99][1], " ", board.coordinates[100][1], " ", board.coordinates[101][1], " ", board.coordinates[102][1], " ", board.coordinates[103][1], " ", board.coordinates[104][1]), " ", board.coordinates[105][1], " ", board.coordinates[106][1], " ", board.coordinates[107][1])
    #     print(" ")
    #     print(board.coordinates[108][1], " ", board.coordinates[109][1], " ", board.coordinates[110][1], " ", board.coordinates[111][1], " ", board.coordinates[112][1], " ", board.coordinates[113][1], " ", board.coordinates[114][1], " ", board.coordinates[115][1], " ", board.coordinates[116][1]), " ", board.coordinates[117][1], " ", board.coordinates[118][1], " ", board.coordinates[119][1])
    #     print(" ")
    #     print(board.coordinates[120][1], " ", board.coordinates[121][1], " ", board.coordinates[122][1], " ", board.coordinates[123][1], " ", board.coordinates[124][1], " ", board.coordinates[125][1], " ", board.coordinates[126][1], " ", board.coordinates[127][1], " ", board.coordinates[128][1]), " ", board.coordinates[129][1], " ", board.coordinates[130][1], " ", board.coordinates[131][1])
    #     print(" ")
    #     print(board.coordinates[132][1], " ", board.coordinates[133][1], " ", board.coordinates[134][1], " ", board.coordinates[135][1], " ", board.coordinates[136][1], " ", board.coordinates[137][1], " ", board.coordinates[138][1], " ", board.coordinates[139][1], " ", board.coordinates[140][1]), " ", board.coordinates[141][1], " ", board.coordinates[142][1], " ", board.coordinates[143][1])
    #     print(" ")
