class Solution(object):
    def longestOnes(self, nums, k):

        start = 0
        end = 0
        zeros = 0
        ones = 0
        final = 0
        
        for i in range(len(nums)):

            
             
            print("Ones: ",ones, "Zeros: ", zeros)
            print("Start: ",start, "End: ", end)
            
            final = max(final, ones)
             
        return final
            
print(Solution().longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3))         
                
        