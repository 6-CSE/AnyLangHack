from Node import Node
from heuristic import heuristic1
from heuristic import heuristic2
import copy

def read_input(node, file):
    '''
        This function is to read the inputs from the input file
        and store them in the corresponding 2-D array.
        
        Arguments:
            - node: An object of the Node class
            - file: File object for the input file
            
        Returns:
            None
    '''
    for i in range(3):                  # iterate over the 3 stacks
        line = file.readline()  
        line = line[1:-2]               # Removing []
        line = line.replace(" ", "")    # Replace whitespaces
        blocks_list = line.split(",")   # Replace ,
        blocks_list = [int(block) for block in blocks_list if len(block) > 0]
        node.blocks.append(blocks_list) # Add the block list to the blocks
        
def move_gen(node, target_node, heuristic):
    '''
        This function accepts a state and returns all the states 
        that can be reached from the given state in one step.
        
        Arguments:
            - node: node/state whose neighbours have to be found
            - target_node: Goal state/node
            - heuristic (function): function to calculate the heuristic value
            
        Returns:
            List of Valid neighbours/state which can be visited from
            the given state. 
    '''
    
    neighbours = []
    for i, blocks_list in enumerate(node.blocks):
        if len(blocks_list) > 0:
            for j in range(1, 3):
                neighbour = Node()      # Initialize a new Node
                neighbour.blocks = copy.deepcopy(node.blocks)
                # Move the top-most block
                block = neighbour.blocks[i].pop(-1)
                neighbour.blocks[(i+j)%3].append(block)
                # Calculate the heuristic value
                neighbour.h = heuristic(target_node, neighbour)
                neighbours.append(neighbour)
    return neighbours
    
def goal_test(node, target_node):
    '''
        This function checks whether the state is the target(goal) 
        state or not. If it is a target state it returns true otherwise 
        false.
        
        Arguments:
            - node: node which needs to be checked
            - target_node: Goal node/state
            
        Returns:
            True if the given state is the target state else False.
    '''
    
    if node == target_node:
        return True
    return False