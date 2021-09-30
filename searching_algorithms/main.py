import sys
import numpy as np
import copy
from Literal import Literal
from utils import is_tautology
from utils import evaluate_node
from utils import move_gen
from utils import newmovegen
from Node import Node
from BeamSearch import BeamSearch
from VariableNeighbourhoodDescent import VariableNeighbourhoodDescent
from TabuSearch import TabuSearch

if len(sys.argv) != 4:
    print("Usuage: ./run.sh [Beam-Width] [Tabu-Tenure] [OUTPUT-FILE]")
    quit()

n = 4
k = 5

# Creating list of all possible literals to choose from
literals = [Literal(i, j) for i in range(n) for j in range(2)]
clauses = set()         # Initializing a set for all possible literals

# Randomly generating clauses
while len(clauses) != k:
    # Randomly generate clause with each literal having probability
    # of 1/2n
    clause = np.random.choice(literals, size=3, replace=False)
    copy_clause = copy.deepcopy(clause)
    # Check whether the generates clause is a tautology 
    if not is_tautology(copy_clause):
        clauses.add(frozenset(clause))

# Wrting the clauses generated into a file
file = open(sys.argv[3], "w")    
for clause in clauses:
    for i, literal in enumerate(clause):
        if i != 2:
            file.write(str(literal))
            file.write(" + ")           # + for OR operation
        else:
            file.write(str(literal))
    file.write("\n")

# Initializing start node    
start_node = Node([1, 0, 0, 1])
start_node.e = evaluate_node(start_node, clauses)

beam_width = int(sys.argv[1])
tabu_tenure = int(sys.argv[2])

print("Beam Search")
print("------------")
print("Solution:", BeamSearch(beam_width, clauses))
print("\nVariable Neighbourhood Descent")
print("------------------------------")
print("Solution:", VariableNeighbourhoodDescent(start_node, n, clauses))
print("\nTabu Search")
print("-----------")
print("Solution:", TabuSearch(start_node, tabu_tenure, clauses))