
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
        
