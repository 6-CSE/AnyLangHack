class Node:
    def __init__(self):
        self.blocks = []            # Arrangement of blocks in the state
        self.h = None               # Value of heuristic for the ndoe
        self.parent = None
        self.child = None
        
    def __eq__(self, other):
        '''
            Function to compare the two objects of node.
        '''
        if other is not None:
            return self.blocks == other.blocks
            
    def __lt__(self, other):
        '''
            Function to check whether one node is less than the other node.
        '''
        if other is not None:
            return self.h < other.h