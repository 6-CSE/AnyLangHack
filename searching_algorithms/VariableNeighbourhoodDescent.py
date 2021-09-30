from queue import PriorityQueue
from Node import Node
from utils import evaluate_node
from utils import move_gen
from utils import goal_test

def VariableNeighbourhoodDescent(start_node, num_variable, clauses):
    '''
        This function implements the Variable Neighbourhood Descent
        algorithm.
        
        Arguments:
        ----------
            - start_node: Start/Initial node for the algorithm
            - num_variable: Number of variables in the formula
            - clauses: The list of clauses to be satisfied
            
        
        Returns:
        --------
            The solution state for given set of clauses i.e the set of
            values for each variable to satisfy all the clauses.
    '''
    
    states_explored = 1             # Start state is visited/explored
    current_node = start_node       # Initialize the current _node as start_node
    
    if goal_test(start_node, len(clauses)):
        print("Number of States explored: ", states_explored)
        return start_node
    
    num_bit = 1
    while True:
        # path_length += 1            # increment the length of path
        open_list = PriorityQueue() # create priority queue for the neighbors
        
        # Search over each neighbor
        for neighbor in move_gen(current_node.values, num_bit, clauses):
            open_list.put(neighbor)
            states_explored += 1    # increment the number of states explored
            
        node = open_list.get()      # Pop the node with least heuristic value
        
        # Check whether the current node is the goal node
        if goal_test(node, len(clauses)):
            print("Number of States explored: ", states_explored)
            return node
        
        # If stuck in Local Minima then change neighborhood relation
        elif node.e >= current_node.e:
            num_bit +=1 
        
        # Update the current node    
        else:
            current_node = node
            