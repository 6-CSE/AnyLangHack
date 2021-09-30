import sys
from AntColony import AntColony
import time
import matplotlib.pyplot as plt
import random

def _swap_2opt(route, i, k):
    """ Swapping the route """
    new_route = route[0:i]
    new_route.extend(reversed(route[i:k + 1]))
    new_route.extend(route[k + 1:])
    return new_route
    
def tsp_2_opt(city_distances, tour, cost):
    """
    Approximate the optimal path of travelling salesman according to 2-opt algorithm
    Args:
        graph: 2d numpy array as graph
        route: list of nodes
    Returns:
        optimal path according to 2-opt algorithm
    """
    improved = True
    best_found_route = tour
    best_found_route_cost = cost
    while improved:
        improved = False
        
        for i in range(1, len(best_found_route) - 1):
            for k in range(i + 1, len(best_found_route) - 1):
                new_route_cost = (best_found_route_cost - 
                                city_distances[best_found_route[i-1]][best_found_route[i]] - 
                                city_distances[best_found_route[k]][best_found_route[k+1]] + 
                                city_distances[best_found_route[i-1]][best_found_route[k]] + 
                                city_distances[best_found_route[i]][best_found_route[k+1]])
                                
                if new_route_cost < best_found_route_cost:
                    best_found_route_cost = new_route_cost
                    best_found_route = _swap_2opt(best_found_route, i, k)
                    improved = True
                    break
            if improved:
                break
        
    return best_found_route, best_found_route_cost

def Greedy(city_distances, num_cities):
    start_time = time.time()
    best_cost = float('inf')
    tour = []

    for city in range(num_cities):
        
        if (time.time() - start_time) >= 70:
            return best_cost, tour
        
        start_node = city
        visited_cities = set()
        visited_cities.add(start_node)
        tour = []
        tour.append(start_node)
        current_node = start_node
        cost = 0
         
        for i in range(num_cities-1):
            distances = city_distances[current_node]
            
            sorted_distances = sorted(range(len(distances)), key=distances.__getitem__)
            j = 0
            
            while (sorted_distances[j] in visited_cities):
                j += 1
                
            visited_cities.add(sorted_distances[j])
            tour.append(sorted_distances[j])
            current_node = sorted_distances[j]
            # print(sorted_distances[j], distances[sorted_distances[j]])
            cost += distances[sorted_distances[j]]
            
        tour, cost = tsp_2_opt(city_distances, tour, cost)
        
        if cost < best_cost:
            print(cost)
            print(tour)
            print("...................................................................................")
            best_cost = cost
            
    return best_cost, tour