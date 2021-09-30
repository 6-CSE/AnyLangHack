from queue import PriorityQueue
from utils import goal_test
from utils import move_gen

def best_first_search(start_node, target_node, heuristic):
    '''
        This function implements the Best-First Search algorithm.
        
        Arguments:
            - target_node: Goal state/node
            - start_node: Start state/node
            - heuristic (function): The heuristic function to
                                    calculate the heuristic value
                                    
        Returns:
            Tuple containing number of states explored and length
            of the path found.
    '''
    states_explored = 0         # variable for number of states explored
    path_length = 0             # variable for length of path
    open_list = PriorityQueue() # create an empty priority queue
    frontier = []               # empty list for frontier
    closed_list = []            # empty list for closed list
    open_list.put(start_node)   # Put the start_node in the open list
    frontier.append(start_node) # Put the start_node in the frontier
    
    # Repeat until the priority queue is not empty
    while not open_list.empty():
        node = open_list.get()  # Pop the node with least heuristic value
        
        print(node.blocks, node.h)  # Print the path
        
        path_length += 1        # Increment the length of the path        
        
        # Check whether the current node is the goal node
        if goal_test(node, target_node):
            target_node.parent = node
            return states_explored, path_length
        
        # Iterate over all the neighbors
        for neighbor in move_gen(node, target_node, heuristic):
            # check whether the node has not been visited
            if neighbor not in frontier and neighbor not in closed_list:
                states_explored +=1         # increment the number of states explored     
                neighbor.parent = node      # assign the parent
                open_list.put(neighbor)     # Put the neighbor in the open list
                frontier.append(neighbor)   # Put the neighbor in the frontier
        
        closed_list.append(node)            # Put the current node in the visited list
        
    return states_explored, path_length   