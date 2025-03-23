#Trick is to keep a count of each number found in a hashmap, with the number as the key and the count as the value
#If a match is found then increase operations and decrease the count of the number in the hashmap, since we 
#dont want to use it again

class Solution(object):
    def maxOperations(self, nums, k):
       
        hMap = {}       
        operations = 0
        
        for n in nums:
            #If a match is found and there is still one available, then increase operation count
            if((k - n) in hMap and hMap[k-n] > 0):
                operations+=1
                hMap[k-n] -= 1 
                
            #Otherwise add it to our hashmap or increase the count in our hashmap            
            else:
                if(n in hMap):
                    hMap[n] +=1
                else:
                    hMap[n] = 1
                
        return operations
    
print(Solution().maxOperations([1,2,3,4], 5))
        