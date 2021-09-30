import copy
from Node import Node

def move_gen(node, num_bits, clauses):
    '''
        This function accepts a state and returns all the states 
        that can be reached from the given state by changing num_bits.
        
        Arguments:
        ----------
            - node: node/state whose neighbours have to be found
            - num_bits: Number of bits to be changed
            - clauses: A list of clauses in the formula
            
        Returns:
        --------
            List of Valid neighbours/state which can be visited from
            the given state.
    '''
    neighbors = []
    
    # 1 bit to be changed
    if num_bits == 1:
        for i in range(len(node)):
            copy_node = copy.deepcopy(node)
            neighbors.append(Node(copy_node))  
            # Changing the value of the ith bit
            neighbors[i].values[i] = neighbors[i].values[i] ^ 1
            # Calculate the number of clauses satisfied
            neighbors[i].e = evaluate_node(neighbors[i], clauses)
            
    # 2 bits to be changed
    if num_bits == 2:
        for i in range(len(node)):
            for j in range(i+1, len(node)):
                copy_node = copy.deepcopy(node)
                # Changing the value of ith and jth bit
                copy_node[i] = copy_node[i] ^ 1
                copy_node[j] = copy_node[j] ^ 1
                neighbors.append(Node(copy_node))
                # Calculate the number of clauses satisfied
                neighbors[-1].e = evaluate_node(neighbors[-1], clauses)
    
    # 3 bits to be changed
    if num_bits == 3:
        # Reversing all bits
        node = [literal ^ 1 for literal in node]
        for i in range(len(node)):
            copy_node = copy.deepcopy(node)
            neighbors.append(Node(copy_node))
            # Changing the ith bit 
            neighbors[i].values[i] = neighbors[i].values[i] ^ 1
            # Calculate the number of clauses satisfied
            neighbors[i].e = evaluate_node(neighbors[i], clauses)
    
    # 4 bits to be changed
    if num_bits == 4:
        neighbor = []
        # Changing all bits
        for i in range(len(node)):
            neighbor.append(node[i]^1)
        neighbors.append(Node(neighbor))
        # Calculate the number of clauses satisfied
        neighbors[-1].e = evaluate_node(neighbors[-1], clauses)
    
    return neighbors
    
def evaluate_node(node, clauses):
    '''
        This function calculates the number of clauses satisfied.
        
        Arguments:
        ----------
            - node: The node whose value is to be evaluated.
            - clauses: A list of clauses in the formula
            
        Returns:
        --------
            The number of clauses statisfied.
    '''
    num_satisfied = 0           # Initialize statisfied clauses to 0
    
    # Calculate the value of each clause by taking OR of each literal 
    for clause in clauses:
        result = 0
        for literal in clause:
            result = result | literal.calculate_value(node.values)
        
        # If satisfied then increment num_satisfied
        if result:
            num_satisfied += 1
    
    # Return the negative of num_satisfied to make it a minimization problem
    return -num_satisfied
    
def is_tautology(clause):
    '''
        This function checks whether a given clause is a tautology.
        The function checks whether the clause contains a variable
        and its negation.
        
        Arguments:
        ----------
            -clause: A list of Literals
            
        Returns:
        --------
            True if the given clause is a tautology else False.
    '''
    # Remove the negation of all the literals in the clause
    for i in range(len(clause)):
        clause[i].is_not = clause[i].is_not | 1
    
    # Check if there is a duplicate variable in the clause
    if len(set(clause)) == len(clause):
        return False
        
    return True 

def goal_test(node, num_clauses):
    '''
        This function checks whether the state is the target(goal) 
        state or not. If it is a target state it returns true otherwise 
        false. The target state should have all the clauses satisfied.
        
        Arguments:
        ----------
            - node: node which needs to be checked
            - num_clauses: The total number of clauses to be satisfied
            
        Returns:
        --------
            True if the given state is the target state else False.
    '''

    return node.e == -num_clauses

def newmovegen(node,clauses,memory):
    '''
        (Move Gen Function for Tabu Search)
        This function accepts a state and returns all the states 
        that can be reached from the given state by changing one
        bits of non-tabu variables.
        
        Arguments:
        ----------
            - node: node/state whose neighbours have to be found
            - clauses: List of clauses to be satisfied
            - memory: memory vector for Tabu Search
            
        Returns:
        --------
            List of Valid neighbours/state which can be visited from
            the given state.
    '''
    
    neighbors = []
    
    # Finding all the possible neighbors to the given node
    for i in range(len(node)):
        copy_node = copy.deepcopy(node)
        neighbors.append(Node(copy_node))
        # Changing the ith bit
        neighbors[i].values[i] = neighbors[i].values[i] ^ 1
        # Calculate the number of clauses satisfied
        neighbors[i].e = evaluate_node(neighbors[i], clauses)
    
    # Deleting the tabu neighbors/nodes
    for i, j in enumerate(memory[::-1]):
        if j != 0:
           del neighbors[len(memory)-i-1] 

    return neighbors