#This is a prefix sum question, so we iterate through the gain array adding each number at i to the previous
#We put each sum in a new array 'final' and then return the max.

class Solution(object):
    def largestAltitude(self, gain):
        final = [0] * (len(gain))
        
        #Iterate through the gain array and calculate the next number for the final array, we start with 0
        for i in range(len(gain)):
            final[i] = gain[i] + final[i-1]
        
        #If the answer is less than 0, we return 0 since we start with 0    
        return max(final) if max(final) >=0 else 0
    
print(Solution().largestAltitude([44,32,-9,52,23,-50,50,33,-84,47,-14,84,36,-62,37,81,-36,-85,-39,67,-63,64,-47,95,91,-40,65,67,92,-28,97,100,81]))