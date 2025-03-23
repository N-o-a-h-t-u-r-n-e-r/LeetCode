#What a load of dogsh#@. There is no trick for this one, the solution is to overwrite the given char list
#We can do this by finding the index for where to insert the number, then subtract 1 from there and place the letter
#The index for where to place the number is also the answer at the end. I appended a 0 onto the end so the last pass is made

class Solution(object):
    def compress(self, chars):
        letter = chars[0]
        count = 0
        ans = 0
        chars.append(0)
  
        for i in range(len(chars)):
            if((letter != chars[i])):
                ans+=1
                chars[ans-1] = letter
                letter = chars[i]
                
                if(count > 1):                
                    for c in str(count):                                      
                        chars[ans] = c
                        ans+=1   
                    count = 1                           
            else:
                count+=1

        return ans
            
            
    
    
          
        
sol = Solution()
print(sol.compress(["a","a","a","b","b","a","a"]))