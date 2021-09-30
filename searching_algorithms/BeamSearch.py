import numpy as np
from queue import PriorityQueue
from Node import Node
from utils import evaluate_node
from utils import move_gen
from utils import goal_test

def BeamSearch(beam_width, clauses):
    '''
        This function implements the Beam Search algorithm.
        
        Arguments:
        ----------
            - beam_width (b): beam_width for the Beam Search algorithm
            - clauses: List of clauses to be satisfied
            
        Returns:
        --------
            The solution state for given set of clauses i.e the set of
            values for each variable to satisfy all the clauses.
    '''
    
    # Initially beam width states will be explored
    states_explored = beam_width
    
    # Randomly generate beam width states
    start_states = np.random.randint(low=0, high=2, size=(beam_width, 4))
    
    print("Initial State:\n", start_states)
    
    best_neighbor = []                      # List of best b neighbors
    
    for node in start_states:
        start_node = Node(list(node))
        # Calculate the number of clauses satisfied
        start_node.e = evaluate_node(start_node, clauses)
        best_neighbor.append(start_node)
        
        # Check whether the current node is the goal node
        if goal_test(start_node, len(clauses)):
            print("Number of States explored: ", states_explored)
            return start_node
    
    
    while True:
        open_list = PriorityQueue()         # Initialize a Min Priority Queue
        
        result = True                       # boolean for determing local minima problem
        
        # Considering b best neighbors
        for i in range(beam_width):
            neighbors = PriorityQueue()     # Initialize a Min Priority Queue
            # Expanding each of the best neighbors
            for neighbor in move_gen(best_neighbor[i].values, 1, clauses):
                open_list.put(neighbor)     # Putting the neighbor in the open list
                neighbors.put(neighbor)     # Putting the neighbor in the open list     
                states_explored += 1        # Incrementing the state explored
                
            neighbor = neighbors.get()      # Finding the best neighbor of the expanded node
            
            # Check for local minima problem
            result = result & (neighbor.e >= best_neighbor[i].e)
        
        # If result is True, then stuck in local minima problem
        if result:
            print("Search is stuck in local minima")
            print("Number of States explored: ", states_explored)
            return
        
        # Finding the b best neighbors
        best_neighbor = []
        
        for i in range(beam_width):
            neighbor = open_list.get()      # popping b best neighbors from open list
            best_neighbor.append(neighbor)
            
            # Check whether if the neighbor is a goal node
            if goal_test(neighbor, len(clauses)):
                print("Number of States explored: ", states_explored)
                return neighbor
                
        # [print(neighbor.values, neighbor.e) for neighbor in best_neighbor]