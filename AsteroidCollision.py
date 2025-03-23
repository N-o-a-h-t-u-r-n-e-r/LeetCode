class Solution(object):
    def asteroidCollision(self, asteroids):
       
        stack = []
       
        for i in asteroids:
     
                while(stack and i < 0 and stack[-1] > 0):
                    
                    if(abs(stack[-1]) < abs(i)):   
                        stack.pop()
                        continue
                    
                    
                    if(abs(stack[-1]) == abs(i)): 
                        stack.pop()
                    break
                    
                else: 
                     stack.append(i)   
                                
                    

                        


        return stack
    
print(Solution().asteroidCollision([5,10,-5]))
                  
            
        