#Trick is to put the senate in a queue and pop until we run out of Rs or Ds
#Using two variables to keep track of how many of each we need to remove was key
#Upon popping, if say its a 'R' then we check if we have any Rs we need to remove, if so, only pop it.
#However if we do not, then add it back to the queue, and add 1 to the to_removeD counter.
#Using a queue and appending back onto the end if a character was not removed simulates taking turns.

class Solution(object):
    def predictPartyVictory(self, senate):
        
        queue = []
        
        d_count = 0
        r_count = 0
        
        for p in senate:
            queue.append(p)
            if p == 'R':
                r_count+=1
            else: 
                d_count+=1
               
        #Keep track of the Ds and Rs we need to remove from the queue
        to_removeD = 0
        to_removeR = 0
        
        while (r_count > 0 and d_count > 0):
            
            curr = queue.pop(0)
            
            #First check if we need to remove any, if not then we add to the to remove D counter and append
            #The R back onto the back of the queue, since it was not removed.
            if curr == 'R':
                if(to_removeR == 0):
                    to_removeD+=1
                    queue.append(curr)
                else:
                    to_removeR-=1
                    r_count-=1
                    
            #Same logic as above, just for other party
            elif curr == 'D':
                if(to_removeD == 0):
                    to_removeR+=1
                    queue.append(curr)
                else:
                    to_removeD-=1
                    d_count-=1
                    
        return 'Dire' if d_count > 0 else 'Radiant'
                    
print(Solution().predictPartyVictory("DDDDD"))
            
        
        
        