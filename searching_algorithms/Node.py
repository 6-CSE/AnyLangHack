class Node:
    '''
        This class implements the Node i.e. state of
        all the variables.
    '''
    def __init__(self, values):
        '''
            Arguments:
            ----------
                - values: List of binary values for each variable
                          For example, [0, 0, 0, 0] represents that 
                          variables a,b,c,d are False. 
        '''
        self.values = values
        self.e = None
        
    def __eq__(self, other):
        '''
            Function to compare the two objects of node.
        '''
        if other is not None:
            return self.values == other.values
            
    def __lt__(self, other):
        '''
            Function to check whether one node is less than 
            the other node.
        '''
        if other is not None:
            return self.e < other.e
            
    def __str__(self):
        '''
            This function specifies how to print a Node object.
        '''
        return str(self.values)