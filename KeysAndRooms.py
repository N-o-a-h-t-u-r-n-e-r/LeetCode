#Do a DFS to visit all rooms and add a key to the stack if it hasnt been visited already
#If the length of our visited rooms is equal to all the rooms, then return true as we
#have seen all rooms

class Solution(object):
    def canVisitAllRooms(self, rooms):
        n = len(rooms)
        #Edge Case
        if(n <= 1):
            return True
        #Stack to perform DFS
        stack = [rooms[0]]
        
        #Dictionary to keep track of visited rooms
        visited = {0}
        
        while(stack):
            room = stack.pop()
            for key in room:
                #If its found, skip to the next key
                if key in visited:
                    continue
                
                #Otherwise add it to our stack so we can visit that room and add the key to visited
                stack.append(rooms[key])
                visited.add(key)
        return(n == len(visited))