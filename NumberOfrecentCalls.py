#A simple queue question, just add the new value and pop until the new ping minus the old ping is less than 3000
#We are finding the difference, so having just one value > 3000 by itself is fine

class RecentCounter(object):

    def __init__(self):
        self.requests = []

    def ping(self, t):
        
        
        self.requests.append(t)
        while(t -  self.requests[0] > 3000):
             self.requests.pop(0)
            
        return len( self.requests)
            

# Your RecentCounter object will be instantiated and called as such:
obj = RecentCounter()
param_1 = obj.ping(500)
print(param_1)