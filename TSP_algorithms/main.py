import sys
from AntColony import AntColony
import time
import matplotlib.pyplot as plt
from Greedy import Greedy

file = open(sys.argv[1], "r") 
type = file.readline()

num_cities = int(file.readline())

city_coordinates = []

for i in range(num_cities):
    city = file.readline().split()
    city = (float(coordinate) for coordinate in city)
    city_coordinates.append(city)
    
city_distances = []

for i in range(num_cities):
    distances = file.readline().split()
    distances = [float(distance) for distance in distances]
    city_distances.append(distances)
    
# print(city_distances[-1])
# print(len(city_distances))
start_time = time.time()
best_cost = float('inf')
best_tour = []

best_cost, best_tour = Greedy(city_distances, num_cities)

init_pheromone = [[10**(-1) for i in range(num_cities)] for j in range(num_cities)]
# for k, i in enumerate(best_tour):
    # j = best_tour[(k+1)%num_cities]
    # init_pheromone[i][j] = num_cities*10/best_cost

while time.time() - start_time <= 280:
    ant = None
    if type == "euclidean":
        if num_cities <= 100:
            ant = AntColony(alpha=4, beta=4, rho=0.1, Q=0.1, city_distances=city_distances, 
                            max_iter=100, num_ants=num_cities//5, sigma=1,
                            init_pheromone=init_pheromone)
        else:
            ant = AntColony(alpha=4, beta=4, rho=0.1, Q=0.1, city_distances=city_distances, 
                            max_iter=100, num_ants=num_cities//4, sigma=1,
                            init_pheromone=init_pheromone)
    else:
        if num_cities <= 100:
            ant = AntColony(alpha=15, beta=14, rho=0.2, Q=1, city_distances=city_distances, 
                            max_iter=100, num_ants=num_cities//5, sigma=1,
                            init_pheromone=init_pheromone)
        else:
            ant = AntColony(alpha=15, beta=14, rho=0.2, Q=1, city_distances=city_distances, 
                            max_iter=100, num_ants=num_cities//4, sigma=1,
                            init_pheromone=init_pheromone)
    ant.optimisation(start_time)
    if ant.best_cost < best_cost:
        best_cost = ant.best_cost
        best_tour = ant.best_tour
        print(ant.best_cost)
        print(ant.best_tour)
        print("...................................................................................")
    
    
print("The final tour length found is =", best_cost)
print("Path of the tour found is :\n", best_tour)


# sum = 0
# for i, city in enumerate(ant.best_tour[:-1]):
    # sum +=city_distances[city][ant.best_tour[(i+1)%num_cities]]

# print(sum)