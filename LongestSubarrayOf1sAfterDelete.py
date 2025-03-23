#Sliding window technique is used with a start and end pointer.
#As end increases (our right pointer) check if the number of 0s is greater than 1 (out limit)
#If so then start increasing start until there is only 1 or less 0s in our "window", return the max window length

class Solution(object):
    def longestSubarray(self, nums):
       
        start = 0
        zeros = 0
        final = 0
        
        #Edge case for if no 1s
        if(1 not in nums):
            return 0
        
        #End pointer is just our loop counter
        for end in range(len(nums)):
            
            #If a 0 is found by end pointer, increase number of 0s
            if(nums[end] == 0):
                zeros+=1
               
            #If we are over our limit, increase start until a zero is removed
            while(zeros > 1):
                if(nums[start] == 0):
                    zeros-=1
                start+=1
    
            #Get the current width of our window. + 1 because 0 indexing
            width = end - start + 1
                
            #Get the max
            final = max(width, final)
     
        #Edge case for if no 0s are ever found
        if(zeros == 0):
            return len(nums)-1
             
        #-1 since we do not include the 0       
        return(final-1)
    
print(Solution().longestSubarray([0,1,1,1,0,1,1,0,1]))
print(Solution().longestSubarray([1,1,0,1]))