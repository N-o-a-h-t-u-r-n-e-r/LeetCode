#Trick is to create an array to hold the sums, then at each index in the sum array, check if the current sum
#is equal to the total sum - the previous element. If so, then we have found our index

class Solution(object):
    def pivotIndex(self, nums):
        
        sums = [0] * len(nums)
        sums[0] = nums[0]
        
        #Create sum array
        for i in range(1, len(nums)):
            sums[i] = nums[i] + sums[i-1]
            
            
        
        for i in range(0, len(nums)):
            
            #Edge case for when i-1 doesnt exist, we substitute 0
            if(i == 0):
                if(sums[i] == sums[-1] - 0):
                    return i
                
            #Otherwise normal calculation
            else:
                if(sums[i] == sums[-1] - sums[i-1]):
                    return i
          
        #Default case for if no pivot is found  
        return -1
    
print(Solution().pivotIndex([0,-1,-1,-1,-1,-1]))