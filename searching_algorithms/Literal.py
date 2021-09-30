class Literal:
    '''
        This class is for implenting a Literal.
    '''
    def __init__(self, value, is_not):
        '''
            Arguments:
            ----------
                value: Use 0 for a, 1 for b, 2 for c and 3 for d
                is_not: Boolean whether the literal is a negation
                        or not.
        '''
        self.value = value
        self.is_not = is_not
    
    def calculate_value(self, node):
        '''
            This function calculates the value of the Literal
            at the given value of the variable.
            
            Arguments:
            ---------
                - Node: Node at which the value of the Literal
                        is to be calculated.
            
            Returns:
            -------
                The calculated value of the literal.
        '''
        # If the Literal is negation, then calculate the negation
        if self.is_not:
            return node[self.value]^1
        else:
            return node[self.value]
            
    def __str__(self):
        '''
            This function specifies how to print the Literal.
        '''
        variables = ["a", "b", "c", "d"]
        return "~" + variables[self.value] if self.is_not else variables[self.value]
    
    def __eq__(self, other):
        '''
            This function specifies how to check equality of two Literal
            objects.
        '''
        if isinstance(other, Literal):
            return self.value == other.value and self.is_not == other.is_not
        return NotImplemented
        
    def __key(self):
        return (self.value, self.is_not)
        
    def __hash__(self):
        '''
            This function specifies how to hash a Literal object.
        '''
        return hash(self.__key())