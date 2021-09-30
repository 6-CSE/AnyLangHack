from queue import PriorityQueue
from utils import goal_test
from utils import move_gen

def hill_climb(start_node,target_node, heuristic):
    '''
        This function implements the Hill Climbing algorithm.
        
        Arguments:
            - target_node: Goal state/node
            - start_node: Start state/node
            - heuristic (function): The heuristic function to
                                    calculate the heuristic value
                                    
        Returns:
            Tuple containing number of states explored and length
            of the path found.
    '''
    states_explored = 1             # variable for number of states explored
    path_length = 1                 # variable for length of path
    side_iterations = 0             # variable for counting number of side moves
    current_node = start_node
    
    # Check whether the current node is the goal node
    if goal_test(current_node,target_node):
        target_node.parent = current_node
        return states_explored, path_length
    
    # Repeat the algorithm until neighbors have less value
    while True:
        path_length += 1            # increment the length of path
        open_list = PriorityQueue() # create priority queue for the neighbors
        
        # Search over each neighbor
        for neighbor in move_gen(current_node, target_node, heuristic):
            neighbor.parent = current_node
            open_list.put(neighbor)
            states_explored += 1    # increment the number of states explored
            
        node = open_list.get()      # Pop the node with least heuristic value
        
        print(node.blocks, node.h)  # Print the path
        
        # Check whether the current node is the goal node
        if goal_test(node,target_node):
            target_node.parent = node
            return states_explored, path_length
        # If neighbors have lesser value than current node then local minima
        elif node.h > current_node.h:
            print("Search is stuck in local minima")
            side_iterations = 0
            return states_explored, path_length
        # If neighbors have value equal to current node then plateau
        elif node.h == current_node.h:
            side_iterations += 1
            if side_iterations >= 1000:
                print("Search is stuck in plateau")
                return count
            current_node = node
        # Update the current_node
        else:
            current_node = node
            side_iterations = 0