import sys
import time
from Node import Node
from utils import read_input
from bfs import best_first_search
from heuristic import heuristic1
from heuristic import heuristic2
from heuristic import heuristic3
from hill import hill_climb

if len(sys.argv) != 4:
    print("Usage: ./run.sh [INPUT TEXT FILE] [ALGORITHM CHOICE] [HEURISTIC CHOICE]")
    print("Algorithm Choice:\n\t-bfs: Best First Search\n\t-hill: Hill Climbing")
    print("Heuristic Choice:\n\tA number between 1 and 3 (both inclusive)")
    quit()

file = open(sys.argv[1], "r")       # Reading test case file name
file.readline()                     

start_node = Node()                 # Creating start node object
read_input(start_node, file)        # reading the initial state    

# ignoring the extra lines
file.readline()
file.readline()

goal_node = Node()                  # Creating goal node object
read_input(goal_node, file)         # reading the goal state

algo_choice = sys.argv[2]
heuristic_choice = int(sys.argv[3])

# Calculating the heuristic value for start node and goal node
heuristic = None
if heuristic_choice == 1:
    heuristic = heuristic1
    start_node.h = heuristic1(goal_node, start_node)
    goal_node.h = heuristic1(goal_node, goal_node)
elif heuristic_choice == 2:
    heuristic = heuristic2
    start_node.h = heuristic2(goal_node, start_node)
    goal_node.h = heuristic2(goal_node, goal_node)
elif heuristic_choice == 3:
    heuristic = heuristic3
    start_node.h = heuristic3(goal_node, start_node)
    goal_node.h = heuristic3(goal_node, goal_node)
else:
    print("The heuristic choice should be between 1 and 3 (both inclusive)")

# Using the appropriate algorithm
if algo_choice == "bfs":
    start_time = time.time()
    result = best_first_search(start_node, goal_node, heuristic)
    print("States Explored: {}\nPath Length: {}\n".format(result[0], result[1]))
    print("Time taken: " + str(time.time() - start_time))
elif algo_choice == "hill":
    start_time = time.time()
    result = hill_climb(start_node, goal_node, heuristic)
    print("States Explored: {}\nPath Length: {}\n".format(result[0], result[1]))
    print("Time taken: " + str(time.time() - start_time))
else:
    print("The algorithm chosen should be either `bfs` or `hill` without quotes")