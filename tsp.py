from itertools import permutations
from sys import maxsize

class graph:
    connections = []
    number_of_nodes = 0
    number_of_edges = 0
    def _init_(self, no_of_nodes, no_of_edges):
        self.number_of_nodes = no_of_nodes
        self.number_of_edges = no_of_edges
        for i in range(no_of_nodes):
            self.connections.append([])
        for i in range(no_of_nodes):
            for j in range(no_of_nodes):
                self.connections[i].append(0)

    def make_graph(self):
        for i in range(self.number_of_edges):
            print("ENTER CONNECTION <NODE A, NODE B, CONNECTING COST>:", end = " ")
            x, y, c = map(int, input().split())
            self.connections[x][y] = c
            self.connections[y][x] = c
        
        for i in self.connections:
            for j in i:
                if j == 0:
                    j = -1
        for i in range(self.number_of_nodes):
            self.connections[i][i] = 0 
    
    def tsp(self, source):
        nodes = []
        for i in range(self.number_of_nodes):
            if i != source:
                nodes.append(i)
        
        min_path = maxsize
        next_permutation=permutations(nodes)

        print()
        act_path = []
        for i in next_permutation:
    
            current_pathweight = 0
    
            k = source
            for j in i:
                if self.connections[k][j] != -1:
                    current_pathweight += self.connections[k][j]
                    k = j
                else:
                    break
            if self.connections[k][source] != -1:
                current_pathweight += self.connections[k][source]
            else: 
                current_pathweight = maxsize

            min_path = min(min_path, current_pathweight)
            if min_path == current_pathweight and min_path != maxsize:
                act_path = i
        return min_path, act_path

if _name_ == "_main_":
    number_of_nodes = int(input("ENTER NUMBER OF NODES: "))
    number_of_edges = int(input("ENTER NUMBER OF EDGES: "))

    graph_obj = graph(number_of_nodes, number_of_edges)
    graph_obj.make_graph()

    source = int(input("ENTER SOURCE: "))
    ans, path = graph_obj.tsp(source)
    path = list(path)
    path.append(source)
    path.insert(0, source)
    print("PATH FOLLOWED:", path[0], end = " ")
    for i in range(1, len(path)):
        if i < len(path):
            print("->", end = " ")
        print(path[i], end = " ")
    print()
    print("MINIMUM DISTANCE : ", ans)

'''
import copy
inf = float('inf')

class TSP_AI:
    """Traveling Salesman Problem
        -------------------------------------------------------------------
        Traveling Salesman Problem using Nearest Neighbour AI algorithm
    """

    def _init_(self, city_matrix = None, source = 0):
        self.city_matrix = [[0]*4]*4 if city_matrix is None else city_matrix
        self.n : int = len(self.city_matrix)
        self.source : int = source


    def Input(self):
        self.n = int(input('Enter city count : '))

        for i in range(self.n):                                         # Get the distances between cities
            self.city_matrix.append([
                inf if i == j else int(input(f'Cost to travel from city {i+1} to {j+1} : '))
                for j in range(self.n)
            ])

        self.source = int(input('Source: ')) % self.n                   # Get the source city


    def solve(self):
        minCost = inf                                                   # Initially minCost is infinity
        for i in range(self.n):
            print("Path", end='')
            cost = self._solve(copy.deepcopy(city_matrix), i, i)        # Calling solver for each as source city
            print(f" -> {i+1}    :    Cost = {cost}")
            if cost and cost < minCost: minCost = cost                  # If this cost is optimal, save it
        
        return minCost


    def _solve(self, city_matrix, currCity = 0, source = 0):
        if self.n < 2: return 0
        print(f" -> {currCity+1}", end='')

        for i in range(self.n):
            city_matrix[i][currCity] = inf                              # Set all values in the currCity column as infinity (once visited, shouldn't be visited anymore)

        currMin, currMinPos = inf, 0
        for j in range(self.n):
            if currMin > city_matrix[currCity][j]:                      # Get the nearest city to the current city
                currMin, currMinPos = city_matrix[currCity][j], j

        if currMin == inf: return self.city_matrix[currCity][source]    # If currMin is infinity(i.e. all cities have been visited, return cost of moving from this last city to start city to complete the path-loop)
        city_matrix[currCity][currMinPos] = city_matrix[currMinPos][currCity] = inf     # Set distance from currCity to next city and vice versa to infinity
        return currMin + self._solve(city_matrix, currMinPos, source)   # Calling the next recursion for selected city


if _name_ == '_main_':
    city_matrix = [
        [inf, 10,  15,  20],
        [10,  inf, 35,  25],
        [15,  35,  inf, 30],
        [20,  25,  30,  inf]
    ]

    source_city = 0
    tsp = TSP_AI(city_matrix, source_city)
    print(f"Optimal Cost : {tsp.solve()}")
'''
