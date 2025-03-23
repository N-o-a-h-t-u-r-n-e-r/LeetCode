#We can use DFS to explore the city of the index where a 1 is found.
#Whatever index we find the 1 at, we dfs there and keep doing so until all cities have been visited

class Solution:
    def findCircleNum(self, isConnected):
        
        #DFS function, if we find another non-visited city, then call itself and pass in the index for that city
        def dfs(i):
            for j in range(len(isConnected)):
                if isConnected[i][j] and not visited[j]:
                    visited[j] = True
                    dfs(j)

        n = len(isConnected)
        visited = [False] * n
        provinces = 0

        #Main Loop that will check every city(i) and if a connection hasnt been visited, then call dfs
        for i in range(n):
            if not visited[i]:
                provinces += 1
                visited[i] = True
                dfs(i)

        return provinces