import random

class Ant:
    def __init__(self, num_cities):
        self.path = []
        self.num_cities = num_cities
        self.tour_cost = 0
        
    def construct_tour(self, pheromones, distances, alpha, beta):
        # start_node = start_node
        start_node = random.randint(0, self.num_cities-1)
        visited_cities = set()
        visited_cities.add(start_node)
        
        i = start_node
        cities = list(range(0, self.num_cities))

        self.path.append(start_node)
        while(len(self.path) != self.num_cities):
            probabilities = ([pheromones[i][j]**alpha + (1/distances[i][j])**beta
                             if j not in visited_cities else 0 for j in range(self.num_cities)])                 
            sum_prob = sum(probabilities)
            probabilities = [prob/sum_prob for prob in probabilities]
            
            next_city = random.choices(cities, weights=probabilities)[0]
            visited_cities.add(next_city)
            self.path.append(next_city)
            
            self.tour_cost += distances[i][next_city]

            i = next_city
            
        return self.tour_cost
            