from queue import PriorityQueue
from Node import Node
from utils import evaluate_node
from utils import newmovegen
from utils import goal_test

def TabuSearch(start_node, tabu_tenure, clauses):
    '''
        This function implements the Tabu Search algorithm.
        
        Arguments:
        ----------
            - start_node: Start/Initial node for the algorithm
            - tabu_tenure: The maximum number of iterations for which
                           the a bit after modification should be
                           considered Tabu
            - clauses: A list of clauses
            
        Returns:
        --------
            The solution state for given set of clauses i.e the set of
            values for each variable to satisfy all the clauses.                 
    '''
    
    states_explored = 1                 # Start state is visited/explored
    current_node = start_node           # Initialize the current _node as start_node
    MAX_TRIES = 100                     # Run Tabu Search for MAX_TRIES iterations
    memory = [0]*len(start_node.values) # Initialize Memory Vector for Tabu Search
    
    # Check if the initial node is the goal node
    if goal_test(start_node, len(clauses)):
        print("Number of States explored: ", states_explored)
        return start_node
    
    for i in range(MAX_TRIES):
        open_list = PriorityQueue() # create priority queue for the neighbors
        
        # Expanding the current node
        for neighbor in newmovegen(current_node.values, clauses, memory):
            open_list.put(neighbor)
            states_explored += 1    # increment the number of states explored
        
        node = open_list.get()      # Pop the best neighbor
        
        # Check whether the best neighbor is a goal node
        if goal_test(node, len(clauses)):
            print("Number of States explored: ", states_explored)
            return node
        
        # Update the memory vector for Tabu Search
        update_memory(memory, current_node, node, tabu_tenure)
        
        current_node = node             # Update the current node
        
        # If end of Search appears and Solution is not found
        if i == MAX_TRIES-1:
            print("No Solution found for MAX_TRIES = 100")
            return
    
def update_memory(memory, current_node, next_node, tabu_tenure):
    '''
        This function updates the memory vector for Tabu Search.
        
        Arguments:
        ----------
            - memory: Memory Vector for Tabu Search which is to be
                      updated.
            - current_node: Node which is being visited in Tabu Search
            - next_node: Node which will be visited next in Tabu Search
            - tabu_tenure: The maximum number of iterations for which
                           the a bit after modification should be
                           considered Tabu
                           
       Returns:
       --------
            None
    '''
    
    # Iterating over all the variables
    for i in range(len(current_node.values)):
        # Check if the values are same for both the nodes
        if current_node.values[i] == next_node.values[i]:
            if memory[i] != 0:
                memory[i] -= 1          # Decrement the memory value
        else:
            memory[i] = tabu_tenure     # Update memory for the bit modified