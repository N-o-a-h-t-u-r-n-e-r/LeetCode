#Trick is to use the sliding window technique. All numbers in the window of size k are summed and then averaged


class Solution(object):
    def findMaxAverage(self, nums, k):
        
        #Find starting sum and max average
        summage = sum(nums[:k])
        max_avg = summage/k
        
        #Only loop to the length of nums - k since our window size is k. We don't want a out of bounds error.
        for i in range(len(nums) - k):
            
            #Substract the number no longer in the window and add the new number in the window with k offset
            summage = summage - nums[i] + nums[i+k]
            max_avg = max((summage/k), max_avg)
            
        return max_avg
    
print(Solution().findMaxAverage([5], 1))