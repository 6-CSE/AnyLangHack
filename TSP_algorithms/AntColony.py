from Ant import Ant
import time

class AntColony:
    def __init__(self, alpha, beta, rho, Q, city_distances, max_iter, num_ants, sigma, init_pheromone):
        self.alpha = alpha
        self.beta = beta
        self.rho = rho
        self.Q = Q
        self.city_distances = city_distances
        self.max_iter = max_iter
        self.num_ants = num_ants
        self.sigma = sigma
        
        self.num_cities = len(city_distances)
        self.pheromones = init_pheromone
        self.best_cost = float('inf')
        self.best_tour = None
        self.best_index = None
        self.omega = int(0.1*self.num_cities)
        
    def optimisation(self, start_time):
        for i in range(self.max_iter):
        
            if time.time() - start_time >= 280:
                break
            
            ants = [Ant(self.num_cities) for j in range(self.num_ants)]
            
            tour_costs = [ant.construct_tour(self.pheromones, self.city_distances,
                          self.alpha, self.beta) for ant in ants]
                          
            sorted_tour_costs = sorted(range(len(tour_costs)), key=tour_costs.__getitem__)
                          
            [self.set_best_index(i) for i in range(len(tour_costs)) if tour_costs[i] < self.best_cost]
            
            if self.best_index:
                self.best_cost = tour_costs[self.best_index]
                self.best_tour = ants[self.best_index].path
                
            self.set_best_index(None)
            
            self.best_tour, self.best_cost = self.tsp_2_opt(self.city_distances, self.best_tour, self.best_cost, start_time)
            
            delta_pheromone = [[0 for i in range(self.num_cities)] for j in range(self.num_cities)]
            for index in range(self.omega):
                ant = ants[sorted_tour_costs[index]]
                for k, i in enumerate(ant.path):
                    j = ant.path[(k+1)%self.num_cities]
                    delta_pheromone[i][j] += (self.sigma - index)*self.Q/tour_costs[sorted_tour_costs[index]]
            
            # delta_pheromone = [[0 for i in range(self.num_cities)] for j in range(self.num_cities)]
            # for index, ant in enumerate(ants):
                # for k, i in enumerate(ant.path):
                    # j = ant.path[(k+1)%self.num_cities]
                    # delta_pheromone[i][j] += self.Q/tour_costs[index]
                    
            elitist_pheromone = [[0 for i in range(self.num_cities)] for j in range(self.num_cities)]
            for k, i in enumerate(self.best_tour):
                j = self.best_tour[(k+1)%self.num_cities]
                elitist_pheromone[i][j] = self.sigma*self.Q/self.best_cost
                    
            for u in range(self.num_cities):
                for v in range(self.num_cities):
                    self.pheromones[u][v] = ((1-self.rho)*self.pheromones[u][v] + 
                                            delta_pheromone[u][v] + elitist_pheromone[u][v])
                    
    def set_best_index(self, i):
        self.best_index = i
        
    def _swap_2opt(self, route, i, k):
        """ Swapping the route """
        new_route = route[0:i]
        new_route.extend(reversed(route[i:k + 1]))
        new_route.extend(route[k + 1:])
        return new_route
        
    def tsp_2_opt(self, city_distances, tour, cost, start_time):
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
            
            if time.time() - start_time >= 280:
                break
            
            for i in range(1, len(best_found_route) - 1):
                for k in range(i + 1, len(best_found_route) - 1):
                    
                    new_route_cost = (best_found_route_cost - 
                                    city_distances[best_found_route[i-1]][best_found_route[i]] - 
                                    city_distances[best_found_route[k]][best_found_route[k+1]] + 
                                    city_distances[best_found_route[i-1]][best_found_route[k]] + 
                                    city_distances[best_found_route[i]][best_found_route[k+1]])
                                    
                    if new_route_cost < best_found_route_cost:
                        best_found_route_cost = new_route_cost
                        best_found_route = self._swap_2opt(best_found_route, i, k)
                        improved = True
                        break
                if improved:
                    break
            
        return best_found_route, best_found_route_cost
            