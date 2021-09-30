def heuristic1(target_node,current_node):
    '''
        This function simply checks whether each block is on the 
        correct block, with respect to the final configuration. 
        We subtract one for every block that is on the block it 
        is supposed to be on, and add one for every one that is 
        on a wrong one. For example, the heuristic value for our 
        start state is 6 since every block is not in its correct 
        position and goal state is -6 since all the blocks are in 
        the correct position. With such a function we are looking 
        for smaller values of the heuristic function. In other words, 
        the algorithm is performing steepest gradient descent.
        
        Arguments:
            - target_node: Goal state/node
            - current_node: Node for which heuristic value is to
                            be calculated
                            
        Returns:
            - Heuristic value
    '''
    target_block = target_node.blocks
    current_block = current_node.blocks
    count=0
    for i in range(len(current_block)):
        for j in range(len(current_block[i])):
            try:
                if(target_block[i][j]==current_block[i][j]):
                    count += 1
                else:
                    count = count - 1
            except Exception as e:
                count = count - 1
    
    return -count
    
def heuristic2(target_node, current_node):
    '''
        (Manhattan Distance) This function looks at the entire pile 
        that the block is resting on. If the configuration of the pile 
        is correct, with respect to the goal, it subtracts one for every 
        block in the pile, or else it adds one for every block in that 
        pile. For example, the heuristic value for the start node is 6 = 
        0 + 1 + 2 + 0 + 1 + 2. With such a function we are looking 
        for smaller values of the heuristic function.
        
        Arguments:
            - target_node: Goal state/node
            - current_node: Node for which heuristic value is to
                            be calculated
                            
        Returns:
            - Heuristic value
    '''
    target_block = target_node.blocks
    current_block = current_node.blocks
    count=0
    for i in range(len(current_block)):
        for j in range(len(current_block[i])):
            try:
                if(target_block[i][j]==current_block[i][j]):
                    count += j
                else:
                    count -= j
            except:
                count -= j
    return -count
    
def heuristic3(target_node, current_node):
    '''
        This function looks at the distance between each of the blocks 
        in the current state and the goal state. The x-coordinate of the 
        block is the number of the stack to which it belongs (counting 
        the stack number from left) and the y-coordinate of the block is 
        the position of the block from the bottom in the stack/pile.
        The value of the heuristic is given by the sum of the Manhattan 
        distances for each block. For example, the heuristic value for the 
        start node 12. With such a function we are looking for smaller values 
        of the heuristic function.
        
        Arguments:
            - target_node: Goal state/node
            - current_node: Node for which heuristic value is to
                            be calculated
                            
        Returns:
            - Heuristic value
    '''
    target_block = target_node.blocks
    current_block = current_node.blocks
    count = 0
    for i in range(len(current_block)):
        for j in range(len(current_block[i])):
            index = None
            for k in range(len(target_block)):
                try:
                    index = (k, target_block[k].index(current_block[i][j]))
                    break
                except:
                    continue
            count += abs(i - index[0]) + abs(j - index[1])
    return count