class Solution(object):
    
    # Global counter
    def __init__(self):
        self.res = 0 
    
    def minReorder(self, n, connections):
        matrix = {i: [] for i in range(n)}  # Initialize adjacency list
        
        #Use a set to convert connections list to a set to perform constant time lookup
        connection_set = set()

         #Initialize visited set to avoid checking paths more than once
        visited = set()
        
        #Create the undirected adjacency list and a set for fast lookup
        for u, v in connections:
            matrix[u].append(v)
            matrix[v].append(u)
            #Add the directed edge (u -> v)
            connection_set.add((u, v)) 
        
        
        #Start BFS from city 0 so we know we are traversing away from it
        self.bfs(0, matrix, visited, connection_set)
        
        return self.res
        
    def bfs(self, city, matrix, visited, connection_set):
        #Mark the current city as visited
        visited.add(city)
        
        # Visit all neighbors of the current city
        for neighbor in matrix[city]:
            # We avoid revisiting the same city
            if neighbor not in visited:
                #Check if the directed edge exists from city to its neighbor
                if (city, neighbor) in connection_set:
                    #This means the road needs to be re-directed
                    self.res += 1 
                    
                #Perform a recursive BFS on the unvisited neighbor
                self.bfs(neighbor, matrix, visited, connection_set)
    

sol = Solution()
print(sol.minReorder(6, [[0,1], [1,3], [2,3], [4,0], [4,5]]))